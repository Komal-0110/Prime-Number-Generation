from config.config import databaseconn

client = databaseconn.connection()
db = client["Midaas_Task"]
collection = db["user"]

class UserModel:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        
    def json(self) -> dict:
        return {'username': self.username, 'email': self.email, 'password': self.password}
    
    @classmethod
    def find_by_email(cls, email: str):
        myquery = {'email': email}
        user_exists = collection.find_one(myquery)
        return user_exists
            
        
    def save_to_db(self):
        result = collection.insert_one({
            "username" : self.username,
            "email" : self.email,
            "password" : self.password
        })
        inserted_id = result.inserted_id
        inserted_document = collection.find_one({"_id": inserted_id})

        return inserted_document["_id"]
            
   