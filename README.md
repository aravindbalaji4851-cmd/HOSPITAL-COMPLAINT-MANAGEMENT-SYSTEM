# Hospital Complaint Management System

## Overview

The Hospital Complaint Management System is a REST API developed using Python, Django, and Django REST Framework to manage complaints within a hospital environment.

The application allows users to register, authenticate, submit complaints, view their complaints, update complaint details, and delete complaints. It also provides endpoints to track unresolved complaints, count complaints, summarize complaint statuses, and filter complaints based on priority.

The project implements token-based authentication, user-specific complaint management, and custom permissions to restrict access to complaints.

## Features

* User registration
* Token-based authentication
* Create hospital complaints
* List complaints belonging to the authenticated user
* Retrieve individual complaints
* Update existing complaints
* Delete complaints
* Complaint title and description management
* Complaint type and department classification
* Priority-based complaint management
* Complaint status tracking
* List unresolved complaints
* Count complaints belonging to the authenticated user
* Generate complaint status summaries
* Filter High- and Critical-priority complaints
* User-specific access control
* SQLite database integration

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Django ORM
* Token Authentication
* Git
* GitHub
* VS Code REST Client

## Project Structure

```text
HOSPITAL-COMPLAINT-MANAGEMENT-SYSTEM/
│
├── complaints/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── ...
│
├── healthdesk/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── APIDOC.http
├── db.sqlite3
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/HOSPITAL-COMPLAINT-MANAGEMENT-SYSTEM.git
```

### 2. Navigate to the Project Directory

```bash
cd HOSPITAL-COMPLAINT-MANAGEMENT-SYSTEM
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Configure the required environment variables for your local development environment.

Keep sensitive configuration values, including your Django secret key, outside the public repository.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

The development server will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

All endpoints use the `/healthdesk/` prefix.

### User Authentication

| HTTP Method | Endpoint                     | Description                      | Authentication |
| ----------- | ---------------------------- | -------------------------------- | -------------- |
| POST        | `/healthdesk/user-register/` | Register a new user              | Not required   |
| POST        | `/healthdesk/token/`         | Generate an authentication token | Not required   |

### Complaint Management

| HTTP Method | Endpoint                                 | Description                                 | Authentication |
| ----------- | ---------------------------------------- | ------------------------------------------- | -------------- |
| GET         | `/healthdesk/complaints/`                | List the authenticated user's complaints    | Required       |
| POST        | `/healthdesk/complaints/`                | Create a complaint                          | Required       |
| GET         | `/healthdesk/complaints/<id>/`           | Retrieve a specific complaint               | Required       |
| PUT         | `/healthdesk/complaints/<id>/`           | Update a complaint                          | Required       |
| DELETE      | `/healthdesk/complaints/<id>/`           | Delete a complaint                          | Required       |
| GET         | `/healthdesk/complaints/unresolved/`     | List unresolved complaints                  | Required       |
| GET         | `/healthdesk/complaints/count/`          | Count the user's complaints                 | Required       |
| GET         | `/healthdesk/complaints/status-summary/` | Retrieve a complaint status summary         | Required       |
| GET         | `/healthdesk/complaints/high-critical/`  | List High- and Critical-priority complaints | Required       |

## API Usage Examples

### 1. Register a User

**Endpoint:**

```http
POST /healthdesk/user-register/
```

**Request Body:**

```json
{
    "username": "user01",
    "first_name": "Arun",
    "last_name": "K",
    "email": "arun01@example.com",
    "password": "your-test-password"
}
```

Creates a user account for accessing the complaint management API.

### 2. Generate an Authentication Token

**Endpoint:**

```http
POST /healthdesk/token/
```

**Request Body:**

```json
{
    "username": "user01",
    "password": "your-test-password"
}
```

Use the returned token to authenticate subsequent requests.

### 3. Create a Complaint

**Endpoint:**

```http
POST /healthdesk/complaints/
```

**Request Headers:**

```http
Content-Type: application/json
Authorization: Token YOUR_TOKEN_HERE
```

**Request Body:**

```json
{
    "title": "Monitoring Equipment Not Working",
    "description": "A patient monitoring device appears to be malfunctioning and requires inspection.",
    "complaint_type": "Equipment",
    "department": "Intensive Care Unit",
    "priority": "Critical",
    "status": "Resolved"
}
```

Creates a complaint associated with the authenticated user.

The example values must match the choices and validation rules defined in the application.

### 4. List Complaints

**Endpoint:**

```http
GET /healthdesk/complaints/
```

Returns the complaints belonging to the authenticated user.

**Request Header:**

```http
Authorization: Token YOUR_TOKEN_HERE
```

### 5. Retrieve a Specific Complaint

**Endpoint:**

```http
GET /healthdesk/complaints/1/
```

Retrieves the specified complaint, subject to the application's ownership permissions.

### 6. Update a Complaint

**Endpoint:**

```http
PUT /healthdesk/complaints/1/
```

**Request Body:**

```json
{
    "title": "Long Waiting Time",
    "description": "I waited more than three hours for my appointment.",
    "complaint_type": "Waiting Time",
    "department": "Cardiology",
    "priority": "High",
    "status": "In Progress"
}
```

Updates an existing complaint after validating the submitted data.

A PUT request generally requires all required fields.

### 7. Delete a Complaint

**Endpoint:**

```http
DELETE /healthdesk/complaints/1/
```

Deletes the specified complaint if the authenticated user is authorized to perform the operation.

### 8. List Unresolved Complaints

**Endpoint:**

```http
GET /healthdesk/complaints/unresolved/
```

Retrieves unresolved complaints according to the filtering logic implemented in the application.

### 9. Count Complaints

**Endpoint:**

```http
GET /healthdesk/complaints/count/
```

Returns the number of complaints belonging to the authenticated user.

### 10. Complaint Status Summary

**Endpoint:**

```http
GET /healthdesk/complaints/status-summary/
```

Provides a summary of complaint records grouped by status, according to the implementation in the API.

### 11. Filter High- and Critical-Priority Complaints

**Endpoint:**

```http
GET /healthdesk/complaints/high-critical/
```

Returns complaints belonging to the authenticated user with High or Critical priority.

## Authentication and Permissions

The application uses Django REST Framework's token authentication.

After registering an account, users can obtain an authentication token and include it in requests to protected endpoints.

The token must be provided in the request header:

```http
Authorization: Token YOUR_TOKEN_HERE
```

Custom permissions and user-specific filtering help restrict complaint access to the appropriate authenticated user.

## Complaint Information

Each complaint contains information such as:

* Title
* Description
* Complaint type
* Department
* Priority
* Status
* Associated user

The available values and validation rules are defined in the application's models and serializers.

## API Testing

The API can be tested using:

* VS Code REST Client
* Postman
* Insomnia

The `APIDOC.http` file contains example HTTP requests for testing the available endpoints.

### Recommended Test Cases

* Register a new user.
* Generate an authentication token.
* Create a complaint with valid data.
* List complaints for the authenticated user.
* Retrieve an individual complaint.
* Update an existing complaint.
* Delete a complaint.
* Test invalid complaint data.
* Attempt to access another user's complaint.
* List unresolved complaints.
* Verify complaint counts.
* Verify complaint status summaries.
* Filter complaints by High and Critical priorities.

## Future Enhancements

* Administrator and hospital staff roles
* Complaint assignment to departments or staff
* Complaint resolution notifications
* Complaint history and audit logs
* Search complaints by title or department
* Pagination and advanced filtering
* Automated API testing
* Frontend integration

## Author

**Aravind Balaji K J**

GitHub: [aravindbalaji4851-cmd](https://github.com/aravindbalaji4851-cmd)

Project Repository: [HOSPITAL-COMPLAINT-MANAGEMENT-SYSTEM](https://github.com/aravindbalaji4851-cmd/HOSPITAL-COMPLAINT-MANAGEMENT-SYSTEM)
