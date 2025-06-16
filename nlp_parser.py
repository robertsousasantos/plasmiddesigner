"""Utilities to parse user requests using Gemini models or fall back to simple heuristics."""

from __future__ import annotations

import json
import os
import re
from typing import Dict

try:
    import google.generativeai as genai
except ImportError:  # pragma: no cover - if lib not installed
    genai = None

_MODEL_NAME = os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash")


def _call_gemini(prompt: str) -> Dict[str, str] | None:
    """Call the Gemini API if credentials are available."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or genai is None:
        return None
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(_MODEL_NAME)
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception:
        # In constrained environments the request will likely fail
        return None


def parse_user_request(text: str) -> Dict[str, str]:
    """Parse a free-form user request into structured requirements."""
    prompt = (
        "Extract the organism (ecoli, yeast, bacillus) and target protein from the"\
        " following request. Respond with JSON including keys 'organism' and"\
        " 'protein'.\nRequest: "
        f"{text}"
    )
    result = _call_gemini(prompt)
    if result:
        return result

    # Fallback heuristic parsing
    text_low = text.lower()
    if "e. coli" in text_low or "ecoli" in text_low:
        organism = "ecoli"
    elif "saccharomyces" in text_low or "yeast" in text_low:
        organism = "yeast"
    elif "bacillus" in text_low:
        organism = "bacillus"
    else:
        organism = "ecoli"

    # crude extraction of protein name
    match = re.search(r"express(?:ao)?\s+(?:da|de)?\s*([\w\-]+)", text_low)
    protein = match.group(1) if match else "proteinX"

    return {"organism": organism, "protein": protein}
