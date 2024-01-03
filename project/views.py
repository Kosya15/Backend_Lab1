from flask import Flask, jsonify, request
from datetime import date
from project import app, db
from project.models import UserModel, RecordModel, CategoryModel
from project.schemas import UserSchema, RecordSchema, CategorySchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError


with app.app_context():
    db.create_all()
    db.create_all()
    db.session.commit()


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    return {
            "id": user.id, 
            "name": user.name
            }


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {
            "message": f"User {user_id} successfully deleted!"
            }


@app.route("/user", methods=["POST"])
def create_user():
    user_data = request.get_json()
    valid = UserSchema()
    try:
        valid.load(user_data)
    except ValidationError as error:
        return jsonify({'error': error.messages}), 400
    user = UserModel(name=user_data["name"])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return "Error! Entered data is incorrect.", 400
    user_info = {"id": user.id, "name": user.name}
    return jsonify(user_info), 200


@app.route("/users", methods=["GET"])
def get_users():
    return list({"id": user.id, "name": user.name} for user in UserModel.query.all())


@app.route("/category", methods=["GET"])
def get_category():
    category_id = request.args.get("id")
    category = CategoryModel.query.get_or_404(category_id)
    return {"id": category.id, "name": category.name}


@app.route("/category", methods=["POST"])
def create_category():
    category_data = request.args
    valid = CategorySchema()
    try:
        valid.load(category_data)
    except ValidationError as error:
        return jsonify({'error': error.messages}), 400
    category = CategoryModel(name=category_data["name"])
    try:
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        return "Error! Entered data is incorrect.", 400
    
    return jsonify({"id": category.id, "name": category.name}), 200


@app.route("/category", methods=["DELETE"])
def delete_category():
    category_id = request.args.get("id")
    category = CategoryModel.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return {"message": f"Category {category_id} successfully deleted!"}


@app.route("/record/<int:record_id>", methods=["GET"])
def get_record(record_id):
    record = RecordModel.query.get_or_404(record_id)
    response = {
        "id": record.id,
        "user_id": record.user_id,
        "category_id": record.category_id,
        "creation_date": record.creation_date,
        "sum": record.sum
    }
    return response, 200


@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    record = RecordModel.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return {"message": f"Record {record_id} successfully deleted!"}


@app.route("/record", methods=["POST"])
def create_record():
    record_data = request.args
    valid = RecordSchema()
    try:
        valid.load(record_data)
    except ValidationError as error:
        return jsonify({'error': error.messages}), 400
    record = RecordModel(sum=record_data["sum"], user_id=record_data["user_id"], category_id=record_data["category_id"])
    try:
        db.session.add(record)
        db.session.commit()
    except IntegrityError:
        return "Error! Entered data is incorrect.", 400
    response = {
        "id": record.id,
        "user_id": record.user_id,
        "category_id": record.category_id,
        "creation_date": record.creation_date,
        "sum": record.sum
    }
    return response, 200


@app.route("/record", methods=["GET"])
def get_filtered_records():
    ctg_Id = request.args.get('category_id')
    us_Id = request.args.get('user_id')
    records = []
    if not ctg_Id and not us_Id:
        return "Enter at least one argument: category_id or user_id", 400
    if not us_Id:
        records = RecordModel.query.filter_by(category_id=ctg_Id)
    if not ctg_Id:
        records = RecordModel.query.filter_by(user_id=us_Id)
    if ctg_Id and us_Id:
        records = RecordModel.query.filter_by(category_id=ctg_Id, user_id=us_Id)
    return list({"id": record.id, "user_id": record.user_id, "category_id": record.category_id, "creation_date": record.creation_date, "sum": record.sum} for record in records), 200




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