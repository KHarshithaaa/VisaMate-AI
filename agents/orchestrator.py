
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from config import GEMINI_API_KEY, MODEL_NAME
from schemas.response import VisaAnswer
from tools.fallback import safe_fallback
from tools.official_sources import US_SOURCES


SYSTEM_PROMPT = """
You are VisaMate AI, a multi-agent visa navigation assistant.

Your responsibilities:
1. Understand the user's visa question.
2. Research relevant visa information using supplied context.
3. Explain eligibility considerations.
4. Help prepare document checklists.
5. Identify compliance risks.

STRICT RULES:
- Never invent visa regulations, fees, deadlines or eligibility.
- Never guarantee visa approval.
- Never pretend that you checked live government websites.
- Use only supplied source information.
- Clearly identify information that requires official verification.
- Do not provide legal advice.
- If evidence is insufficient, say so.
- Always recommend official government sources.
- Be clear, friendly and helpful.
"""


def answer_question(question: str, country: str, visa_type: str) -> VisaAnswer:

    if not GEMINI_API_KEY or country != "United States":
        return safe_fallback(country, visa_type)

    try:
        llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            google_api_key=GEMINI_API_KEY,
            temperature=0
        )

        structured_llm = llm.with_structured_output(VisaAnswer)

        source_context = "\n".join(
            f"- {source.title}: {source.url}"
            for source in US_SOURCES
        )

        prompt = f"""
Destination: {country}
Visa category: {visa_type}

User question:
{question}

Available official source links:
{source_context}

IMPORTANT:
These are source links only. Their live contents have not been retrieved.

Provide general navigation guidance.
Do not invent current immigration requirements.
Include relevant supplied source links.
Set confidence to low.
Set needs_human_review to true.
"""

        result = structured_llm.invoke([
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ])

        if not isinstance(result, VisaAnswer):
            result = VisaAnswer.model_validate(result)

        result.needs_human_review = True
        result.confidence = "low"

        return result

    except Exception as error:
        print("Gemini error:", error)
        return safe_fallback(country, visa_type)
