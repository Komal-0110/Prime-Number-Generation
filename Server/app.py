from flask_cors import CORS
from flask_restful import Api
from flask import Flask, request, jsonify, make_response
from dotenv import load_dotenv, find_dotenv
from Authentication import SignUp, SignIn, SignOut
from PrimeGenerator import AllModelsRun
import os

load_dotenv(find_dotenv())

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(SignOut, '/signout')

@app.before_request
def check_authentication():
    if request.path == '/primegen':
        auth_cookie = request.cookies.get('Authorization')
        if not auth_cookie:
            return make_response(jsonify({'error': 'Please log in first.'}), 401)
        
api.add_resource(AllModelsRun, '/primegen')

if __name__ == '__main__':
    app.run(port=5000)