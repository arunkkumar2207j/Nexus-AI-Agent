from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

print("Init LLM...")
llm = ChatOllama(model="llama3:latest")
print("Invoking...")
try:
    res = llm.invoke([HumanMessage(content="Hello")])
    print(f"Response: {res.content}")
except Exception as e:
    print(f"Error: {e}")
