# 🎓 Campus Event Booking System

![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Django](https://img.shields.io/badge/Django-5.0-green?style=flat-square)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)

> A robust, full-stack event management solution designed for university campuses. Built with **Django** MVT architecture and **Bootstrap 5** for a seamless, responsive user experience.

---

## 📖 Overview

The **Campus Event Booking System** solves the problem of manual event registration by providing a centralized digital platform. It features strict logic for seat management, ensuring no overbooking occurs, and provides a personalized dashboard for students to track their academic schedules.

**Developer:** Usaf  
**Current Version:** v1.0.0

---

## ⚡ Key Features

### 🔐 Advanced Authentication & RBAC
* **Role-Based Access Control (RBAC):** Distinct permissions for Superusers (Admins) and Standard Users (Students).
* **Secure Session Management:** Built on top of Django's industry-standard auth system.
* **Automated Redirection:** Smart routing logic based on login status.

### 📅 Event Logic & Data Integrity
* **Concurrency Handling:** Prevents race conditions where multiple users might book the last seat simultaneously.
* **Dynamic Capacity Tracking:** Seat counts update in real-time upon successful transactions.
* **Constraint Enforcement:** Users are strictly prohibited from double-booking the same event.
* **Soft Cancellation:** Users can release tickets, automatically restoring inventory to the global pool.

### 🎨 Modern UI/UX
* **Glassmorphism Design:** A modern, clean interface using semi-transparent layers and blur effects.
* **Responsive Grid:** Fully functional across Desktop, Tablet, and Mobile devices via Bootstrap 5.
* **Feedback Loops:** Integrated Toast notifications (Success/Warning/Error) for every user action.

---

## 🛠️ Technical Architecture

### Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python & Django | Handles routing, ORM, and business logic. |
| **Frontend** | HTML5, CSS3, JS | Rendered via Django Templates (DTL). |
| **Styling** | Bootstrap 5 | Component library for responsive design. |
| **Database** | SQLite | Lightweight relational database (Dev). |
| **Media** | Pillow | Image processing for event banners. |

### Project Structure
```bash
Campus-Events/
├── events/                 # Main Application App
│   ├── migrations/         # Database propagation files
│   ├── templates/          # HTML files (MVT pattern)
│   │   ├── events/         # Dashboard & Home templates
│   │   └── registration/   # Auth templates (Login/Signup)
│   ├── admin.py            # Admin panel configuration
│   ├── models.py           # Database Schema
│   ├── views.py            # Business Logic & Controllers
│   └── urls.py             # Route definitions
├── mycampus/               # Project Configuration
│   ├── settings.py         # Global configs (Apps, Middleware)
│   └── urls.py             # Root URL dispatcher
├── media/                  # User uploaded content (Images)
├── manage.py               # CLI utility
└── db.sqlite3              # Database file

## ⚡ Quick Start Guide

Follow these steps to get a local copy of the project up and running.

**Prerequisites:**
* Python 3.10 or higher
* Git

### 1. Clone & Configure
First, download the repository and set up a secure virtual environment to isolate project dependencies.

```bash
# Clone the repository
git clone [https://github.com/Usaf007/campus-event-booking.git](https://github.com/Usaf007/campus-event-booking.git)

# Enter the project directory
cd campus-event-booking

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
2. Install & Initialize
Install the required packages and build the database structure.

Bash
# Install Django and image handling libraries
pip install django pillow

# Apply database migrations (Creates tables)
python manage.py migrate

# Create an Admin account (Follow the prompts)
python manage.py createsuperuser
3. Launch the Application
Start the local development server.

Bash
python manage.py runserver
Success! The application is now live.

Frontend: Visit http://127.0.0.1:8000/

Admin Panel: Visit http://127.0.0.1:8000/admin/

🔮 Future Roadmap
[ ] Email Notifications: Send confirmation emails upon booking.

[ ] Waitlist System: Allow users to queue for fully booked events.

[ ] Payment Integration: Stripe/PayPal integration for paid workshops.

[ ] REST API: Build an API using Django REST Framework (DRF) for mobile apps.

🤝 Contribution
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

Built with ❤️ by Usaf