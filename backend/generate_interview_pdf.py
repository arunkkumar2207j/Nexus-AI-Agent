from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = styles['Title']
    heading_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.darkblue
    )
    body_style = styles['BodyText']
    
    story = []
    
    # Title
    story.append(Paragraph("Nexus AI Agent - Interview Questions & Answers", title_style))
    story.append(Spacer(1, 12))
    
    questions = [
        {
            "q": "1. What is the overall architecture of this project?",
            "a": "The project is a full-stack AI agent application. The **Frontend** is built with React, Vite, and TailwindCSS using TypeScript. The **Backend** is a Python FastAPI server. The core AI logic uses **LangGraph** to manage a stateful workflow between a 'Supervisor' node and worker nodes ('Researcher', 'Writer'). It uses **Ollama** for local LLM inference (Llama 3) and **ChromaDB** as a vector store for RAG (Retrieval Augmented Generation)."
        },
        {
            "q": "2. Why clear Supervisor logic is important in Multi-Agent systems?",
            "a": "A Supervisor acts as the router. In this project, the Supervisor node decides whether to delegate work to a 'Researcher' (if external info is needed), a 'Writer' (to synthesize an answer), or to 'FINISH'. Without clear logic (and robust error handling), the agent can get stuck in loops or fail to return a satisfying answer. We implemented robust JSON parsing and fallback mechanisms to ensure the Supervisor always makes a valid decision."
        },
        {
            "q": "3. Explain the RAG pipeline used here.",
            "a": "The RAG (Retrieval Augmented Generation) pipeline consists of two parts: **Ingestion** and **Retrieval**. During ingestion, a PDF is loaded, split into chunks (using RecursiveCharacterTextSplitter), embedded (using HuggingFace embeddings), and stored in ChromaDB. During retrieval (in the 'Researcher' node), the user's query is embedded, relevant chunks are fetched from ChromaDB, and these chunks are passed as context to the LLM to generate an informed response."
        },
        {
            "q": "4. What challenge did you face with LangChain/Ollama and how did you solve it?",
            "a": "We faced an issue where `ChatOllama` with `format='json'` caused the LLM to hang indefinitely. This was likely due to a compatibility issue or model constraint. We solved it by removing the strict JSON mode constraints and instead implementing a robust regex-based parser in the Supervisor node to extract the JSON decision from the model's natural language output. We also implemented a fallback to ensure the agent defaults to 'researcher' if parsing fails."
        },
        {
            "q": "5. Why use LangGraph instead of standard LangChain chains?",
            "a": "Standard chains are typically DAGs (Directed Acyclic Graphs) and are linear. **LangGraph** allows for cyclic graphs, which are essential for agentic loops (e.g., Supervisor -> Researcher -> Supervisor). This enables the agent to 'think' and iterate: if the research isn't sufficient, the Supervisor can send it back to the Researcher again before finalizing."
        },
        {
            "q": "6. How do you handle frontend-backend communication?",
            "a": "We use REST APIs. The React frontend sends POST requests to the FastAPI backend (`/api/chat`). We handle CORS (Cross-Origin Resource Sharing) in FastAPI to allow the frontend (localhost:5173) to communicate with the backend (localhost:8000). We also implemented a `/health` endpoint for monitoring connectivity."
        }
    ]
    
    for item in questions:
        story.append(Paragraph(item['q'], heading_style))
        story.append(Paragraph(item['a'], body_style))
        story.append(Spacer(1, 12))
        
    doc.build(story)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    create_pdf("Nexus_Interview_Questions.pdf")
