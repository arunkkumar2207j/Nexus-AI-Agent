# Nexus AI Agent

Nexus AI Agent is a sophisticated multi-agent orchestration platform designed to handle complex workflows and retrieval-augmented generation (RAG) tasks. By leveraging **LangGraph**, it coordinates specialized agents—Supervisor, Researcher, and Writer—to perform deep research and generate comprehensive specific responses. The system features a high-performance **FastAPI** backend and a modern, responsive **React** frontend.

## 🚀 Features

*   **Multi-Agent Orchestration**: centralized `Supervisor` node that routes tasks to specialized `Researcher` and `Writer` agents.
*   **Retrieval-Augmented Generation (RAG)**: Ingests PDF documents using **PyPDF** and **ChromaDB** to provide context-aware answers.
*   **Vector Search**: Uses semantic embeddings to retrieve relevant information from uploaded documents.
*   **Interactive Chat Interface**: A polished, dark-mode UI built with **React** and **TailwindCSS** for real-time interaction.
*   **Modern Tech Stack**:
    *   **Backend**: Python, FastAPI, LangChain, LangGraph
    *   **Frontend**: React, Vite, TypeScript, Framer Motion

## 🛠️ Tech Stack

### Backend
*   **Python 3.10+**
*   **FastAPI**: High-performance web framework for APIs.
*   **LangGraph**: For building stateful, multi-agent applications.
*   **LangChain**: Framework for LLM application development.
*   **ChromaDB**: Vector store for embedding and retrieval.
*   **Ollama**: Local LLM support.

### Frontend
*   **React 19**: Library for building user interfaces.
*   **Vite**: Next-generation frontend tooling.
*   **TailwindCSS**: Utility-first CSS framework for styling.
*   **Lucide React**: Beautiful & consistent icons.
*   **Framer Motion**: For smooth animations.

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.10 or higher
*   Node.js & npm
*   Git
*   [Ollama](https://ollama.com/) (running locally for LLM support)

### 1. Clone the Repository
```bash
git clone <repository_url>
cd google-antigravity
```

### 2. Backend Setup
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

### 3. Frontend Setup
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
3.  **Chat**: Open the frontend URL in your browser.
4.  **Upload Documents**: Use the upload feature to ingest PDFs for the RAG system to reference.
5.  **Interact**: Ask questions. The Supervisor agent will delegate tasks to the Researcher (fetching info) or Writer (drafting responses) as needed.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
