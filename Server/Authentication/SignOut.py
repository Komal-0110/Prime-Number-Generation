from flask_restful import Resource
from flask import jsonify, make_response


class SignOut(Resource):
    def post(self):
        respone = make_response(jsonify({"message": "Logged out successfully" }), 200)
        respone.set_cookie('Authorization', '', expires=0, httponly=True, secure=True)
        return respone