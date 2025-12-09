import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection

# Load variables from .env
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME", "fraudshield_ai")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set. Please add it to your .env file.")

# Create MongoDB client and database
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]


def get_transactions_collection() -> Collection:
    """
    Returns the 'transactions' collection.
    We will store all transaction + model prediction here.
    """
    return db["transactions"]
