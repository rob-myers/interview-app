## Getting started with requests

```py
# pip3 install requests
import requests

r = requests.get('https://api.github.com')
help(r)
```

## Gemini API test

```sh
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key: $( cat ~/.gemini_api_key )" \
  -X POST \
  -d '{"contents": [{ "parts": [{ "text": "Explain how AI works in a few words" }]}]}'
```

## Create, activate, and deactivate a python virtual environment

### VSCode Approach

Command `> Python: Create env` then `Venv` will create env `.venv` in root

Then starting a new terminal with start inside the virtual env.

```sh
# show current deps
pip3 list

pip3 install google-genai
pip3 list
```



### Manual approach

```sh
cd ~/coding/interview-app/python

python3 -m venv .venv/smt-tutorial
source .venv/smt-tutorial/bin/activate

# later
deactivate
```