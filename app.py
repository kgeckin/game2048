# app.py
from flask import Flask, render_template, redirect, url_for, request, session
import logic
import copy  # Derin kopyalama için
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "varsayılan_gizli_anahtar")

# Hücre renkleri sözlüğü
tile_colors = {
    0: "#CDC1B4",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#EDC22E",
}

@app.route("/")
def index():
    if "mat" not in session:
        session["mat"] = logic.start_game()
        session["score"] = 0
        # Eğer 'best' oturumda yoksa, onu sıfırla; yoksa mevcut değeri koru.
        if "best" not in session:
            session["best"] = 0
    mat = session["mat"]
    state = logic.get_current_state(mat)
    score = session.get("score", 0)
    best = session.get("best", 0)
    return render_template("index.html", board=mat, state=state,
                           score=score, best=best, tile_colors=tile_colors)
@app.route("/move", methods=["POST"])
def move():
    direction = request.form.get("direction")
    mat = session.get("mat")
    if not mat:
        mat = logic.start_game()
        session["score"] = 0

    # Hamleden önce mevcut durumu yedekleyelim (undo için)
    session["prev_board"] = copy.deepcopy(mat)
    session["prev_score"] = session.get("score", 0)

    # Yön tuşuna göre hamleyi uygula
    if direction == "w":
        mat, changed, score_inc = logic.move_up(mat)
    elif direction == "s":
        mat, changed, score_inc = logic.move_down(mat)
    elif direction == "a":
        mat, changed, score_inc = logic.move_left(mat)
    elif direction == "d":
        mat, changed, score_inc = logic.move_right(mat)
    else:
        changed = False
        score_inc = 0

    if changed:
        session["score"] = session.get("score", 0) + score_inc
        # En yüksek skoru güncelle
        if session["score"] > session.get("best", 0):
            session["best"] = session["score"]
        logic.add_new_2(mat)
    session["mat"] = mat
    return redirect(url_for("index"))

@app.route("/undo")
def undo():
    # Önceki durumu (board ve score) geri yükle
    if "prev_board" in session and "prev_score" in session:
        session["mat"] = session["prev_board"]
        session["score"] = session["prev_score"]
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    session.pop("mat", None)
    session.pop("score", None)
    # session.pop("best", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
