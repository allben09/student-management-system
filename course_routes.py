from flask import Blueprint, request, jsonify
from app.models import Course, Enrollment
from app.database import db
from app.auth import admin_required, teacher_or_admin_required, any_user_required

course_bp = Blueprint('courses', __name__)

@course_bp.route('/', methods=['GET'])
@any_user_required()
def get_courses():
    courses = Course.query.filter_by(is_active=True).all()
    return jsonify([c.to_dict() for c in courses]), 200

@course_bp.route('/', methods=['POST'])
@admin_required()
def create_course():
    data = request.get_json()
    
    if not data.get('course_id') or not data.get('name'):
        return jsonify({"msg": "course_id and name are required"}), 400
    
    if Course.query.filter_by(course_id=data['course_id']).first():
        return jsonify({"msg": "Course ID already exists"}), 409
    
    course = Course(
        course_id=data['course_id'],
        name=data['name'],
        instructor=data.get('instructor', ''),
        credits=data.get('credits', 3),
        max_students=data.get('max_students', 30)
    )
    
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201

@course_bp.route('/<int:id>', methods=['GET'])
@any_user_required()
def get_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"msg": "Course not found"}), 404
    return jsonify(course.to_dict()), 200

@course_bp.route('/<int:id>', methods=['PUT'])
@admin_required()
def update_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"msg": "Course not found"}), 404
    
    data = request.get_json()
    for field in ['name', 'instructor', 'credits', 'max_students']:
        if field in data:
            setattr(course, field, data[field])
    
    db.session.commit()
    return jsonify(course.to_dict()), 200

@course_bp.route('/<int:id>', methods=['DELETE'])
@admin_required()
def delete_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"msg": "Course not found"}), 404
    
    course.is_active = False
    db.session.commit()
    return jsonify({"msg": "Course deleted successfully"}), 200
