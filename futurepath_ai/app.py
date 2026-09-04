"""
FuturePath AI - prototype backend.

Run with:  python app.py
Then open: http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, jsonify, session, send_file

from careers_data import get_career
from matcher import score_answer, top_matches
from cv_generator import generate_cv

app = Flask(__name__)
app.secret_key = "dev-only-change-me"  # fine for local prototype use

QUESTIONS = [
    "Hi! I'm your FuturePath AI mentor 👋 Let's find a career direction that "
    "actually fits you. First: what subjects, hobbies, or activities make you "
    "lose track of time?",
    "Nice. Now — how do you prefer to work: alone or in a team, hands-on or "
    "planning/thinking, following steps or coming up with new ideas?",
    "Last one: which of these pulls you in most — technology, helping "
    "people, building/fixing things, working with numbers, or creativity? "
    "Feel free to mention more than one.",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat/start", methods=["POST"])
def chat_start():
    session["scores"] = {}
    session["step"] = 0
    return jsonify({"reply": QUESTIONS[0], "step": 0, "done": False})


@app.route("/api/chat", methods=["POST"])
def chat():
    body = request.get_json(force=True) or {}
    message = body.get("message", "")

    scores = session.get("scores", {})
    step = session.get("step", 0)

    scores = score_answer(message, scores)
    session["scores"] = scores
    step += 1
    session["step"] = step

    if step < len(QUESTIONS):
        return jsonify({"reply": QUESTIONS[step], "step": step, "done": False})

    matches = top_matches(scores, n=3)
    if not matches:
        return jsonify({
            "reply": (
                "Thanks! I didn't catch enough detail to make a confident "
                "match yet — tell me a bit more about what you enjoy, in "
                "your own words."
            ),
            "step": step,
            "done": False,
        })

    reply = "Based on what you've told me, here are your top matches:"
    return jsonify({
        "reply": reply,
        "step": step,
        "done": True,
        "matches": [
            {
                "id": c["id"],
                "title": c["title"],
                "sector": c["sector"],
                "description": c["description"],
            }
            for c in matches
        ],
    })


@app.route("/api/roadmap/<career_id>")
def roadmap(career_id):
    career = get_career(career_id)
    if not career:
        return jsonify({"error": "not found"}), 404
    return jsonify(career)


@app.route("/api/cv/generate", methods=["POST"])
def cv_generate():
    data = request.get_json(force=True) or {}
    buf = generate_cv(data)
    filename = f"{(data.get('full_name') or 'FuturePath').strip().replace(' ', '_')}_CV.docx"
    return send_file(
        buf,
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


if __name__ == "__main__":
    app.run(debug=True)
