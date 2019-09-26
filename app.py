#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/reg", methods=["GET", "POST"])
def reg_handle():
    if request.method == ("GET"):
        return render_template("reg.html")
    elif request.method == ("POST"):
        uname = request.form.get("uname")
        upass = request.form.get("upass")
        upass2 = request.form.get("upass2")
        phone = request.form.get("phone")
        verify_code = request.form.get("verify_code")
        email = request.form.get("email")


@app.route("/login", methods=["GET", "POST"])
def login_handle():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        uname = request.form.get("uname")
        upass = request.form.get("upass")
        


        

if __name__ == '__main__':
    app.run(port=80, debug=True)