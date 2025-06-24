# Late Show API Challenge

A Flask REST API for a Late Night TV show system using PostgreSQL, JWT authentication, and MVC architecture.

## Setup

### 1. Clone and Install Dependencies

```sh
git clone <your-repo-url>
cd late-show-api-challenge
pipenv install
pipenv shell
```

### 2. PostgreSQL Setup

Create the database:

```sql
CREATE DATABASE late_show_db;
```

### 3. Environment Variables

Set your database connection:

```sh
export DATABASE_URI="postgresql://username:password@localhost:5432/late_show_db"
export JWT_SECRET_KEY="your-secret-key"
export FLASK_APP=server.app
```

### 4. Migrate and Seed

```sh
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python -m server.seed
```

### 5. Run the Server

```sh
flask run
```

## Auth Flow

1. **Register:** `POST /register` (username, password)
2. **Login:** `POST /login` (returns JWT token)
3. **Use token:** Add header `Authorization: Bearer <token>` to protected routes

## Routes

| Route        | Method | Auth? | Description                  |
| ------------ | ------ | ----- | ---------------------------- |
| /register    | POST   | ❌     | Register a user              |
| /login       | POST   | ❌     | Log in + get JWT             |
| /episodes    | GET    | ❌     | List episodes                |
| /episodes/<id> | GET  | ❌     | Get episode + appearances    |
| /episodes/<id> | DELETE | ✅   | Delete episode + appearances |
| /guests      | GET    | ❌     | List guests                  |
| /appearances | POST   | ✅     | Create appearance            |

## Sample Requests & Responses

### Register User

POST /register
Content-Type: application/json

```
{
  "username": "admin",
  "password": "password"
}
```

**Response:**

```
{
  "message": "User registered successfully"
}
```

### Login

POST /login
Content-Type: application/json

```
{
  "username": "admin",
  "password": "password"
}
```

**Response:**

```
{
  "access_token": "..."
}
```

### List Episodes

GET /episodes

**Response:**

```
[
  {
    "id": 1,
    "date": "2023-01-01",
    "number": 1
  }
]
```

### Get Episode Details

GET /episodes/1

**Response:**

```
{
  "id": 1,
  "date": "2023-01-01",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 5,
      "guest": {
        "id": 1,
        "name": "Tom Hanks",
        "occupation": "Actor"
      }
    }
  ]
}
```

### Create Appearance (Protected)

POST /appearances
Authorization: Bearer <your_jwt_token>
Content-Type: application/json

```
{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```

**Response:**

```
{
  "id": 4,
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```

### Delete Episode (Protected)

DELETE /episodes/1
Authorization: Bearer <your_jwt_token>

**Response:**

```
{
  "message": "Episode deleted"
}
```

## Postman Usage Guide

1. **Import Collection:**  
   * Open Postman  
   * Click "Import" → "File"  
   * Select `challenge-4-lateshow.postman_collection.json`
2. **Set Environment Variables:**  
   * Create a new environment  
   * Add variable `base_url` = `http://localhost:5000`  
   * Add variable `token` (will be set after login)
3. **Testing Flow:**  
   * Run "Register User" request  
   * Run "Login" request and copy the token  
   * Set the `token` environment variable  
   * Test all other endpoints
4. **Protected Routes:**  
   * Use `{{token}}` in Authorization header  
   * Format: `Bearer {{token}}`

## Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

##  Submission Checklist

- [x] MVC folder structure
- [x] PostgreSQL used (no SQLite)
- [x] Models + validations complete
- [x] Auth implemented + protected routes
- [x] Seed data works
- [x] All routes work and have been tested in Postman
- [x] Clean, complete README.md
- [x] GitHub repo pushed and shared 