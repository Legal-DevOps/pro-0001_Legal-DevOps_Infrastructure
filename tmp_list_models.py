import os
from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")
models = client.models.list()
for model in models.data:
    if "vision" in model.id.lower():
        print(model.id)
