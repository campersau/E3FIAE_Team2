from flask import Blueprint, render_template, session, redirect, url_for, request, flash

# Der Blueprint MUSS "main" heißen, damit 'main.login' funktioniert
main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html", title="Chatbot", username=session.get("username"))

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if username and password:
            session["username"] = username
            flash("Erfolgreich angemeldet.", "success")
            return redirect(url_for("main.home"))
        flash("Bitte Benutzername und Passwort eingeben.", "error")
    return render_template("login.html", title="Login")

@main.route("/logout")
def logout():
    session.clear()
    flash("Erfolgreich abgemeldet.", "info")
    return redirect(url_for("main.home"))

# Diagnose-Route
@main.route("/ping")
def ping():
    return "pong"
