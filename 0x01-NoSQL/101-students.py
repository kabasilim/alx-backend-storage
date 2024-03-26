#!/usr/bin/env python3
"""This file contains the top_students function"""


def top_students(mongo_collection):
    """This returns all students sorted by average score"""
    final_list = []
    agg = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }

    ])

    for i in agg:
        final_list.append(i)

    return final_list
