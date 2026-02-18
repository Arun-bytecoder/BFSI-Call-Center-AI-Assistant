import re

class ComplianceLayer:

    def validate(self, query, response):

        forbidden = [
            "hack",
            "bypass",
            "fake document",
            "generate loan approval"
        ]

        for word in forbidden:
            if word in query.lower():
                return "I'm unable to assist with that request."

        # Block fabricated promotional rates
        if re.search(r"\b\d{1,2}\.\d+%|\b\d{1,2}%\b", response):
            return "Exact interest rates are provided only during official loan evaluation."

        # Block random dollar examples
        if re.search(r"\$\d+", response):
            return "Specific numerical financial calculations cannot be provided.\nEMI values depend on sanctioned interest rate and loan agreement terms.\nPlease refer to official documentation or consult a financial advisor."

        return response
