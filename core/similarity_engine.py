import json
import faiss
import numpy as np
from core.embeddings import EmbeddingModel
from config.settings import DATASET_PATH, STRONG_MATCH_THRESHOLD


class SimilarityEngine:

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.data = self.load_dataset(DATASET_PATH)
        self.index, self.embeddings = self.build_index()

    def load_dataset(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def build_index(self):
        texts = [
            entry["instruction"] + " " + entry["input"]
            for entry in self.data
        ]

        embeddings = np.array(
            [self.embedder.encode(text) for text in texts]
        ).astype("float32")

        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        return index, embeddings

    def search(self, query):

        query_embedding = np.array(
            [self.embedder.encode(query)]
        ).astype("float32")

        distances, indices = self.index.search(query_embedding, 1)

        similarity_score = 1 / (1 + distances[0][0])

        if similarity_score >= STRONG_MATCH_THRESHOLD:
            return True, self.data[indices[0][0]]["output"]

        return False, None
