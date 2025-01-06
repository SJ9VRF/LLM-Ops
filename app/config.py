import os

def get_api_key():
    return os.getenv("OPENAI_API_KEY", "your-default-api-key")
