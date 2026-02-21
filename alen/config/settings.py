import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    POLICY_MODE = os.getenv("POLICY_MODE", "strict")
    ALLOWED_SCOPES = os.getenv("ALLOWED_SCOPES", "127.0.0.1,localhost").split(",")

settings = Settings()
