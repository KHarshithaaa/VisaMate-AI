from schemas.response import VisaAnswer
from tools.official_sources import US_SOURCES

def safe_fallback(country: str, category: str) -> VisaAnswer:
    if country != "United States":
        return VisaAnswer(
            answer=(
                f"I don't yet have a verified official-source knowledge pack for {country}. "
                "To avoid giving you incorrect immigration guidance, I can't confirm requirements. "
                "Please use that country's official immigration or embassy website. Add its verified "
                "government sources to tools/official_sources.py before enabling detailed answers."
            ),
            sources=[],
            needs_human_review=True,
            confidence="low",
            fallback_used=True,
        )
    return VisaAnswer(
        answer=(
            f"I can help you navigate general {category.lower()}-visa information for the United States, "
            "but I cannot verify current eligibility or guarantee an outcome from the starter knowledge pack. "
            "Start with the official links below, check the latest instructions for your visa class and location, "
            "and confirm case-specific questions with the embassy/consulate or a qualified immigration professional. "
            "If you share your specific question, I can help organize what to verify."
        ),
        sources=US_SOURCES,
        needs_human_review=True,
        confidence="low",
        fallback_used=True,
    )
