import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

class databaseconn():
    def connection():
        load_dotenv(find_dotenv())

        password = os.environ.get("MONGODB_PWD")
        connection_string = f"mongodb+srv://komalvaswani0110:{password}@cluster0.p2monpp.mongodb.net/?retryWrites=true&w=majority"

        client = MongoClient(connection_string)
        return client
