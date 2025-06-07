from flask import render_template, request,redirect,url_for
from app import app

@app.run("/")
def form():
    return render_template("form.html")

@app.run("/submit")
def submit():
    if request.method =="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return render_template("result.html",name=name,email=email)
    else:
        return redirect(url_for("form"))