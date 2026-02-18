from core.similarity_engine import SimilarityEngine
from core.classifier import QueryClassifier
from core.rag_engine import RAGEngine
from core.compliance import ComplianceLayer
from core.financial_rules import EMI_FORMULA_RESPONSE, INTEREST_EXPLANATION_RESPONSE
from core.llm_engine import LocalLLM



class BFSIAssistant:

    def __init__(self):
        self.similarity = SimilarityEngine()
        self.classifier = QueryClassifier()
        self.llm = LocalLLM()
        self.rag = RAGEngine()
        self.guard = ComplianceLayer()

    def handle_query(self, query):

        query_lower = query.lower()

        # =====================================================
        # 1️⃣ Deterministic Financial Safety Layer
        # =====================================================

        if "emi" in query_lower and "formula" in query_lower:
            return {
                "response": EMI_FORMULA_RESPONSE,
                "routing": "DETERMINISTIC_EMI"
            }

        if "reducing balance" in query_lower or "interest calculation" in query_lower:
            return {
                "response": INTEREST_EXPLANATION_RESPONSE,
                "routing": "DETERMINISTIC_INTEREST"
            }

        # =====================================================
        # 2️⃣ Forced RAG for Critical Financial Topics
        # =====================================================

        if "eligibility" in query_lower:
            context = self.rag.retrieve(query)

            rag_prompt = f"""
Provide a clear and professional explanation using ONLY the context below.

Do NOT assume any company identity.
Do NOT invent numerical values.
Do NOT create sample calculations.
Keep response concise and compliant.

Context:
{context}

Customer Question:
{query}

Answer:
"""

            llm_response = self.llm.generate(rag_prompt)
            final = self.guard.validate(query, llm_response)

            return {
                "response": final,
                "routing": "RAG_FORCED_ELIGIBILITY"
            }

        # =====================================================
        # 3️⃣ Dataset Similarity Layer (FAISS)
        # =====================================================

        match, dataset_response = self.similarity.search(query)

        if match:
            final = self.guard.validate(query, dataset_response)
            return {
                "response": final,
                "routing": "DATASET"
            }

        # =====================================================
        # 4️⃣ Classification Layer
        # =====================================================

        query_type = self.classifier.classify(query)

        # =====================================================
        # 5️⃣ LLM or RAG Routing
        # =====================================================

        if query_type == "simple":

            safe_prompt = f"""
Provide a professional financial explanation.

Structure the response:
- Start with a clear definition.
- Use short paragraphs.
- Use bullet points if listing criteria.
- Keep it concise (max 8 sentences).
- Do not use promotional language.

Question:
{query}
"""

            llm_response = self.llm.generate(safe_prompt)
            
            # Clean common model artifacts
            llm_response = llm_response.replace("User Query:", "")
            llm_response = llm_response.replace("Response:", "")
            llm_response = llm_response.replace("Sure,", "")
            llm_response = llm_response.strip()
            
            final = self.guard.validate(query, llm_response)
            return {
                "response": final,
                "routing": "LLM"
            }
        
        else:
            
            context = self.rag.retrieve(query)

            rag_prompt = f"""
            Answer clearly and professionally.

- One short definition.
- List key factors only.
- Maximum 5 sentences.
- No detailed explanations.

Context:
{context}

Question:
{query}
"""

            llm_response = self.llm.generate(rag_prompt)
            final = self.guard.validate(query, llm_response)

            return {
                "response": final,
                "routing": "RAG"
            }
