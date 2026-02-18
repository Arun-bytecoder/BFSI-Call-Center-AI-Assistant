import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from config.settings import KNOWLEDGE_PATH


class RAGEngine:

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings()
        self.vectorstore = self.build_vectorstore()

    def build_vectorstore(self):

        documents = []

        for file in os.listdir(KNOWLEDGE_PATH):
            with open(os.path.join(KNOWLEDGE_PATH, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

        return FAISS.from_texts(documents, self.embeddings)

    def retrieve(self, query):
        docs = self.vectorstore.similarity_search(query, k=1)
        return "\n".join([doc.page_content[:600] for doc in docs])
