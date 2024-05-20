import datetime
from config.config import databaseconn

client = databaseconn.connection()
db = client["Midaas_Task"]
collection = db["execution"]

class ExecutionModel:
    def __init__(self, email, start_range, end_range, time_elapsed, algorithm_chosen, num_primes_returned):
        self.timestamp = datetime.datetime.now()
        self.email = email
        self.start_range = start_range
        self.end_range = end_range
        self.time_elapsed = time_elapsed
        self.algorithm_chosen = algorithm_chosen
        self.num_primes_returned = num_primes_returned  

    def save_to_db(self):
        result = collection.insert_one({
            "timestamp": self.timestamp,
            "email": self.email,
            "start_range": self.start_range,
            "end_range": self.end_range,
            "time_elapsed": self.time_elapsed,
            "algorithm_chosen": self.algorithm_chosen,
            "num_primes_returned": self.num_primes_returned
        })
        inserted_id = result.inserted_id
        inserted_document = collection.find_one({"_id": inserted_id})
        return inserted_document["_id"]
    
