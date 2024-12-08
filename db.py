from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    return client["restaurant_db"]

db = get_database()
orders_collection = db["orders"]
menu_collection = db["menu"]
reviews_collection = db["reviews"]
