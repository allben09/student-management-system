<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/github/license/allben09/student-management-system" alt="License">
  <img src="https://img.shields.io/github/stars/allben09/student-management-system?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/allben09/student-management-system?style=social" alt="Forks">
  <img src="https://img.shields.io/github/issues/allben09/student-management-system" alt="Issues">
  <img src="https://img.shields.io/badge/Docker-Ready-blue?logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/Code-Style-Black-black" alt="Code Style">
  <img src="https://img.shields.io/badge/CI-Passing-brightgreen?logo=github-actions" alt="CI">
  <img src="https://img.shields.io/badge/Code_Coverage-85%25-green" alt="Coverage">
  <img src="https://img.shields.io/badge/Security-Passing-brightgreen" alt="Security">
  <img src="https://img.shields.io/badge/API-RESTful-blue" alt="API">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs">
</p>

<h1 align="center">🎓 Advanced Student Management System</h1>

<p align="center">
  <strong>A production-ready, full-featured Student Management System built with Flask, SQLAlchemy, JWT authentication, and Docker.</strong>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-key-features">Features</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-api-documentation">API</a> •
  <a href="#-docker">Docker</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 📑 Table of Contents

- [About](#-about)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start-5-minutes)
- [Installation](#-installation)
- [API Documentation](#-api-documentation)
- [Dashboard](#-dashboard-screenshots)
- [Testing](#-testing)
- [Docker](#-docker)
- [Project Roadmap](#-project-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 About

This **Advanced Student Management System** is a complete, production-ready solution for managing students, courses, enrollments, and grades. Built with modern Python technologies, it features a secure JWT authentication system with role-based access control (Admin, Teacher, Student), a RESTful API, and a responsive web dashboard with real-time analytics.

**Why this project stands out:**
- ✅ **Complete solution** - Everything from student registration to grade management
- ✅ **Production ready** - Docker, CI/CD, security scanning, and testing included
- ✅ **Modern stack** - Flask, SQLAlchemy, JWT, Bootstrap 5, Chart.js
- ✅ **Developer friendly** - Clean code, comprehensive documentation, and contribution guidelines
- ✅ **Scalable** - Designed to grow from SQLite to PostgreSQL/MySQL
- ✅ **Educational** - Perfect for learning full-stack development
- ✅ **Portfolio ready** - Professional project to showcase your skills

---

## ✨ Key Features

### 🔐 Security & Authentication
- **JWT-based authentication** with access and refresh tokens
- **Role-based access control** (Admin, Teacher, Student)
- **Password hashing** with bcrypt
- **Secure environment configuration** with `.env`
- **CORS** properly configured

### 👨‍🎓 Student Management
- Complete CRUD operations
- Search, filter, and pagination
- Student enrollment in courses
- Grade assignment and management
- GPA calculation
- Student activity tracking

### 📚 Course Management
- Course creation and management
- Capacity management (max students)
- Instructor assignment
- Course enrollment tracking
- Course analytics

### 📊 Dashboard & Analytics
- Real-time statistics cards
- Interactive charts with Chart.js
- Course enrollment distribution
- Quick action buttons
- Role-based views

### 📄 Reporting & Export
- Export student data to CSV
- PDF report generation (coming soon)
- Grade reports
- Course enrollment reports

### 🐳 DevOps Ready
- **Docker** and **Docker Compose** support
- **GitHub Actions** CI/CD pipeline
- **Security scanning** with Bandit
- **Code coverage** reporting
- **Pre-commit hooks** for code quality

### 🧪 Testing
- Unit tests with pytest
- Integration tests
- API endpoint testing
- Coverage reporting

---

## 🛠️ Tech Stack

### Backend
- **Flask** 2.3.3 - Web framework
- **SQLAlchemy** 3.0.5 - ORM
- **Flask-JWT-Extended** - JWT authentication
- **Flask-Migrate** - Database migrations
- **Flask-Bcrypt** - Password hashing
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **Bootstrap 5** - UI framework
- **Chart.js** - Interactive charts
- **Jinja2** - Template engine
- **Font Awesome** - Icons

### Database
- **SQLite** (development)
- Ready for **PostgreSQL** and **MySQL**

### DevOps & Tools
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **pytest** - Testing framework
- **Black** - Code formatting
- **Flake8** - Linting
- **Bandit** - Security scanning
- **pre-commit** - Git hooks

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Clone the repository
git clone https://github.com/allben09/student-management-system.git
cd student-management-system

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp .env.example .env
# Edit .env with your settings

# 5. Initialize database
flask db upgrade
flask create-admin

# 6. Run the app
python run.py

# 7. Open browser at http://localhost:5000
# Login: admin / admin123
