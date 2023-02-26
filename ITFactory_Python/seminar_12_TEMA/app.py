from flask import Flask, request, abort, jsonify
from cars_repository import CarRepository
import exceptions

app = Flask(__name__)
repo = CarRepository("cars.json")

@app.route("/car", methods=["POST"])
def add_car():
	car = request.json
	try:
		repo.add_car(car)
		return "OK", 201
	except exceptions.InvalidCarException as ex:
		abort(400, ex)

@app.route("/cars", methods=["GET"])
def show_all():
	try:
		cars = repo.get_all()
		return jsonify(cars)
	except exceptions.InvalidCarException as ex:
		abort(404, ex)

@app.route("/car/<licence_plate>", methods=["GET"])
def show_by_plate(licence_plate):
	try:
		car = repo.find_by_plate(licence_plate)
		return car
	except exceptions.InvalidCarException as ex:
		abort(404, ex)

@app.route("/car/<licence_plate>", methods=["DELETE"])
def delete_by_plate(licence_plate):

	try:
		repo.delete_by_plate(licence_plate)
		return "", 204
	except exceptions.InvalidCarException as ex:
		abort(404, ex)

@app.route("/car/<licence_plate>", methods=["PUT"])
def replace_by_plate(licence_plate):
	car = request.json
	try:
		repo.replace_by_plate(car, licence_plate)
		return "", 204
	except exceptions.InvalidCarException as ex:
		abort(404, ex)


if __name__ == '__main__':
	app.run(debug=True)