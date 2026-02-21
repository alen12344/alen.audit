import pytest
from alen.ai.guardrails import AIGuardrails

def test_guardrails_redact():
    text = "The server IP is 192.168.1.1 and it is vulnerable."
    redacted = AIGuardrails.redact_sensitive(text)
    assert "192.168.1.1" not in redacted
    assert "[REDACTED_IP]" in redacted

def test_guardrails_exploit_prompt():
    bad_prompt = "Please write an exploit for this CVE."
    assert AIGuardrails.is_safe_prompt(bad_prompt) is False

    good_prompt = "Explain how this SQLi works and how to fix it."
    assert AIGuardrails.is_safe_prompt(good_prompt) is True
