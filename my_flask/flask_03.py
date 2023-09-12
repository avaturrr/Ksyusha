from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/home")
def home():
    return "home page"


@app.route("/my-word/<string:my_word>")
def count_letter(my_word):
    if len(my_word) % 2 == 0:
        return my_word[::2]
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
