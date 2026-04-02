# Nexus AI Agent

Nexus AI Agent is a sophisticated multi-agent orchestration platform designed to handle complex workflows and retrieval-augmented generation (RAG) tasks. By leveraging **LangGraph**, it coordinates specialized agents—Supervisor, Researcher, and Writer—to perform deep research and generate comprehensive specific responses. The system features a high-performance **FastAPI** backend and a modern, responsive **React** frontend.

## 🚀 Features

- **Multi-Agent Orchestration**: Centralized `Supervisor` node that routes tasks to specialized `Researcher` and `Writer` agents.
- **Retrieval-Augmented Generation (RAG)**: Ingests PDF documents using **PyPDF** and **ChromaDB** to provide context-aware answers.
- **Vector Search**: Uses semantic embeddings to retrieve relevant information from uploaded documents.
- **Interactive Chat Interface**: A polished, dark-mode UI built with **React** and **TailwindCSS** for real-time interaction.
- **Live Agent Visualization**: Watch the AI agents work in real-time with the agent state visualizer.
- **Modern Tech Stack**:
  - **Backend**: Python, FastAPI, LangChain, LangGraph
  - **Frontend**: React, Vite, TypeScript, Framer Motion

## 📚 Documentation

- **[Architecture Diagram](architecture/architecture.html)** - Visual overview of the system architecture
- **[Beginner's Guide](docs/beginner-guide.html)** - Comprehensive guide for installation, running locally, and deployment

## 🛠️ Tech Stack

### Backend

- **Python 3.10+**
- **FastAPI**: High-performance web framework for APIs.
- **LangGraph**: For building stateful, multi-agent applications.
- **LangChain**: Framework for LLM application development.
- **ChromaDB**: Vector store for embedding and retrieval.
- **Ollama**: Local LLM support.

### Frontend

- **React 19**: Library for building user interfaces.
- **Vite**: Next-generation frontend tooling.
- **TailwindCSS**: Utility-first CSS framework for styling.
- **Lucide React**: Beautiful & consistent icons.
- **Framer Motion**: For smooth animations.

## 📁 Project Structure

```
Nexus-AI-Agent/
├── README.md
├── backend/
│   ├── main.py              # FastAPI server & API endpoints
│   ├── requirements.txt     # Python dependencies
│   ├── graph/
│   │   ├── graph.py         # LangGraph workflow definition
│   │   ├── nodes.py         # Agent node implementations
│   │   └── state.py         # Agent state definition
│   ├── services/
│   │   └── vector_store.py  # ChromaDB & document processing
│   └── chroma_db/           # Vector database storage
├── frontend/
│   ├── package.json         # Node.js dependencies
│   ├── vite.config.ts       # Vite configuration
│   └── src/
│       ├── App.tsx          # Main application component
│       └── components/
│           ├── ChatInterface.tsx    # Chat UI
│           ├── DocumentUpload.tsx   # File upload UI
│           └── AgentVisualizer.tsx  # Agent status display
├── architecture/
│   └── architecture.html    # System architecture diagram
└── docs/
    └── beginner-guide.html  # Beginner's documentation
```

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or higher
- Node.js & npm
- Git
- [Ollama](https://ollama.com/) (running locally for LLM support)

### 1. Clone the Repository

```bash
git clone <repository_url>
cd Nexus-AI-Agent
```

### 2. Set Up Ollama

First, pull the Llama 3 model and start the Ollama server:

```bash
# Pull the Llama 3 model
ollama pull llama3

# Start Ollama server (keep this running)
ollama serve
```

### 3. Backend Setup

Navigate to the backend directory and set up the Python environment.

```bash
cd backend

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Configuration**:
Create a `.env` file in the `backend` directory if required by document loaders or specific LLM providers (e.g., `OPENAI_API_KEY` if switching from Ollama).

**Run the Backend**:

```bash
# Start the FastAPI server
uvicorn main:app --reload
```

The backend will run at `http://localhost:8000`.

### 4. Frontend Setup

Open a new terminal, navigate to the frontend directory, and install dependencies.

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will usually run at `http://localhost:5173`.

## 📖 Usage

1.  **Start Ollama**: Ensure your local Ollama instance is running (e.g., `ollama serve`).
2.  **Launch Apps**: Start both backend and frontend servers as described above.
3.  **Chat**: Open the frontend URL in your browser (`http://localhost:5173`).
4.  **Upload Documents**: Use the "Knowledge Base" tab to upload PDFs for the RAG system to reference.
5.  **Interact**: Ask questions in the "Mission Control" tab. The Supervisor agent will delegate tasks to the Researcher (fetching info) or Writer (drafting responses) as needed.

## 🚀 Quick Start

```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Start Backend
cd backend
.venv\Scripts\activate  # or source .venv/bin/activate
uvicorn main:app --reload

# Terminal 3: Start Frontend
cd frontend
npm run dev

# Open http://localhost:5173 in your browser
```

## 🔧 Troubleshooting

### "Failed to fetch" error

- Make sure the backend server is running on port 8000
- Check for any error messages in the backend terminal

### Ollama connection error

- Ensure Ollama is installed and running: `ollama serve`
- Pull the Llama 3 model: `ollama pull llama3`

### Python module not found

- Activate the virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### Port already in use

- Close other applications using the port
- Or use a different port: `uvicorn main:app --port 8001`

## 🌐 Deployment

For deployment options and detailed instructions, see the **[Beginner's Guide](docs/beginner-guide.html)**.

### Quick Deployment Options:

- **Local Network**: Use `--host 0.0.0.0` flag for backend and `--host` for frontend
- **Cloud Platforms**: Railway, Render, AWS, Google Cloud, DigitalOcean
- **Docker**: Create Dockerfiles for containerized deployment

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## ✍️ Author

**Arun Hari Kamble**  
Technical Manager | Full Stack (React.js + Python) | AI & Emerging Tech Enthusiast

---

<div align="center">
  <p>Built with ❤️ using React, FastAPI, LangGraph, and Ollama</p>
  <p>⭐ Star this repo if you find it useful!</p>
</div>
