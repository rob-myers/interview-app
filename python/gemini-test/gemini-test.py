# pip3 install google-genai
#
# cd python/gemini-test
# python3 gemini-test.py

import os

from google import genai

gemini_api_key = os.popen('cat ~/.gemini_api_key').read()
os.environ['GEMINI_API_KEY'] = gemini_api_key

client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents='Explain how AI works in a few words, please'
)

print(response.text)