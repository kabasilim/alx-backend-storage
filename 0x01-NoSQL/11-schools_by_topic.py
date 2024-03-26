#!/usr/bin/env python3
"""This file contains the schools_by_topic function"""


def schools_by_topic(mongo_collection, topic):
    """This function returns the list of schools having a specific topic"""
    schools = []
    for school in mongo_collection.find({'topics': {"$regex": topic}}):
        schools.append(school)
    return schools
