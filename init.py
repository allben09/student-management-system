from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from app.database import db, init_db
from app.config import Config
import os

bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(config_class)

    # Initialize extensions
    CORS(app)
    JWTManager(app)
    bcrypt.init_app(app)
    init_db(app)

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.student_routes import student_bp
    from app.routes.course_routes import course_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.report_routes import report_bp
    from app.routes.web_routes import web_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(student_bp, url_prefix='/api/students')
    app.register_blueprint(course_bp, url_prefix='/api/courses')
    app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
    app.register_blueprint(report_bp, url_prefix='/api/reports')
    app.register_blueprint(web_bp)  # Web routes with no prefix

    # CLI command to create admin user
    @app.cli.command("create-admin")
    def create_admin():
        from app.models import User
        from app.database import db
        username = os.getenv('ADMIN_USERNAME', 'admin')
        email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
        password = os.getenv('ADMIN_PASSWORD', 'admin123')
        
        if User.query.filter_by(username=username).first():
            print(f"Admin user '{username}' already exists")
        else:
            admin = User(username=username, email=email, role='admin')
            admin.set_password(password)
            db.session.add(admin)
            db.session.commit()
            print(f"✅ Admin user created: {username}")

    return app
