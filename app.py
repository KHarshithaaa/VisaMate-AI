import streamlit as st
from agents.orchestrator import answer_question

st.set_page_config(page_title="VisaMate AI", page_icon="🛂", layout="wide")
st.title("🛂 VisaMate AI")
st.caption("Multi-agent visa navigation and compliance assistant")
st.warning("Visa rules change. This prototype provides general information, not legal advice. Verify every requirement on the linked official government website.")

with st.sidebar:
    st.header("Your visa context")
    country = st.selectbox("Destination country", ["United States", "United Kingdom", "Canada", "Australia", "Germany"])
    visa_type = st.selectbox("Visa category", ["Student", "Work", "Tourist", "Business", "Family / Dependent"])
    st.caption("MVP note: the starter knowledge base contains official US source links only. Other destinations will trigger a safe fallback until you add verified sources.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask about visa steps, eligibility, documents, or compliance...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Routing your question to the right specialist..."):
            result = answer_question(question, country, visa_type)
        st.markdown(result.answer)
        if result.sources:
            st.markdown("**Official sources to verify**")
            for source in result.sources:
                st.markdown(f"- [{source.title}]({source.url})")
        if result.needs_human_review:
            st.info("Please confirm this with the relevant embassy, consulate, or qualified immigration professional.")
    st.session_state.messages.append({"role": "assistant", "content": result.answer})
