# VisaMate AI – Multi-Agent Visa Navigation & Compliance Assistant

A cautious AI prototype that routes visa questions through a structured answer workflow, validates outputs with Pydantic, and uses deterministic fallbacks when the model is unavailable or a destination has no verified source pack.

## MVP capabilities
- Streamlit chat interface
- Destination and visa-category selection
- OpenAI GPT-4o-mini through LangChain
- Pydantic structured response validation
- Deterministic fallback when API credentials are missing or a destination is not configured
- Conservative compliance prompt and human-review warning
- Official US government source links

## Important scope limitation
This starter version is a safe MVP scaffold, **not a complete live visa research system**. It does not crawl official websites or verify that linked pages are current. The US links are references for users to consult, not evidence that a rule has been checked. Other countries intentionally return a fallback until their official source packs and retrieval pipeline are added.

## Setup

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API key
Copy `.env.example` to `.env` and add your OpenAI API key:
```env
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
```
Never commit `.env` or share your API key.

### 4. Run
```bash
streamlit run app.py
```

## GitHub deployment

Create an empty repository named `VisaMate-AI` on GitHub, then run from this folder:
```bash
git init
git add .
git commit -m "Initial VisaMate AI MVP"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/VisaMate-AI.git
git push -u origin main
```

## Deploy on Streamlit Community Cloud
1. Push this repository to GitHub.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Select the repository and `app.py` as the main file.
4. In app settings → Secrets, add:
```toml
OPENAI_API_KEY = "your_key"
OPENAI_MODEL = "gpt-4o-mini"
```
5. Deploy.

## Next engineering milestones
1. Add official-source retrieval (fetch/index only permitted government pages; record URL and retrieval timestamp).
2. Add specialist tools for research, eligibility, documents, and compliance.
3. Add citation-to-claim checks and tests for unsupported claims.
4. Add country-specific source packs and automated freshness checks.
5. Add evaluation tests for prompt injection, stale sources, missing evidence, and API failures.

## Safety
Visa and immigration rules can change and depend on individual circumstances. This tool is for general information navigation, not legal advice or a guarantee of eligibility or visa approval.
