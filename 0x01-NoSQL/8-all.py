#!/usr/bin/env python3
""" list all docs in python """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all docs in a collection """
    all_docs = []
    docs = mongo_collection.find()
    if mongo_collection.count_documents(filter={}) == 0:
        return all_docs
    for doc in docs:
        all_docs.append(doc)
    return all_docs
