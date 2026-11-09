from pydantic import BaseModel, Field
from typing import List

class Source(BaseModel):
    title: str
    url: str

class VisaAnswer(BaseModel):
    answer: str = Field(min_length=1)
    sources: List[Source] = Field(default_factory=list)
    needs_human_review: bool = True
    confidence: str = "low"
    fallback_used: bool = False
