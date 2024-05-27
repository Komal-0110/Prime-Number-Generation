from Model.UserModel import UserModel
from flask import request
from flask_bcrypt import Bcrypt
from flask_restful import Resource 

bcrypt = Bcrypt()

class SignUp(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        
        if not username or not email or not password:
            return {"error": "Please fill all the inputs."}, 400
        
        if UserModel.find_by_email(email=email):
            return {"error" : "Please fill all the inputs"}, 400
        
        
        hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = UserModel(username=username, email=email, password=hash_password)

        try:
            user_id = new_user.save_to_db()
            return {"message": "User registered successfully", "_id": str(user_id)}, 201
        except Exception as e:
            print(f"Error: {e}")
            return {"error": "Invalid server error"}, 500