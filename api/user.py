from flask import Blueprint, request, jsonify
# from db import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://blurface962:MGRN50j3Giad6GaN@cluster.yh4tljd.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

class Database:
    def __init__(self) :
        self.db = client["blurfacedatabase"]
        self._users = self.db["users"]
        self._images = self.db["files"]
        

user_service = Blueprint("user_service", __name__)
database = Database()

# MongoDB collection for user data
users_collection = database._users

@user_service.route("/register", methods=["POST"])
def register():
    data = request.json

    # Extract user registration data from the request
    email = data.get("email")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    phone_number = data.get("phoneNumber")
    gender = data.get("gender")
    password = data.get("password")

    # Check if the email already exists
    if users_collection.find_one({"email": email}):
        return jsonify({"message": "Email already registered"}), 400

    # Create a new user document
    new_user = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "gender": gender,
        "password": password,
    }

    # Insert the user data into the database
    users_collection.insert_one(new_user)

    return jsonify({"message": "Registration successful"}), 201


@user_service.route("/login", methods=["POST"])
def login():
    data = request.json

    # Extract user login data from the request
    email = data.get("email")
    password = data.get("password")

    # Find the user by email
    user = users_collection.find_one({"email": email})

    if user is None:
        return jsonify({"message": "User not found"}), 404

    # Check the password
    if user["password"] != password:
        return jsonify({"message": "Invalid password"}), 401

    # You can also generate a token here and return it for authentication

    return jsonify({"message": "Login successful"}), 200
