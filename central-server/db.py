from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["logdb"]
logs_collection = db["logs"]

def create_indexes():
    logs_collection.create_index("timestamp")
    logs_collection.create_index("level")
    logs_collection.create_index("service")
    logs_collection.create_index("source")
    logs_collection.create_index([("service", 1), ("timestamp", -1)])