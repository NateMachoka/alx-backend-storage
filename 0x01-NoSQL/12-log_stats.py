#!/usr/bin/env python3
""" Nginx logs statistics """

from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})

    # Count of methods
    methods_count = {
        "GET": collection.count_documents({"method": "GET"}),
        "POST": collection.count_documents({"method": "POST"}),
        "PUT": collection.count_documents({"method": "PUT"}),
        "PATCH": collection.count_documents({"method": "PATCH"}),
        "DELETE": collection.count_documents({"method": "DELETE"}),
    }

    # Count of GET method for path /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Output results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
