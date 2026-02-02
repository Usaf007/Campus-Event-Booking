# 🎓 Campus Event Booking System

A full-stack, database-driven web application built with **Django** and **Bootstrap 5**. This system allows university students to browse academic events, secure bookings in real-time, and manage their tickets via a personal dashboard.

**Developer:** Yousaf Atiq  
**Status:** ✅ Active / Completed

---

## 🚀 Features

### 🔹 User & Authentication
* **Secure Sign Up/Login:** Built on top of Django's robust authentication system.
* **Role-Based Access:** Admins have full control; Users can only manage their own bookings.
* **Profile Management:** Personalized dashboard ("My Bookings") for every student.

### 🔹 Event Management (Backend)
* **Real-time Seat Tracking:** Automatically decrements available seat counts upon booking.
* **Double-Booking Prevention:** Logic to prevent a user from booking the same event twice.
* **Sold Out Logic:** "Book Now" buttons are disabled automatically when seats reach zero.
* **Admin Panel:** Full GUI for creating events, uploading images, and managing capacity.

### 🔹 Modern Frontend
* **Responsive Design:** Built with **Bootstrap 5** for mobile and desktop compatibility.
* **Dynamic UI:** Clean "Glassmorphism" aesthetic with hover effects and card layouts.
* **Alert System:** Success/Error messages (Toast notifications) for user feedback.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django 5.x
* **Database:** SQLite (Dev), PostgreSQL (Production ready)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Version Control:** Git & GitHub

---

## 📸 Screenshots

*(You can upload screenshots of your Home Page and Dashboard here later)*

---

## ⚙️ Installation & Setup

If you want to run this project locally, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/campus-event-booking.git](https://github.com/YOUR_USERNAME/campus-event-booking.git)
cd campus-event-booking
2. Create a Virtual Environment

Bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies

Bash
pip install django pillow
4. Apply Migrations

Bash
python manage.py migrate
5. Create a Superuser (Admin)

Bash
python manage.py createsuperuser
6. Run the Server

Bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

🧪 Testing the Logic
Login: Sign up as a new user.

Book: Navigate to an event and click "Book Now".

Verify: Check the "My Bookings" tab to see your ticket.

Cancel: Cancel the ticket and watch the seat count on the homepage increase automatically.