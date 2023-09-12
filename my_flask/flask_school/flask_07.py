""" Описать модель группы(id, fullname). Создать сайт. Создать напрямую в базе 3 группы.
Описать шаблон и вью для получения и отображения списка всех групп.
Создать шаблон и вью для создания группы. Добавить ссылку для перехода на создание группы на странице отображения всех групп.
"""

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__, template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flaskschool.db"
db = SQLAlchemy(app)


class MyBase(db.Model):
    __abstract__ = True

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Group(MyBase):
    id = db.Column("id", db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))


class Student(MyBase):
    id = db.Column("id", db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    group_id = db.Column(db.Integer, ForeignKey(Group.id), nullable=True)
    group = relationship("Group", foreign_keys="Student.group_id", backref="students")


@app.route("/")
def read():
    groups = Group.query.all()
    return render_template("07.html", groups=groups)


@app.route("/read_students")
def read_students():
    students = Student.query.all()
    return render_template("07_st.html", students=students)


@app.route("/add_groups", methods=["POST", "GET"])
def add_groups():
    if request.method == "GET":
        return render_template("07_add.html")
    else:
        group = Group(fullname=request.form["fullname"])
        group.save()
        return redirect(url_for("read"))


@app.route("/add_student", methods=["POST", "GET"])
def add_student():
    if request.method == "GET":
        return render_template("07_add_st.html")
    else:
        student = Student(firstname=request.form["firstname"], group_id=request.form["group_id"])
        student.save()
        return redirect(url_for("read_students"))


@app.route("/update_group", methods=["POST", "GET"])
def update_group():
    if request.method == "GET":
        return render_template("07_update.html", id=request.args.get("id"))
    else:
        group = db.session.query(Group). \
            filter_by(id=request.args.get("id")).first()
        group.fullname = request.form["fullname"]
        group.update()
        return redirect(url_for("read"))


@app.route("/update_student", methods=["POST", "GET"])
def update_student():
    if request.method == "GET":
        return render_template("07_update_st.html", id=request.args.get("id"))
    else:
        student_id = request.args.get("id")
        student = db.session.query(Student).filter_by(id=student_id).first()
        student.firstname = request.form["firstname"]
        student.group_id = request.form["group_id"]
        student.update()
        return redirect(url_for("read_students"))


@app.route("/delete_group", methods=["GET"])
def delete_group():
    group = Group.query.get(request.args.get("id"))
    group.delete()
    return redirect(url_for("read"))


@app.route("/delete_st", methods=["GET"])
def delete_st():
    student = Student.query.get(request.args.get("id"))
    student.delete()
    return redirect(url_for("read_students"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
