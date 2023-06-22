""" Описать модель группы(id, fullname). Создать сайт. Создать напрямую в базе 3 группы.
Описать шаблон и вью для получения и отображения списка всех групп.
Создать шаблон и вью для создания группы. Добавить ссылку для перехода на создание группы на странице отображения всех групп.
"""

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="/home/user/PycharmProjects/Ksyusha/my_flask/flask_school/templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flaskschool.db"
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))


@app.route("/")
def read():
    groups = Group.query.all()
    return render_template("07.html", groups=groups)


@app.route("/add_groups", methods=["POST", "GET"])
def add_group():
    if request.method == "GET":
        return render_template("07_add.html")
    else:
        group = Group(fullname=request.form["fullname"])
        db.session.add(group)
        db.session.commit()
        return redirect(url_for("read"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
