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
        

