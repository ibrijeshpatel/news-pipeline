import hashlib
from datetime import datetime

def generate_id(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()

def parse_datetime(date_str: str) -> datetime:
    # Try ISO format first
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        # Fallback: PhocusWire uses "Jul 17, 2025"
        return datetime.strptime(date_str, "%b %d, %Y")
