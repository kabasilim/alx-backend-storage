#!/usr/bin/env python3
"""This file contains the list_all function"""


def list_all(mongo_collection):
    """This function lists all documents in the collection"""
    allDocs = []

    for doc in mongo_collection.find():
        allDocs.append(doc)

    return allDocs
