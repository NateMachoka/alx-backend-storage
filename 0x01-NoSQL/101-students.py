#!/usr/bin/env python3
""" Function to get top students sorted by average score """

from pymongo import MongoClient


def top_students(mongo_collection):
    # Retrieve all students from the collection
    students = mongo_collection.find()

    results = []

    for student in students:
        # Calculate the average score
        if 'topics' in student:
            scores = [topic['score'] for topic in student['topics']]
            average_score = sum(scores) / len(scores) if scores else 0
        else:
            average_score = 0

        # Prepare the result with the average score included
        student_info = {
            '_id': student['_id'],
            'name': student['name'],
            'averageScore': average_score
        }
        results.append(student_info)

    # Sort the results by average score in descending order
    results.sort(key=lambda x: x['averageScore'], reverse=True)

    return results
