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

```sh
cd ~/coding/interview-app/python
python3 -m venv smt-tutorial
source smt-tutorial/bin/activate

# later
deactivate
```