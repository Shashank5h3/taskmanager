# Team Task Manager

## Overview

A full-stack **Task Management System** built using Django that allows teams to manage projects and tasks efficiently with **role-based access control**.

---

## Features

### Authentication

* User Registration (Admin / Member)
* Login & Logout system
* Secure password handling

### Admin Features

* Create Projects
* Create & Assign Tasks
* View all tasks
* Dashboard with analytics:

  * Total Tasks
  * Completed Tasks
  * Pending Tasks
  * Overdue Tasks

### Member Features

* View assigned tasks
* Update task status (Pending → In Progress → Completed)

### Dashboard

* Real-time task statistics
* Overdue task highlighting
* Clean UI with status badges

### UI/UX

* Modern responsive design
* Bootstrap-based layout
* Premium glassmorphism login/register UI

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Deployment:** Railway
* **Version Control:** Git & GitHub

---

## Installation & Setup

```bash
git clone https://github.com/YOUR_USERNAME/taskmanager.git
cd taskmanager

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

Open:

<!-- http://127.0.0.1:8000/ -->

## 🌐 Live Demo

<!-- 👉 https://your-app-name.up.railway.app -->

---

## Demo Video

👉 Add your demo video link here

## Project Structure

taskmanager/
│── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   ├── static/
│
│── taskmanager/
│   ├── settings.py
│   ├── urls.py

## Key Concepts Used

* Django Custom User Model
* Role-Based Access Control
* ORM Relationships (ForeignKey)
* Authentication System
* CRUD Operations
* Template Rendering

## Future Improvements

* Email notifications for tasks
* Task filtering & search
* REST API integration
* Team collaboration features

## Author

*Shashank Kalla*
B.Tech CSE | Full Stack Developer

## Conclusion

This project demonstrates a complete **full-stack development workflow**, including backend logic, frontend UI, database management, and deployment.
