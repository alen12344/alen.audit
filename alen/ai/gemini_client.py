import google.generativeai as genai
from alen.config.settings import settings
import logging

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            logger.warning("GEMINI_API_KEY not configured. AI features will fail.")
        genai.configure(api_key=settings.GEMINI_API_KEY)
        # Recommended model for text reasoning
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')

    def analyze(self, system_prompt: str, data: str) -> str:
        prompt = f"{system_prompt}\n\nData to analyze:\n{data}"
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini API Error: {e}")
            return f"Error analyzing data: {str(e)}"
