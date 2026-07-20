# 🎓 Advanced Student Management System

A full-featured, production-ready Student Management System built with **Flask**, **SQLAlchemy**, **JWT authentication**, and **Docker**. This system provides a RESTful API, a modern web dashboard, role-based access control, data export, and more—designed to stand out in your portfolio.

## ✨ Key Features

- **Secure Authentication**: JWT-based login with role-based access (Admin, Teacher, Student).
- **RESTful API**: Complete CRUD operations for students, courses, enrollments, and grades.
- **Web Dashboard**: Responsive admin interface built with Bootstrap 5.
- **Advanced Data Management**:
  - SQLite database (easily switch to PostgreSQL/MySQL).
  - Search, pagination, and filtering.
  - Export data to CSV and PDF reports.
- **Role-Based Access Control**:
  - **Admin**: Full control over all data.
  - **Teacher**: Can view and manage students, assign grades.
  - **Student**: View own profile, grades, and enrolled courses.
- **Analytics Dashboard**: Visual statistics with charts (using Chart.js).
- **Dockerized**: Run with a single `docker-compose up` command.
- **Testing**: Unit and integration tests with pytest.
- **Logging**: Rotating file logs for audit trails.
- **Environment Configuration**: Use `.env` for secure settings.

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-JWT-Extended, Flask-Migrate, Bcrypt
- **Frontend**: Bootstrap 5, Jinja2, Chart.js
- **Database**: SQLite (development), PostgreSQL/MySQL ready
- **Authentication**: JWT (JSON Web Tokens)
- **Reporting**: ReportLab (PDF), Pandas (CSV/Excel)
- **Deployment**: Docker, Gunicorn
- **Testing**: pytest, pytest-flask

## 📋 Prerequisites

- Python 3.10+
- Docker (optional, for containerized deployment)
- Git

## 🚀 Quick Start

### Option 1: Run Locally (without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/allben09/student-management-system.git
   cd student-management-system
