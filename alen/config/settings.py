import os
from pathlib import Path
from dotenv import load_dotenv

CONFIG_PATH = Path.home() / ".alen_env"

# Load global config if exists
if CONFIG_PATH.exists():
    load_dotenv(dotenv_path=CONFIG_PATH)

# Load local config overrides
load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    POLICY_MODE = os.getenv("POLICY_MODE", "strict")
    ALLOWED_SCOPES = os.getenv("ALLOWED_SCOPES", "127.0.0.1,localhost").split(",")

    @classmethod
    def save_api_key(cls, api_key: str):
        with open(CONFIG_PATH, "a") as f:
            f.write(f"\nGEMINI_API_KEY={api_key}\n")
        cls.GEMINI_API_KEY = api_key

settings = Settings()
