import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def current_date():
    c_date = datetime.datetime.now()
    return str(c_date)


if __name__ == "__main__":
    app.run()
