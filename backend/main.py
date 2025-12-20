import os
import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from graph.graph import create_graph
# from services.vector_store import ingest_document # Import later to avoid init issues if dependencies generic

app = FastAPI(title="Nexus AI Analyst")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for dev to fix "Failed to fetch"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Graph
graph = create_graph()

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running"}

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Invokes the agent graph and returns the final response.
    TODO: Upgrade to StreamingResponse for real-time visualization.
    """
    try:
        inputs = {"messages": [HumanMessage(content=request.message)]}
        # For simplicity in this demo, we invoke and return final state.
        # Ideally, we yield events. 
        result = graph.invoke(inputs)
        last_message = result["messages"][-1]
        return {"response": last_message.content, "history": [m.content for m in result["messages"]]}
    except Exception as e:
        print(f"[ERROR] Chat Endpoint failed: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    from services.vector_store import ingest_document # Lazy import
    
    try:
        temp_dir = "temp_uploads"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, file.filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        count = ingest_document(file_path)
        
        # Cleanup
        os.remove(file_path)
        
        return {"message": f"Successfully ingested {count} chunks from {file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
