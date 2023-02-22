from flask import Flask, request, abort, jsonify
from user_repository import UserRepository
import exceptions

app = Flask(__name__)

repo = UserRepository("users.csv")

@app.route("/user", methods=["POST"])
def add_user():
	user = request.json
	try:
		repo.add_user(user)
		return "OK", 201
	except exceptions.InvalidUserException as ex:
		abort(400, ex)

@app.route("/user/<name>", methods=["GET"])
def get_user(name):
	try:
		user = repo.find_by_name(name)
		return jsonify(user)
	except exceptions.UserNotFoundException as ex:
		abort(404, ex)

@app.route("/user/<name>", methods=["DELETE"])
def delete_user(name):
	try:
		repo.delete_by_name(name)
		return "", 204
	except exceptions.UserNotFoundException as ex:
		abort(404, ex)

@app.route("/user/<name>", methods=["PATCH"])
def update_user(name):
	user = request.json
	try:
		repo.update_name(name, user)
		return "", 201
	except exceptions.UserNotFoundException as ex:
		abort(404, ex)


if __name__ == '__main__':
    app.run(debug=True)