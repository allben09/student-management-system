from flask import Blueprint, request, jsonify
from app.models import Student, Course, Enrollment, User
from app.database import db
from app.auth import admin_required, teacher_or_admin_required, any_user_required
from datetime import datetime
import re

student_bp = Blueprint('students', __name__)

def generate_student_id():
    """Generate next student ID in format STU-0001"""
    last_student = Student.query.order_by(Student.id.desc()).first()
    if not last_student:
        return "STU-0001"
    num = int(last_student.student_id.split('-')[1]) + 1
    return f"STU-{num:04d}"

@student_bp.route('/', methods=['GET'])
@any_user_required()
def get_students():
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    
    query = Student.query.filter_by(is_active=True)
    if search:
        query = query.filter(
            db.or_(
                Student.name.ilike(f'%{search}%'),
                Student.email.ilike(f'%{search}%'),
                Student.student_id.ilike(f'%{search}%')
            )
        )
    
    pagination = query.paginate(page=page, per_page=limit, error_out=False)
    return jsonify({
        "data": [s.to_dict() for s in pagination.items],
        "total": pagination.total,
        "page": page,
        "limit": limit,
        "pages": pagination.pages
    }), 200

@student_bp.route('/', methods=['POST'])
@teacher_or_admin_required()
def create_student():
    data = request.get_json()
    
    # Validate required fields
    required = ['name', 'email']
    for field in required:
        if not data.get(field):
            return jsonify({"msg": f"{field} is required"}), 400
    
    # Check if email already exists
    if Student.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Student with this email already exists"}), 409
    
    student = Student(
        student_id=generate_student_id(),
        name=data['name'],
        email=data['email'],
        phone=data.get('phone', ''),
        address=data.get('address', '')
    )
    
    if data.get('date_of_birth'):
        try:
            student.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"msg": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201

@student_bp.route('/<int:id>', methods=['GET'])
@any_user_required()
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"msg": "Student not found"}), 404
    return jsonify(student.to_dict()), 200

@student_bp.route('/<int:id>', methods=['PUT'])
@teacher_or_admin_required()
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"msg": "Student not found"}), 404
    
    data = request.get_json()
    for field in ['name', 'email', 'phone', 'address']:
        if field in data:
            setattr(student, field, data[field])
    
    if 'date_of_birth' in data and data['date_of_birth']:
        try:
            student.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"msg": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    db.session.commit()
    return jsonify(student.to_dict()), 200

@student_bp.route('/<int:id>', methods=['DELETE'])
@admin_required()
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"msg": "Student not found"}), 404
    
    # Soft delete
    student.is_active = False
    db.session.commit()
    return jsonify({"msg": "Student deleted successfully"}), 200

@student_bp.route('/<int:id>/enroll', methods=['POST'])
@teacher_or_admin_required()
def enroll_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"msg": "Student not found"}), 404
    
    data = request.get_json()
    course_id = data.get('course_id')
    
    if not course_id:
        return jsonify({"msg": "course_id is required"}), 400
    
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
        return jsonify({"msg": "Course not found"}), 404
    
    # Check if already enrolled
    existing = Enrollment.query.filter_by(student_id=student.id, course_id=course.id).first()
    if existing:
        return jsonify({"msg": "Student already enrolled in this course"}), 409
    
    # Check capacity
    if course.enrollments.count() >= course.max_students:
        return jsonify({"msg": "Course is full"}), 400
    
    enrollment = Enrollment(student_id=student.id, course_id=course.id)
    db.session.add(enrollment)
    db.session.commit()
    
    return jsonify(enrollment.to_dict()), 201

@student_bp.route('/<int:id>/grade', methods=['POST'])
@teacher_or_admin_required()
def add_grade(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"msg": "Student not found"}), 404
    
    data = request.get_json()
    course_id = data.get('course_id')
    grade = data.get('grade')
    
    if not course_id or grade is None:
        return jsonify({"msg": "course_id and grade are required"}), 400
    
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            return jsonify({"msg": "Grade must be between 0 and 100"}), 400
    except ValueError:
        return jsonify({"msg": "Grade must be a number"}), 400
    
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
        return jsonify({"msg": "Course not found"}), 404
    
    enrollment = Enrollment.query.filter_by(student_id=student.id, course_id=course.id).first()
    if not enrollment:
        return jsonify({"msg": "Student not enrolled in this course"}), 400
    
    enrollment.grade = grade
    db.session.commit()
    
    return jsonify(enrollment.to_dict()), 200

@student_bp.route('/<int:id>/gpa', methods=['GET'])
@any_user_required()
def get_gpa(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"msg": "Student not found"}), 404
    
    gpa = student.calculate_gpa()
    return jsonify({
        "student_id": student.student_id,
        "name": student.name,
        "gpa": gpa
    }), 200
