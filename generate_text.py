from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

promt = "AI will change the world because"

result = generator(promt , max_length = 30, num_return_sequences=2)

print(result)
