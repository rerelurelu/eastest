from pydantic import BaseModel


class Text(BaseModel):
    label: str
    generated_text: str
