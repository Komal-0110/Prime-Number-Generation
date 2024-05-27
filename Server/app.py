from flask_cors import CORS, cross_origin
from flask_restful import Api
from flask import Flask, request, jsonify, make_response
from dotenv import load_dotenv, find_dotenv
from Authentication import SignUp, SignIn, SignOut
from PrimeGenerator import AllModelsRun, GetAllAlgorithm

load_dotenv(find_dotenv())

app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": "http://localhost:5173",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(SignOut, '/signout')
api.add_resource(GetAllAlgorithm, '/GetAllAlgorithm')

@app.before_request
def check_authentication():
    if request.path == '/primegen' and request.method == 'POST':
        auth_cookie = request.cookies.get('Authorization')
        print('auth_cookie : ', auth_cookie)
        if not auth_cookie:
            return make_response(jsonify({'error': 'Please log in first.'}), 401)

@app.route('/primegen', methods=['OPTIONS', 'POST'])
def handle_primegen():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Credentials", "true")
        return response

    # Handle POST request
    return AllModelsRun().post()

api.add_resource(AllModelsRun, '/primegen')


if __name__ == '__main__':
    app.run(port=5000)
