#!/usr/bin/env python3
"""This script provides statistics about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count total logs
    total_logs = nginx_collection.count_documents({})

    # Count logs by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = nginx_collection.count_documents({"method": method})

    # Count status check
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    # Display statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()

