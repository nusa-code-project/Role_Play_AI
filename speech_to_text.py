import base64
import requests
from openai import OpenAI

api_key = "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"

client = OpenAI(api_key=api_key)

url =  "https://cdn.openai.com/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content
encoded_string  = base64.b64encode(wav_data).decode('utf-8')

