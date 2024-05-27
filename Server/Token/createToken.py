from flask import make_response
from jose import jwt 
import os
from dotenv import load_dotenv, find_dotenv
import datetime
load_dotenv(find_dotenv())
def generate_token(user_id):

    secret_key = os.environ.get("SECRET_KEY")
    token = jwt.encode({"userId": user_id}, secret_key, algorithm="HS256", access_token=30 * 24 * 60 * 60)
    return token


def encode_auth_token(user_id):
    
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24, minutes=5, seconds=3600),
            'iat': datetime.datetime.utcnow(),
            'sub': str(user_id)
        }
        return jwt.encode(
            payload,
            os.environ.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return str(e)
