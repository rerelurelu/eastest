def generate_text(text: str, digits: int) -> str:
    return (text * (digits // len(text) + 1))[:digits]
