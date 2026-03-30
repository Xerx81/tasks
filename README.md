# 🧩 Task Manager App (FastAPI + React)

A full-stack task management application built with **FastAPI (backend)** and **React (frontend)**.
It demonstrates authentication, role-based access control, and CRUD operations with a clean, scalable structure.

<img width="1895" height="907" alt="image" src="https://github.com/user-attachments/assets/845c5409-b8f8-462e-ace0-ab01332d8d94" />
<img width="1873" height="903" alt="image" src="https://github.com/user-attachments/assets/b3abe39d-c2be-451a-8280-353fb7cf9e04" />
<img width="1890" height="908" alt="image" src="https://github.com/user-attachments/assets/3a3e90e5-d0ce-44bd-b3b2-24e024ac6e7a" />

---

## 🚀 Features

### 🔐 Authentication & Security

* User registration & login
* JWT-based authentication
* Password hashing using bcrypt
* Protected routes using token-based access

### 👥 Role-Based Access

* **Admin**

  * Create tasks
  * Update tasks
  * Delete tasks
* **User**

  * View all tasks

### 📦 Backend (FastAPI)

* RESTful API design
* Modular project structure
* SQLite database (easy setup)
* Input validation using Pydantic
* Dependency-based authentication system

### 💻 Frontend (React)

* Login & Register pages
* Dashboard to view tasks
* Admin controls for task management
* API integration using Fetch

---

## 🏗️ Project Structure

```
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── deps.py
│   │   │   ├── __init__.py
│   │   │   └── v1
│   │   │       ├── endpoints
│   │   │       │   ├── auth.py
│   │   │       │   └── task.py
│   │   │       └── __init__.py
│   │   ├── core
│   │   │   └── security.py
│   │   ├── db
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── task.py
│   │   │   └── user.py
│   │   └── schemas
│   │       ├── task.py
│   │       └── user.py
│   ├── requirements.txt
│   └── tasks.db
├── frontend
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.svg
│   │   └── icons.svg
│   ├── README.md
│   ├── src
│   │   ├── App.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   └── pages
│   │       ├── Auth.jsx
│   │       ├── Dashboard.jsx
│   │       └── Task.jsx
│   └── vite.config.js
└── README.md
```

---

## ⚙️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)

### Frontend

* React (Vite)
* Tailwind CSS
* Fetch API

---

## 🛠️ Setup Instructions

### 🔹 Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

Swagger docs:

```
http://localhost:8000/docs
```

---

### 🔹 Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

Credtionals for testing:
- Admin
```
username: admin
password: adminpass123
```

- User
```
username: testuser
password: testpass123
```

---

## 🔐 Authentication Flow

1. User registers via `/api/v1/auth/register`
2. User logs in via `/api/v1/auth/login`
3. Backend returns JWT token
4. Token is stored in frontend (localStorage)
5. Token is sent in requests:

```
Authorization: Bearer <token>
```

---

## 📌 API Endpoints

### Auth

* `POST /api/v1/auth/register`
* `POST /api/v1/auth/login`

### Tasks

* `GET /api/v1/tasks` → View tasks (all users)
* `POST /api/v1/tasks` → Create task (admin only)
* `PUT /api/v1/tasks/{id}` → Update task (admin only)
* `DELETE /api/v1/tasks/{id}` → Delete task (admin only)

---

## 🧠 Scalability Notes

The project follows a modular architecture with separation of:

* Models (database layer)
* Schemas (validation layer)
* Routes (API layer)
* Core logic (security & configuration)

This structure allows:

* Easy addition of new features (e.g., projects, teams)
* Improved maintainability and readability

---

## 📌 Future Improvements

* Task assignment to users
* Pagination & filtering
* Better UI/UX
* Docker support
* Redis caching

---
