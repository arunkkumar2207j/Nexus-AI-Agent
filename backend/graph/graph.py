from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import supervisor_node, researcher_node, writer_node

def create_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("writer", writer_node)
    
    workflow.set_entry_point("supervisor")
    
    def router(state):
        return state["next"]
    
    workflow.add_conditional_edges(
        "supervisor",
        router,
        {
            "researcher": "researcher",
            "writer": "writer",
            "FINISH": END
        }
    )
    
    workflow.add_edge("researcher", "supervisor")
    workflow.add_edge("writer", "supervisor") # Or END if writer is final
    
    return workflow.compile()
