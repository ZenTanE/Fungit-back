# Fungit
Backend for Fungit app

## How to run
This project uses uv to manage packages and the virtual environment

Install uv:
```
pip install uv
```

Install dependencies:
```
uv sync
```

Save your Gemini API key as an environment variable, otherwise the **app won't work**:
```
$env:GOOGLE_API_KEY="[YOUR API KEY GOES HERE]"
```

Run flask app:
```
python -m flask --app Api.py run --host=0.0.0.0 --port=5000
```
