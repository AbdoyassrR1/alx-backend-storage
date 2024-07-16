#!/usr/bin/env python3
""" insert a new document """


def insert_school(mongo_collection, **kwargs):
    """ insert a new document """
    return mongo_collection.insert_one(kwargs).inserted_id
