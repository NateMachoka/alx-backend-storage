#!/usr/bin/env python3
""" Function to find schools by topic """

def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools with the specified topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents with the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
