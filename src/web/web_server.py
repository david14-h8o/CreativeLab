from flask import Flask, render_template, request
from src.core.query_handler import handle_query

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = handle_query(user_input)
    return render_template("index_html", response=response)

if __name__ = "__main__":
    app.run(debug=True)
