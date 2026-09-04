"""
FuturePath AI - Psychometric Skill Mapper (prototype version).

The real proposal calls for an NLP model that chats freely with the student.
For a working prototype with zero external API keys/cost, this module uses
transparent keyword-overlap scoring instead: every free-text answer is
matched against each career's keyword list. It's simple, fast, explainable
to a judge/user, and has one clear upgrade path (see bottom of file).
"""

import re
from collections import defaultdict

from careers_data import CAREERS

_WORD_RE = re.compile(r"[a-zA-Z]+")


def _tokenize(text: str):
    return set(w.lower() for w in _WORD_RE.findall(text))


def score_answer(text: str, running_scores: dict) -> dict:
    """
    Score one free-text answer against every career and add the result
    into running_scores (career_id -> float score). Returns running_scores.
    """
    tokens = _tokenize(text)
    if not tokens:
        return running_scores

    for career in CAREERS:
        career_id = career["id"]
        hits = 0
        for kw in career["keywords"]:
            kw_tokens = _tokenize(kw)
            # count a hit if every word of a multi-word keyword phrase
            # appears in the answer, or a single-word keyword appears
            if kw_tokens and kw_tokens.issubset(tokens):
                hits += 1
            elif kw.lower() in text.lower():
                hits += 1
        if hits:
            running_scores[career_id] = running_scores.get(career_id, 0) + hits

    return running_scores


def top_matches(running_scores: dict, n: int = 3):
    """Return the top-n careers as full dicts, sorted by score desc."""
    if not running_scores:
        return []
    ranked = sorted(running_scores.items(), key=lambda kv: kv[1], reverse=True)
    ranked = [cid for cid, score in ranked if score > 0][:n]
    by_id = {c["id"]: c for c in CAREERS}
    return [by_id[cid] for cid in ranked if cid in by_id]


# ---------------------------------------------------------------------------
# UPGRADE PATH: swap this file's internals for a real LLM call and keep the
# same score_answer()/top_matches() interface, e.g.:
#
#   response = anthropic_client.messages.create(
#       model="claude-sonnet-4-6",
#       max_tokens=500,
#       messages=[{"role": "user", "content": f"""
#           A Sri Lankan student said: "{text}"
#           Given this list of careers: {[c['title'] for c in CAREERS]}
#           Return the 3 best-fit career ids as JSON, with a one-sentence
#           reason for each, considering interests, subjects and work style.
#       """}]
#   )
#
# This keeps everything else in app.py unchanged.
# ---------------------------------------------------------------------------
