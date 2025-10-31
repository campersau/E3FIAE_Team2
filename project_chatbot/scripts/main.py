# Test
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
)

@app.route("/")
def home():
    return render_template("index.html", title="YourChatbot")

if __name__ == "__main__":
    # 5050 ist sicher auf deinem Mac (5000 ist oft belegt)
    app.run(debug=True, port=5050)
