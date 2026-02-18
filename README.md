# BFSI Call Center AI Assistant 🚀

An enterprise-grade multi-layer AI assistant for BFSI domain with:
- Deterministic financial safety
- FAISS dataset matching
- RAG-based contextual generation
- Compliance validation
- FastAPI backend
- Enterprise dashboard UI


## Tech Stack

- FastAPI
- FAISS
- Ollama (Phi model)
- Python
- HTML/CSS/JS

## Run Locally

1. Create virtual environment
2. Install dependencies

pip install -r requirements.txt


3. Start API


uvicorn main_api:app --reload


4. Open frontend via Live Server


🏗️ BFSI AI Assistant – Architecture Diagram

flowchart TD

    A[User Query] --> B[FastAPI Backend]

    B --> C{Deterministic Layer}
    C -->|EMI / Interest| D[Predefined Financial Response]

    C -->|No Match| E[Dataset Similarity Engine<br>FAISS]

    E -->|High Similarity| F[Dataset Response]

    E -->|No Match| G[Query Classifier]

    G -->|Simple Query| H[LLM Engine (Phi via Ollama)]

    G -->|Complex / Eligibility| I[RAG Engine]

    I --> J[Context Retrieval (Vector Index)]
    J --> H

    H --> K[Compliance Guard]

    K --> L[Final Safe Response]

    L --> M[Frontend Dashboard]

🔎 What This Diagram Represents

Your system is a multi-layer safe AI architecture.

Instead of directly calling LLM, it uses:

1️⃣ Deterministic control
2️⃣ Dataset retrieval
3️⃣ Intelligent classification
4️⃣ RAG for knowledge grounding
5️⃣ Compliance validation

