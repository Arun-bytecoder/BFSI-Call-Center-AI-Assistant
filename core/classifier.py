class QueryClassifier:

    def classify(self, query):

        complex_keywords = [
            "calculate",
            "breakdown",
            "formula",
            "amortization",
            "emi calculation",
            "interest computation",
            "how is emi calculated"
        ]


        for word in complex_keywords:
            if word in query.lower():
                return "complex"
            if "emi" in query.lower() and "formula" in query.lower():
                return "emi_formula"

        return "simple"
