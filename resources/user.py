import sqlite3
from flask_restful import Resource,reqparse
from flask import request
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True,help="username field is required")
    parser.add_argument("password",type=str,required=True,help="password field is required")


    def post(self):
        #data = request.get_json()
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"user with that username already exist"},400

        # user = UserModel(data["username"],data["password"])
        user = UserModel(**data)  #unpacking key value pairs kwargs
        user.save_to_db()
        return {"message":"registered succesfully"},201
