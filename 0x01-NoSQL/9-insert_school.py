#!/usr/bin/env python3
"""This file contains the insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """This function inserts a new document in a collection based on kwargs"""

    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
