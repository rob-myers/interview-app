# pip3 install google-genai

import os

from google import genai

gemini_api_key = os.popen('cat ~/.gemini_api_key').read()
os.environ['GEMINI_API_KEY'] = gemini_api_key

client = genai.Client()