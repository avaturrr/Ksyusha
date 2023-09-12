from flask import Flask

app = Flask(__name__)


@app.route("/two_pow/<int:number>")
def number_squared(number):
    sq_number = number ** 2
    return str(sq_number)


if __name__ == "__main__":
    app.run()
