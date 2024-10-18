# FastAPI Application

This is a FastAPI application for managing posts and comments with user authentication. The application allows normal users and admins to perform different actions based on their roles.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)\
- [Application Structure](#application-structure)

## Features

- User registration (normal and admin)
- User login with JWT authentication
- Create and view posts
- Add and view comments on posts
- Admin-only access to certain routes

## Technologies Used

- Python 3.7+
- FastAPI
- SQLAlchemy
- SQLite (for local development)
- JWT (JSON Web Tokens)
- Passlib (for password hashing)
- Pydantic (for data validation)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. **Create a virtual environment**
      python -m venv venv
3. **Activate the virtual enviornment**
     venv\Scripts\activate
4.  **install the dependencies**
       pip install -r requirements.txt
5.  **run the app**
      uvicorn main:app --reload
6. **Access the application**
      http://127.0.0.1:8000/docs


##Application Structure

│
├── main.py               # Entry point of the FastAPI application
├── database.py           # Database setup and session management
├── models/               # Database models
│   ├── user_model.py     # User model
│   ├── post_model.py     # Post model
│   └── comment_model.py   # Comment model
├── routes/               # API routes
│   ├── auth_routes.py    # Authentication routes
│   ├── post_routes.py    # Post-related routes
│   └── admin_routes.py   # Admin-specific routes
├── schemas.py            # Pydantic models for request/response validation
├── utils.py              # Utility functions (e.g., password hashing)
├── auth.py               # Authentication logic (JWT token handling)
└── requirements.txt      # List of dependencies


