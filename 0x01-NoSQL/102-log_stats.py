#!/usr/bin/env python3
"""This file provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    count = nginx_collection.count_documents({})
    get_count = nginx_collection.count_documents({'method': 'GET'})
    post_count = nginx_collection.count_documents(
        {'method': 'POST'})
    put_count = nginx_collection.count_documents(
        {'method': 'PUT'})
    patch_count = nginx_collection.count_documents(
        {'method': 'PATCH'})
    delete_count = nginx_collection.count_documents(
        {'method': 'DELETE'})
    status_check = nginx_collection.count_documents({"path": "/status"})
    ip_list = []
    agg = nginx_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {"$limit": 10}
    ])
    for i in agg:
        ip_list.append(i)
    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_check} status check")
    print("IPs:")
    for i in ip_list:
        print(f"\t{i.get('_id')}: {i.get('count')}")
