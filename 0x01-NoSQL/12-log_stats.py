#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stat():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient("localhost", 27017)
    logs = client.logs
    nginx = logs.nginx

    logs_count = nginx.count_documents({})
    get_method = nginx.count_documents({"method": "GET"})
    post_method = nginx.count_documents({"method": "POST"})
    put_method = nginx.count_documents({"method": "PUT"})
    patch_method = nginx.count_documents({"method": "PATCH"})
    delete_method = nginx.count_documents({"method": "DELETE"})
    status = nginx.count_documents({"path": "/status"})
    print(f"{logs_count} logs\n\
Methods:\n\tmethod GET: {get_method}\n\
\tmethod POST: {post_method}\n\tmethod PUT: {put_method}\n\
\tmethod PATCH: {patch_method}\n\tmethod DELETE: {delete_method}\n\
{status} status check")
