from flask import Blueprint, render_template, send_from_directory
from app.auth import admin_required
import os

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    return render_template('index.html')

@web_bp.route('/dashboard')
@admin_required
def dashboard():
    return render_template('dashboard.html')

@web_bp.route('/students')
@admin_required
def students_page():
    return render_template('students.html')

@web_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(web_bp.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
