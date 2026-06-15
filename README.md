# DSA Revision Scheduler

A full-stack DSA Revision Tracking application built using **FastAPI**, **SQLite**, **HTML**, **CSS**, **JavaScript**, and **Chart.js**.

The application helps users track solved DSA problems, schedule revisions using spaced repetition, monitor revision progress, and visualize analytics through an interactive dashboard.

---

## Features

### Problem Management

* Add new DSA problems
* Edit existing problems
* Delete problems
* View all solved problems

### Search & Filtering

* Search problems by title
* Filter problems by topic
* Filter problems by difficulty

### Revision Tracking

* Automatic revision schedule generation
* Upcoming revisions dashboard
* Mark revisions as completed
* Completed revision tracking

### Analytics Dashboard

* Total solved problems
* Pending revisions count
* Completed revisions count
* Revision streak tracker
* Topic-wise analytics

### Data Visualization

* Pie chart showing topic distribution using Chart.js

### Export Functionality

* Export all problems to CSV format

---

## Tech Stack

### Backend

* FastAPI
* SQLite

### Frontend

* HTML
* CSS
* JavaScript

### Visualization

* Chart.js

---

## Project Structure

```text
DSA-Revision-Scheduler
│
├── app
│   ├── database
│   │   ├── db.py
│   │   └── models.py
│   │
│   ├── routers
│   │   ├── problems.py
│   │   └── revisions.py
│   │
│   ├── schemas
│   │   └── problem.py
│   │
│   ├── static
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── templates
│   │   └── index.html
│   │
│   └── main.py
│
├── scheduler.db
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <your-github-repository-url>
cd DSA-Revision-Scheduler
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

### Open Browser

```text
http://127.0.0.1:8000
```

---

## API Endpoints

### Problems

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| POST   | /problem      | Add problem      |
| PUT    | /problem/{id} | Update problem   |
| DELETE | /problem/{id} | Delete problem   |
| GET    | /problems     | Get all problems |

### Revisions

| Method | Endpoint            |
| ------ | ------------------- |
| GET    | /revisions/today    |
| GET    | /revisions/upcoming |
| GET    | /revisions/history  |
| PUT    | /revision/{id}      |

### Analytics

| Method | Endpoint              |
| ------ | --------------------- |
| GET    | /dashboard            |
| GET    | /dashboard/topic-wise |
| GET    | /streak               |
| GET    | /export               |

---

## Future Improvements

* User Authentication
* Login & Registration
* Email Revision Reminders
* Dark Mode
* Deployment on Render/Railway
* AI-Based Revision Suggestions

---

## Screenshots

### Dashboard

(Add screenshot here)

### Problems Table

(Add screenshot here)

### Upcoming Revisions

(Add screenshot here)

### Topic Analytics

(Add screenshot here)

---

## Author

Lokesh Prasad
