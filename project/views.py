import uuid
from flask import Flask, jsonify, request
from datetime import date
from project import app

users = {}
categories = {}
records = {}


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users.keys():
        return jsonify(users[user_id]), 200
    else:
        return jsonify({}), 400


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users.keys():
        user = users[user_id]
        del users[user_id]
        return jsonify(user), 200
    else:
        return jsonify({}), 400


@app.route("/user", methods=["POST"])
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, **user_data}
    users[user_id] = user
    return jsonify(user), 200


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200


@app.route("/category", methods=["GET"])
def get_category():
    category_id = request.args.get("id")
    if category_id in categories.keys():
        return categories[category_id], 200
    else:
        return jsonify({}), 400


@app.route("/category", methods=["POST"])
def create_category():
    new_category_name = request.args.get("name")
    new_category_id = uuid.uuid4().hex
    new_category = {
        "name": new_category_name,
        "id": new_category_id
    }
    categories[new_category_id] = new_category
    return jsonify(new_category), 200


@app.route("/category", methods=["DELETE"])
def delete_category():
    category_id = request.args.get("id")
    if category_id in categories.keys():
        category = categories[category_id]
        del categories[category_id]
        return jsonify(category), 200
    else:
        return jsonify({}), 400


@app.route("/record/<int:record_id>", methods=["GET"])
def get_record(record_id):
    if record_id in records.keys():
        return records[record_id], 200
    else:
        return jsonify({}), 400


@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    if record_id in records.keys():
        record = records[record_id]
        del records[record_id]
        return jsonify(record), 200
    else:
        return jsonify({}), 400


@app.route("/record", methods=["POST"])
def create_record():
    new_record_id = uuid.uuid4().hex
    new_record = {
        "id": new_record_id,
        "user_id": request.args.get("user_id"),
        "category_id": request.args.get("category_id"),
        "creation_date": date.today(),
        "sum": request.args.get("sum")
    }
    records[new_record_id] = new_record
    return jsonify(new_record), 200


@app.route("/record", methods=["GET"])
def get_filtered_records():
    category_id = request.args.get('category_id')
    user_id = request.args.get('user_id')
    result = []
    if not category_id and not user_id:
        return jsonify({"Error": "Enter at least one argument: category_id or user_id"}), 400
    if not user_id:
        for record in records.values():
            if record["category_id"] == category_id:
                result.append(record)
    elif not category_id:
        for record in records.values():
            if record["user_id"] == user_id:
                result.append(record)
    else:
        for record in records.values():
            if record["user_id"] == user_id and record["category_id"] == category_id:
                result.append(record)
    return jsonify(result), 200


@app.route("/")
def homepage():
    response = "<h1>Hello World!</h1>"
    return response, 200


@app.route("/healthcheck")
def healthCheck():
    response = {
        'time': str(date.today()),
        'status': 200,
    }
    return jsonify(response), 200