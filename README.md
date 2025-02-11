# Vitalik AI Agent - MVP

This is a Minimum Viable Product (MVP) for a Vitalik Buterin AI agent that can generate content and answer questions based on a knowledge graph.

## Architecture Diagram

[![](https://mermaid.ink/img/pako:eNqVkk1vwjAMhv-KlfPQ7j1MCnSrGGIg2m3SWg5pY0pGmkT5gCHKf1_opG1H8Mm27Ef-eE-k0RxJQlrLzBaKtFJwhdGStqj8Gkajhz5HxR0UB0QPeag_sfE9jEt4xxqoMevrkOOBtUJvBe7RwUQrj1-RNClnSh8k8hYhG6Z8zhcvN1EzVGiZj9QVOqOVwx7S8k14JsVuRrP7Fc2uBKYD8NVFFl1Oe3gsFwYVnUK2LG6aqbCs2TmYXxZuXA9P5aJ2aPesFlL4I8w1DxJvQqbCGcmO_7ekl35yRzq0HRM8Pvp0yVTEb7HDiiTR5bhhQfqKVOocS1nwOj-qhiTeBrwjVod2S5INky5GwfB4yFSwKJjuN2uY-tD6L0YuvLbzH2kNCjt_AyZapJg?type=png)](https://mermaid.live/edit#pako:eNqVkk1vwjAMhv-KlfPQ7j1MCnSrGGIg2m3SWg5pY0pGmkT5gCHKf1_opG1H8Mm27Ef-eE-k0RxJQlrLzBaKtFJwhdGStqj8Gkajhz5HxR0UB0QPeag_sfE9jEt4xxqoMevrkOOBtUJvBe7RwUQrj1-RNClnSh8k8hYhG6Z8zhcvN1EzVGiZj9QVOqOVwx7S8k14JsVuRrP7Fc2uBKYD8NVFFl1Oe3gsFwYVnUK2LG6aqbCs2TmYXxZuXA9P5aJ2aPesFlL4I8w1DxJvQqbCGcmO_7ekl35yRzq0HRM8Pvp0yVTEb7HDiiTR5bhhQfqKVOocS1nwOj-qhiTeBrwjVod2S5INky5GwfB4yFSwKJjuN2uY-tD6L0YuvLbzH2kNCjt_AyZapJg)

## Structure

*   `data/`: Contains mock raw and cleaned data (e.g., similar to datasets from Kaggle or OpenAI's datasets).
*   `knowledge_graph/`: Contains a mock knowledge graph (e.g., similar to Neo4j or Wikidata).
*   `models/`: Placeholder for a trained model (currently empty, but could be replaced with OpenAI's GPT or Hugging Face models).
*   `rag/`: Implements Knowledge Graph Augmented Generation (KAG) and vector search systems (e.g., similar to LangChain, LlamaIndex, FAISS, Pinecone, or Weaviate).
*   `web_app/`: Contains the Flask web application (e.g., similar to a FastAPI or Django-based service).
*   `observability/`: Implements basic metrics tracking (e.g., similar to Prometheus or OpenTelemetry).
*   `vitalik_ai.py`: Generates tweets using OpenAI.
*   `main.py`: The main application file.
*   `requirements.txt`: Lists the Python dependencies.
*   `.env`: Stores sensitive information (API keys). **Do not commit this file!**
*   `.gitignore`: Specifies files to ignore in Git.

## Setup

1.  Create a virtual environment: `python3 -m venv venv`
2.  Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
3.  Install dependencies: `pip install -r requirements.txt`
4.  Set the OpenAI API key in the `.env` file.
5.  Run the application: `flask --app web_app/app.py --debug run --host=0.0.0.0 --port=8080`

## Endpoints

*   `/`: Main page for querying the AI.
*   `/metrics`: Returns the query count (accessible from main.py if needed, but primarily for the web app).

**Important:** This is a mocked system and should not be used in production.
