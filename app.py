
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for classroom demonstration
CORS(app)

# Fictional sample course data
courses = [
    {
        "id": 1,
        "code": "IT101",
        "name": "Introduction to Information Technology",
        "description": "An introduction to information technology concepts."
    },
    {
        "id": 2,
        "code": "PROG102",
        "name": "Programming Fundamentals",
        "description": "Basic programming concepts and problem solving."
    },
    {
        "id": 3,
        "code": "DBMS103",
        "name": "Database Management Systems",
        "description": "An introduction to databases and SQL."
    },
    {
        "id": 4,
        "code": "NET104",
        "name": "Computer Networking",
        "description": "Learn about computer networks and communication."
    },
    {
        "id": 5,
        "code": "WEB105",
        "name": "Web Development",
        "description": "Learn the basics of creating websites."
    }
]


# Endpoint 1: Health Check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "Student Course API is running"
    }), 200


# Endpoint 2: Get All Courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify({
        "status": "success",
        "count": len(courses),
        "data": courses
    }), 200


# Endpoint 3: Get One Course
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify({
                "status": "success",
                "data": course
            }), 200

    return jsonify({
        "status": "error",
        "message": f"Course with ID {course_id} was not found."
    }), 404


# Run the application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
