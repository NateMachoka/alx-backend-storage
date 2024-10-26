#!/usr/bin/env python3
""" Function to list all documents in a MongoDB collection """

def list_all(mongo_collection):
    """Returns a list of all documents in the specified collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of documents or an empty list if no documents are found.
    """
    return list(mongo_collection.find())
