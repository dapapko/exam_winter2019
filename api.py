from flask import Flask, escape, request, jsonify
from trip import Trip

app = Flask(__name__)


@app.route('/calculate', methods=[ 'POST'])
def calculate():
    data = request.get_json()
    try:
        if len(data["points"]) < 2 or len(data["points"]) > 5 or data["carType"] not in ["econom", "economPlus", "business",  "premium"] or type(data["baby"]) != bool or type(data["animal"]) != bool:
            return jsonify({"error": "Validation error"}), 500
    except KeyError:
        return jsonify({"error": "Validation error"}), 500
    trip = Trip(data['points'], data['carType'], data['baby'], data['animal'])
    trip.get_overall_length_of_route()
    trip.calculate_price()
    if trip.price == 0:
        return  jsonify({"error": "Request error"}), 500
    else:
        return jsonify({"price": trip.price}), 200
