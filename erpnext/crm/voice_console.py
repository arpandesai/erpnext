"""Voice Console integration using openai-realtime-console.

This module wraps the `openai-realtime-console` package so you can operate CRM
features using voice commands. The console listens for voice input and forwards
recognized text as commands to ERPNext.
"""
from __future__ import annotations

try:
    from openai_realtime_console import start_console
except ImportError:  # pragma: no cover - optional dependency
    start_console = None


def start_voice_console() -> None:
    """Launch the voice console if available."""
    if start_console is None:
        raise ImportError(
            "openai-realtime-console is not installed."
            " Install it via `pip install openai-realtime-console`."
        )
    start_console()
