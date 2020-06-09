import jwt
import base64
import os
import hashlib
from flask import Flask, render_template, make_response, request, redirect

app = Flask(__name__)
FLAG = "<secret>"
PASSWORD = "<secret>"
with open("privatekey.pem", "r") as f:
	PRIVATE_KEY = f.read()
with open("publickey.pem", "r") as f:
	PUBLIC_KEY = f.read()

@app.route('/', methods=['GET'])
def home():
		
	resp = make_response(
		render_template("index.html")
	)
	return resp


@app.route('/login', methods=['GET', 'POST'])
def index():
	errors = ""
	todo = False
	if request.method == "POST":
		resp = make_response(redirect("/login"))
		if request.form["action"] == "Login":
			if request.form["username"] == "whiterose" and request.form["password"] == PASSWORD:
				auth = jwt.encode({"auth": "whiterose"}, PRIVATE_KEY, algorithm="RS256")
				todo = True
			else:
				if request.form["username"] == "cisco" and request.form["password"] == "cisco123":
					auth = jwt.encode({"auth": "cisco"}, PRIVATE_KEY, algorithm="RS256")
					todo = True
				else:
					errors = "Incorrect credentials"
			if todo:
				resp.set_cookie("auth", auth)
		else:
			resp.delete_cookie("auth")
		
		return resp
	else:
		auth = request.cookies.get("auth")
		if auth is None:
			logged_in = False
			admin = False
		else:
			logged_in = True
			admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "whiterose"

		if logged_in:
			resp = make_response(redirect("/operation"))
			# resp = make_response(
			# 	render_template("postlogin.html", logged_in=logged_in, admin=admin, flag=FLAG, errors=errors)
			# )
		else:
			resp = make_response(
				render_template("login.html", logged_in=logged_in, admin=admin, flag=FLAG, errors=errors)
			)
	return resp

@app.route('/operation', methods=['GET'])
def operation():
	errors = ""
	todo = False
	auth = request.cookies.get("auth")
	if auth is None:
		logged_in = False
		admin = False
	else:
		logged_in = True
		admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "whiterose"

	if logged_in:
		resp = make_response(
			render_template("postlogin.html", logged_in=logged_in, admin=admin, flag=FLAG, errors=errors)
		)
	else:

		resp = make_response(redirect("/login"))
		# resp = make_response(
		# 	render_template("login.html", logged_in=logged_in, admin=admin, flag=FLAG, errors=errors)
		# )
	return resp

@app.route("/publickey.pem")
def public_key():
	with open("./publickey.pem", "r") as f:
		resp = make_response(f.read())
		resp.mimetype = 'text/plain'
		return resp

@app.route("/da_highprofiledata/elliota")
def elliot():
	errors = ""
	todo = False
	auth = request.cookies.get("auth")
	if auth is None:
		logged_in = False
		admin = False
	else:
		logged_in = True
		admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "whiterose"

	if logged_in:
		resp = make_response(
			render_template("elliot.html", logged_in=logged_in, admin=admin, flag=FLAG, errors=errors)
		)
	else:

		resp = make_response(redirect("/login"))
		# resp = make_response(
		# 	render_template("login.html", logged_in=logged_in, admin=admin, flag=FLAG, errors=errors)
		# )
	return resp

@app.route("/logout")
def logout():
	resp = make_response(redirect("/login"))
	resp.delete_cookie('auth')

	return resp

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)