import re

class AIGuardrails:
    """Redaction and output sanitization."""

    @staticmethod
    def redact_sensitive(text: str) -> str:
        # Simple regex for IPs, Emails, Passwords etc.
        # This is a basic demonstration.
        redacted = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[REDACTED_IP]', text)
        return redacted

    @staticmethod
    def is_safe_prompt(prompt: str) -> bool:
        # Check for exploit generation attempts
        blacklist = ['write an exploit', 'generate shellcode', 'bypass wpf']
        for bad_word in blacklist:
            if bad_word in prompt.lower():
                return False
        return True
