#!/usr/bin/env python3
"""This file contains the update_topics function"""


def update_topics(mongo_collection, name, topics):
    """This function updates the mongo_collection"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
