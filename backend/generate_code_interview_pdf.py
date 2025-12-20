from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    
    # --- Custom Styles ---
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.darkblue
    )
    
    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=10,
        textColor=colors.darkgreen,
        borderPadding=5,
        borderColor=colors.lightgrey,
        borderWidth=1,
        backColor=colors.whitesmoke
    )
    
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Heading3'],
        fontSize=12,
        spaceBefore=10,
        spaceAfter=4,
        textColor=colors.black
    )
    
    answer_style = ParagraphStyle(
        'Answer',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        spaceAfter=8,
        leftIndent=15,
        textColor=colors.darkslategrey
    )
    
    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier',
        backColor=colors.lightgrey,
        borderPadding=4,
        spaceAfter=10,
        leftIndent=20
    )

    story = []
    
    # --- Content ---
    
    story.append(Paragraph("Nexus AI: Technical Interview Q&A", title_style))
    story.append(Paragraph("A comprehensive quiz deck for mastering the codebase.", styles['Italic']))
    story.append(Spacer(1, 20))
    
    # Data Structure for Q&A
    sections = [
        {
            "title": "1. LangGraph & Agent Architecture",
            "qa": [
                {
                    "q": "What is the specific role of 'AgentState' in `graph/state.py`?",
                    "a": "It defines the schema for the graph's shared memory. It is a `TypedDict` containing `messages` (a list of BaseMessage objects) and `next` (a string indicating the next node). It enforces type safety across the workflow."
                },
                {
                    "q": "Explain the significance of `Annotated[List[BaseMessage], operator.add]`.",
                    "a": "The `operator.add` is a reducer function. It tells LangGraph that when a node returns a dictionary with a 'messages' key, it should slightly <b>append</b> the new messages to the existing list rather than overwriting it entirely."
                },
                {
                    "q": "How does the `supervisor_node` decide the next step?",
                    "a": "It constructs a prompt with conversation history and asks an LLM (Ollama/Llama3) to choose between 'researcher', 'writer', or 'FINISH'. It expects a JSON response explicitly."
                },
                {
                    "q": "What is the 'Fail-Working' mechanism in the Supervisor?",
                    "a": "If the LLM outputs malformed JSON or crashes, the node catches the exception and actively defaults to returning `{'next': 'researcher'}`. This ensures the agent loop doesn't break due to a parsing error."
                },
                {
                    "q": "What edge case does the regex `re.search(r'\{.*\}', ...)` handle?",
                    "a": "Local models often are 'chatty' and wrap JSON in text (e.g., 'Here is your JSON: {...}'). The regex extracts just the JSON object from the surrounding noise."
                }
            ]
        },
        {
            "title": "2. Backend Engineering (FastAPI)",
            "qa": [
                {
                    "q": "Why is `ingest_document` imported inside the function scope in `api/upload`?",
                    "a": "To implement a <b>Lazy Import</b>. This prevents heavy dependencies (like Chroma or HuggingFace) from loading at startup if they aren't immediately needed, improving app startup time and avoiding circular import issues."
                },
                {
                    "q": "What is the purpose of `CORSMiddleware` in `main.py`?",
                    "a": "It removes browser security restrictions that prevent the Frontend (running on a different port, e.g., 5173) from making API calls to the Backend (port 8000). `allow_origins=['*']` is a permissive setting for development."
                },
                {
                    "q": "How is the user's request validated before reaching the logic?",
                    "a": "We use a Pydantic model `ChatRequest(BaseModel)`. FastAPI automatically validates that the incoming JSON body matches this schema (specifically, a `message` string field) and returns 422 Error if it doesn't."
                },
                {
                    "q": "Describe the data flow in `chat_endpoint`.",
                    "a": "1. Receive `ChatRequest`. 2. Wrap message in `HumanMessage`. 3. Call `graph.invoke(inputs)`. 4. Wait for execution to finish. 5. Extract the last message from result state. 6. Return response + full history."
                }
            ]
        },
        {
            "title": "3. RAG Implementation (ChromaDB)",
            "qa": [
                {
                    "q": "Which embedding model is used and what is its advantage?",
                    "a": "<b>all-MiniLM-L6-v2</b> via `HuggingFaceEmbeddings`. It is a small, high-performance model that runs efficiently on local CPUs, eliminating the need for paid APIs like OpenAI Ada."
                },
                {
                    "q": "Why use specific chunking parameters (Size: 1000, Overlap: 200)?",
                    "a": "Large chunks (1000) capture full thoughts/paragraphs. The overlap (200) ensures that sentences at the boundaries of chunks aren't cut in half, preserving semantic context for retrieval."
                },
                {
                    "q": "What does `persist_directory='./chroma_db'` achieve?",
                    "a": "It configures ChromaDB to save the vector index to the hard drive. Without this, the knowledge base would be lost every time the backend server restarts (in-memory only)."
                },
                {
                    "q": "What happens in the `researcher_node`?",
                    "a": "It takes the last user message, turns it into a query for the Retriever (Chroma), fetches relevant docs, and returns them as a new `HumanMessage` prefixed with 'Context found:'."
                }
            ]
        },
        {
            "title": "4. Frontend & React Concepts",
            "qa": [
                {
                    "q": "Why use `useRef` for the chat window?",
                    "a": "To hold a mutable reference to the 'bottom' DOM element (`messagesEndRef`). This allows us to imperatively call `scrollIntoView()` whenever new messages arrive."
                },
                {
                    "q": "How is the `isLoading` state used for UX?",
                    "a": "It conditionally renders a loading spinner or disable the input button while waiting for the backend. It prevents the user from double-submitting and provides visual feedback."
                },
                {
                    "q": "What is the benefit of using Tailwind functions like `classNames`?",
                    "a": "It allows for dynamic class strings based on state (e.g., `msg.role === 'user' ? 'bg-blue-500' : 'bg-gray-700'`), keeping the JSX clean."
                }
            ]
        }
    ]
    
    # Loop through sections and questions
    for section in sections:
        story.append(Paragraph(section['title'], section_header_style))
        
        for index, item in enumerate(section['qa'], 1):
            q_text = f"Q{index}: {item['q']}"
            story.append(Paragraph(q_text, question_style))
            story.append(Paragraph(item['a'], answer_style))
        
        story.append(Spacer(1, 10))

    doc.build(story)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    create_pdf("Nexus_Detailed_Interview_QA.pdf")
