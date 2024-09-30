from flask import Blueprint, jsonify

job_routes = Blueprint('jobs', __name__)

@job_routes.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = [
        {"id": 1, "title": "Software Developer", "company": "TechCorp", "description": "Developing applications"},
        {"id": 2, "title": "Data Analyst", "company": "DataCorp", "description": "Analyzing data"}
    ]
    return jsonify(jobs)
