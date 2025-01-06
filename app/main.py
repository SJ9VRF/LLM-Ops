from .config import get_api_key
from .phoenix_client import setup_phoenix
from .tracing import start_tracing

def main():
    api_key = get_api_key()
    setup_phoenix(api_key)
    start_tracing()

if __name__ == "__main__":
    main()

