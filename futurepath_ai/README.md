# FuturePath AI — Prototype

A working prototype of the FuturePath AI concept: a chat-based career mentor
for Sri Lankan youth that maps interests to career paths, gives a learning
roadmap with free/low-cost resources, and generates a downloadable CV.

## Stack (and why)

- **Backend:** Python + Flask — minimal, one process, no build step.
- **Frontend:** Plain HTML/CSS/JS — no framework/bundler needed, opens
  instantly, easy for you to keep editing by hand.
- **"AI" matching engine:** transparent keyword-overlap scoring
  (`matcher.py`), not a hosted LLM — so the prototype runs completely
  offline with zero API cost or key setup. It's a placeholder for the real
  NLP-based Skill Mapper described in the proposal; see "Extend first"
  below for the swap-in point.
- **CV generation:** `python-docx`, producing a real `.docx` file the user
  can open in Word/Google Docs and keep editing.

## Project structure

```
futurepath_ai/
  app.py              Flask routes
  careers_data.py      Career knowledge base (edit this to add careers)
  matcher.py            Keyword-matching "Skill Mapper"
  cv_generator.py      Builds the .docx CV
  templates/index.html  Single-page UI (chat + CV builder tabs)
  static/style.css
  static/app.js
  requirements.txt
```

## How to run it

1. Make sure you have Python 3.9+ installed.
2. Open a terminal in the `futurepath_ai` folder.
3. Create a virtual environment (recommended) and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open **http://127.0.0.1:5000** in your browser.

That's it — no database, no API keys, no build step.

## Using it

- **Mentor Chat tab:** answer the three questions the mentor asks. It
  scores your free-text answers against a keyword-tagged career database
  and shows your top 3 matches. Click a match to see a roadmap: core
  skills to build + free/affordable courses to start with.
- **CV Builder tab:** fill in your details (repeatable blocks for
  education, experience, projects), watch the live preview update, then
  click **Generate CV** to download a formatted `.docx`.

## What I'd extend first

1. **Swap the keyword matcher for a real LLM call.** `matcher.py` is
   written so this is a contained change: replace `score_answer()`'s
   internals with a call to the Claude API (a prompt template is already
   sketched at the bottom of that file) so the mentor can have a genuinely
   free-form conversation, not just three fixed questions, and can explain
   *why* it picked a career in natural language.
2. **Persist users and conversations.** Right now everything lives in the
   Flask session (lost on server restart, no history across devices).
   Swap in SQLite (zero-config) or Postgres, add a simple login (email or
   phone OTP), and let users revisit past matches and CVs.
3. **Real labor-market data ("Localized Labor Market Oracle").** The
   career database is hand-curated. The next real step is a scheduled job
   that pulls current listings from local job portals and adjusts each
   career's "demand" signal — that's what turns this from a static
   quiz into the "Oracle" described in the proposal.
4. **Sinhala/Tamil support.** The architecture (a single `score_answer`
   function, a single chat-message list) is language-agnostic; the
   fastest path is machine-translating user input to English before
   scoring, then translating the mentor's replies back — before investing
   in native-language models.
5. **Interview Simulator module.** Same LLM integration point as #1: a
   new `/api/interview` endpoint that takes a target career, asks
   role-relevant questions one at a time, and scores the answers the same
   way a real interviewer would — reuse the chat UI already built here.
6. **PDF export for the CV**, in addition to `.docx`, using a tool like
   LibreOffice headless conversion (`soffice --headless --convert-to pdf`)
   on the generated file, for users who just want to share a CV without
   opening Word.

## Notes on the data

Career descriptions, skills, and resource links in `careers_data.py` are a
starting set focused on sectors mentioned in the proposal (tech, green
energy, healthcare, tourism, etc.) — treat it as a seed list to expand,
not a complete one. No salary figures are included, since accurate,
current numbers need a real data source (the "Oracle" module above)
rather than being hard-coded.
