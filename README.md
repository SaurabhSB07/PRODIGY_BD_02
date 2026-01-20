# PRODIGY_BD_02 – Persistent Storage with Database Integration

## 📌 Task Description
This project is **Task 02** of the **Prodigy InfoTech Backend Development Internship**.

The task extends a basic REST API to use a **relational database** for **persistent storage**, following real-world backend development practices.

---

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL (Relational Database)
- psycopg2
- python-dotenv
- Git & GitHub

---

## ✨ Features
- REST API for **User Management**
- Persistent data storage using **PostgreSQL**
- ORM-based database interaction (Django ORM)
- Environment-based configuration using `.env`
- Database migrations for schema management
- Proper HTTP status codes & error handling
- Input validation (email, age, required fields)

---

## 🧱 User Model Schema
| Field | Type |
|------|------|
| id | UUID |
| name | String |
| email | Email |
| age | Integer |

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/api/users/` | Create a new user |
| GET | `/api/users/` | Get all users |
| GET | `/api/users/<id>/` | Get user by ID |
| PUT | `/api/users/<id>/` | Update user |
| DELETE | `/api/users/<id>/` | Delete user |

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```env
DB_NAME=prodigy_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

