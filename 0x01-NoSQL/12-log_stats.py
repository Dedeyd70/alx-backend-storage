#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

# Count total number of documents in the collection
total_logs = collection.count_documents({})
print(f'{total_logs} logs where {total_logs} is the number of documents in this collection')

# Count number of documents for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print('Methods:')
for method in methods:
    count = collection.count_documents({"method": method})
    print(f'\t{count} logs with method={method}')

# Count number of documents with specific method and path
specific_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f'{specific_count} logs with method=GET and path=/status')
