# Loom Presentation Script - Vitalik AI Agent

## 1. Introduction (0:00 - 0:30)
- Welcome to the presentation of the **Vitalik AI Agent MVP**.
- This is a **Minimum Viable Product** designed to generate content and answer questions using a **knowledge graph**.
- In this video, I will walk you through the **architecture, functionality, and setup** of the project.

## 2. Architecture Overview (0:30 - 1:30)
- The system is built using **Flask** as the web framework.
- It integrates a **Knowledge Graph** to provide context-aware responses.
- The **RAG (Retrieval-Augmented Generation) module** enhances responses using vector search systems like **FAISS, Pinecone, or Weaviate**.
- Observability is implemented using **Prometheus or OpenTelemetry**.

## 3. Project Structure (1:30 - 2:30)
- `data/`: Stores raw and cleaned datasets (similar to **Kaggle/OpenAI datasets**).
- `knowledge_graph/`: Contains structured knowledge (similar to **Neo4j/Wikidata**).
- `models/`: Placeholder for AI models (e.g., **OpenAI GPT, Hugging Face models**).
- `rag/`: Implements **Knowledge Graph Augmented Generation (KAG)** and **vector search**.
- `web_app/`: The **Flask-based web application**.
- `observability/`: Tracks system metrics.

## 4. Setup Instructions (2:30 - 3:30)
- Clone the repository and navigate to the project directory.
- Create a virtual environment and install dependencies:
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```
- Set up the `.env` file with the **OpenAI API key**.
- Run the application:
  ```bash
  python web_app/app.py
  ```

## 5. Demo (3:30 - 4:30)
- Open the web interface and enter a **tweet subject**.
- The system generates a **context-aware tweet**.
- Click on **"View Context"** to see the knowledge graph data used.

## 6. Conclusion (4:30 - 5:00)
- This MVP demonstrates how **AI and knowledge graphs** can work together.
- Future improvements include **real-time data integration and enhanced observability**.
- Thank you for watching!
