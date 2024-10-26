#!/usr/bin/env python3
""" Function to insert a new document in a MongoDB collection """

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the specified collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The fields and values to insert into the document.

    Returns:
        The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
