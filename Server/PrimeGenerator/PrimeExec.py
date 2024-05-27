from flask_restful import Resource
from .PrimeGenerate import PrimeGenerate 
from Model.ExecutionModel import ExecutionModel
from Model.UserModel import UserModel
from flask import request
import time

class AllModelsRun(Resource):

    def post(self):
        
        data = request.get_json()
        email = data.get('email')
        
        start_range = data.get('start_range')
        end_range = data.get('end_range')
        algorithm_choosen = data.get('algorithm_choosen')

        existing_user_by_email = UserModel.find_by_email(email=email)
        if existing_user_by_email:
            # checking that all value should be filled
            if not email or not start_range or not end_range or not algorithm_choosen:
                return {"error": "Please fill all the inputs."}, 400
            # checking validation as start range < end range
            if start_range > end_range:
                return {"error": "Starting value always less than ending value."}, 400
            # checking that algorithm number should be valid
            if algorithm_choosen not in[1,2,3,4,5,6]:
                return {"error": "Please choose valid algorithm number."}, 400
            start_time = time.time()
            primeNumbers = PrimeGenerate.prime_number_generator_by_choosing_algorithm(start_range, end_range, algorithm_choosen)
            end_time = time.time()
            time_elapsed = end_time - start_time
            num_primes_returned = ','.join(map(str, primeNumbers))
            new_data = ExecutionModel(email=email, start_range=start_range, end_range=end_range, time_elapsed=time_elapsed, algorithm_chosen=algorithm_choosen, num_primes_returned=num_primes_returned)

            try:
                data_id = new_data.save_to_db()
                return {"message": "New data saved successfully", "_id": str(data_id), "PrimeNumber" : num_primes_returned}, 201
            except Exception as e:
                print(f"Error: {e}")
                return {"error": "Invalid server error"}, 500
        else:
            return {"message": "User not found"}, 404