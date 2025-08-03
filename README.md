# 🧾 Expense Tracker API (Flask + PostgreSQL + Docker)

A simple **Expense Tracker REST API** built with **Flask**, **PostgreSQL**, and **Docker Compose**.  
Users can **register, log in, and manage expenses** using secure JWT authentication.

---

## 🚀 Features

- **User Authentication**
  - Register & Login with hashed passwords
  - JWT-based authentication

- **Expense Management**
  - Create, Read, Update, and Delete expenses
  - View all expenses for a logged-in user

- **Database**
  - PostgreSQL for persistent storage

- **Dockerized Setup**
  - One command to spin up API+Database

---

## 📂 Project Structure

```
expense-tracker/
│
├── app.py                # Flask entry point
├── models.py             # SQLAlchemy models
├── auth.py               # Auth routes (Register, Login)
├── expenses.py           # Expense CRUD routes
├── config.py             # Configuration (DB, JWT secret)
├── extensions.py         # SQLAlchemy and JWT init
├── requirements.txt      # Python dependencies
├── Dockerfile            # Backend container
├── docker-compose.yml    # API + PostgreSQL setup
└── README.md
```

---
## 📦 Tech Stack
- Backend: Python, Flask, Flask-JWT-Extended, SQLAlchemy
- Database: PostgreSQL
- Containerization: Docker, Docker Compose
- Testing Tool: Postman / Curl

---
### Author
Tushar Sharma