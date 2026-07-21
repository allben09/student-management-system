from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models import User

def role_required(allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user or user.role not in allowed_roles:
                return jsonify({"msg": "Insufficient permissions"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def admin_required():
    return role_required(['admin'])

def teacher_or_admin_required():
    return role_required(['admin', 'teacher'])

def any_user_required():
    return role_required(['admin', 'teacher', 'student'])
