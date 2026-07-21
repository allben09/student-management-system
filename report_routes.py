from flask import Blueprint, request, jsonify, Response
from app.models import Student, Enrollment
from app.auth import teacher_or_admin_required
from app.database import db
import csv
import io
from datetime import datetime

report_bp = Blueprint('reports', __name__)

@report_bp.route('/students/csv', methods=['GET'])
@teacher_or_admin_required()
def export_students_csv():
    students = Student.query.filter_by(is_active=True).all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Student ID', 'Name', 'Email', 'Phone', 'Enrollment Date', 'GPA', 'Courses'])
    
    for student in students:
        courses = [e.course.course_id for e in student.enrollments if e.course]
        writer.writerow([
            student.student_id,
            student.name,
            student.email,
            student.phone or '',
            student.enrollment_date.strftime('%Y-%m-%d') if student.enrollment_date else '',
            student.calculate_gpa(),
            ', '.join(courses)
        ])
    
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment;filename=students_{datetime.now().strftime("%Y%m%d")}.csv'}
    )
