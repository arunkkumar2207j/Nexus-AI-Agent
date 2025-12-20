from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from .state import AgentState
from services.vector_store import get_retriever

# LLM Selection (Default to Ollama for free, fallback/env for OpenAI)
# In a real app, this would be config-driven.
# Assuming 'llama3' model for Ollama.
# llm = ChatOllama(model="llama3", format="json") # Moved inside node

def supervisor_node(state: AgentState):
    """
    Decides which worker to call next or if we are done.
    """
    options = ["researcher", "writer", "FINISH"]
    
    system_prompt = (
        "You are a supervisor tasked with managing a conversation between the"
        " following workers:  {members}. Given the following user request,"
        " respond with the worker to act next. Each worker will perform a"
        " task and respond with their results. When finished, respond with FINISH."
        " Output JSON: {{'next': 'worker_name'}}"
    )
    
    members = ["researcher", "writer"]
    messages = [SystemMessage(content=system_prompt.format(members=", ".join(members)))] + state["messages"]
    
    # Init LLM here to avoid global scope issues
    try:
        llm = ChatOllama(model="llama3") 
        response = llm.invoke(messages)
    except Exception as e:
         print(f"[ERROR] ChatOllama invoke failed: {e}")
         return {"next": "researcher"} # Force researcher on error

    # Simple JSON parsing (in production use structured output parser)
    import json
    import re
    
    try:
        # Try direct parse
        content = json.loads(response.content)
        next_step = content.get("next", "researcher") # Default to researcher if key missing
    except:
        # Try extracting JSON from text
        match = re.search(r"\{.*\}", response.content, re.DOTALL)
        if match:
            try:
                content = json.loads(match.group(0))
                next_step = content.get("next", "researcher")
            except:
                next_step = "researcher"
        else:
            print(f"[DEBUG] Supervisor JSON Parse Failed. Fallback to researcher.")
            next_step = "researcher" # Fallback to researcher to ensure action

    return {"next": next_step}

def researcher_node(state: AgentState):
    """
    Uses RAG to find information.
    """
    retriever = get_retriever()
    last_message = state["messages"][-1]
    query = last_message.content
    
    # RAG Lookup
    print(f"[DEBUG] Researcher querying: {query}")
    docs = retriever.invoke(query)
    print(f"[DEBUG] Researcher found {len(docs)} documents.")
    context = "\n\n".join([d.page_content for d in docs])
    if len(docs) > 0:
        print(f"[DEBUG] First doc preview: {docs[0].page_content[:100]}...")
    
    return {"messages": [HumanMessage(content=f"Context found:\n{context}")]}

def writer_node(state: AgentState):
    """
    Generates the final answer.
    """
    model = ChatOllama(model="llama3") # Text mode
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}
