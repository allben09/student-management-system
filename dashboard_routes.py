from flask import Blueprint, jsonify
from app.models import Student, Course, Enrollment
from app.auth import admin_required
from app.database import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/stats', methods=['GET'])
@admin_required()
def get_stats():
    total_students = Student.query.filter_by(is_active=True).count()
    total_courses = Course.query.filter_by(is_active=True).count()
    total_enrollments = Enrollment.query.count()
    
    # Calculate average GPA
    enrollments_with_grades = Enrollment.query.filter(Enrollment.grade.isnot(None)).all()
    if enrollments_with_grades:
        avg_gpa = round(sum(e.grade for e in enrollments_with_grades) / len(enrollments_with_grades), 2)
    else:
        avg_gpa = 0.0
    
    # Course enrollment distribution
    course_distribution = []
    for course in Course.query.filter_by(is_active=True).all():
        course_distribution.append({
            'name': course.name,
            'enrolled': course.enrollments.count(),
            'max': course.max_students
        })
    
    return jsonify({
        'total_students': total_students,
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'avg_gpa': avg_gpa,
        'course_distribution': course_distribution
    }), 200
