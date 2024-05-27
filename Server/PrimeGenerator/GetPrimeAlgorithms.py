from flask import jsonify
from flask_restful import Resource
from config.config import databaseconn

client = databaseconn.connection()
db = client["Midaas_Task"]
collection = db["algorithm"]


class GetAllAlgorithm(Resource):
    def get(self):
        algorithms = list(collection.find({}))
        return jsonify(algorithms)