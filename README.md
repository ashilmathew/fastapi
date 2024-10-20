# FastAPI Application

This is a FastAPI application for managing posts and comments with user authentication. The application allows normal users and admins to perform different actions based on their roles.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

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
   git clone https://github.com/ashilmathew/fastapi.git
   cd fastapi
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



