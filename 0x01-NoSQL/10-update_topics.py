#!/usr/bin/env python3
""" Function to update the topics of a school document """


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
