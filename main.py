from openai import OpenAI
# api_key = "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"
# client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)