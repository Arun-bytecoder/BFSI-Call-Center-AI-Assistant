import ollama

class LocalLLM:
    def __init__(self):
        self.model_name = "phi3:mini"

    def generate(self, prompt):

        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a BFSI financial assistant. "
                            "Provide clear, concise, professional responses. "
                            "Do not generate fictional numbers unless requested. "
                            "Avoid promotional language. "
                            "Keep answer under 150 words."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                options={
                    "temperature": 0.3,
                    "num_predict": 150
                }
            )

            return response["message"]["content"]

        except Exception as e:
            print("LLM Error:", str(e))
            return "I’m unable to process your request at the moment. Please try again."
