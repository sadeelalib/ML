from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Generate text
generated_text = generator("The future of AI is", max_length=50, num_return_sequences=1)
print("Generated Text:", generated_text[0]['generated_text'])
