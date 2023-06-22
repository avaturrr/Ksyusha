from flask import request, Flask, redirect, render_template

app = Flask(__name__, template_folder="/home/user/PycharmProjects/Ksyusha/my_flask/templates")


@app.route("/name_lastname_age", methods=["POST", "GET"])
def fname_lname_age():
    if request.method == "POST":
        firstname_form = request.form["firstname"]
        lastname_form = request.form["lastname"]
        age_form = request.form["age"]
        wf(firstname_form, lastname_form, age_form)
        return f"{firstname_form}, {lastname_form}, {age_form}"
    else:
        return render_template("flask_05.html")


def wf(name, last_name, age):
    with open("data_form_form.txt", "a") as my_file:
        my_file.writelines([name, last_name, age])




if __name__ == "__main__":
    app.run()
