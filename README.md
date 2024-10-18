# FastAPI Application

This is a FastAPI application for managing posts and comments with user authentication. The application allows normal users and admins to perform different actions based on their roles.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Application Structure](#application-structure)
- [Usage](#usage)
  - [Normal Users](#normal-users)
  - [Admin Users](#admin-users)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

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
