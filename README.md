# DSA Revision Scheduler

A FastAPI-based application that helps users revise solved DSA problems using a spaced repetition strategy.

## Features

- Add solved problems
- Automatically generate revision schedule
- View today's revisions
- Mark revisions complete
- Dashboard analytics
- Pre-loaded sample DSA problems

## Tech Stack

- Python
- FastAPI
- SQLite

## Setup & Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python -m uvicorn main:app --reload
```

Or on Windows:
```bash
start_server.bat
```

The app will be available at: **http://localhost:8000**

### 3. View API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Get Sample Problems (Pre-loaded)
The app automatically loads 10 sample DSA problems when started:
- Two Sum (Arrays - Easy)
- Binary Search (Searching - Easy)
- Valid Parentheses (Stack - Easy)
- Merge Sort (Sorting - Medium)
- Longest Substring Without Repeating Characters (Strings - Medium)
- Longest Palindromic Substring (Strings - Medium)
- Number of Islands (Graph/DFS - Medium)
- Reverse Linked List (Linked List - Easy)
- Median of Two Sorted Arrays (Arrays - Hard)
- Word Ladder (Graph/BFS - Hard)

### Get All Problems
```bash
curl http://localhost:8000/problems
```

### Get Today's Revisions
```bash
curl http://localhost:8000/revisions/today
```

### Add a New Problem
```bash
curl -X POST http://localhost:8000/problem \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Longest Common Subsequence",
    "topic": "Dynamic Programming",
    "difficulty": "Hard"
  }'
```

### View Dashboard
```bash
curl http://localhost:8000/dashboard
```

### Mark a Revision Complete
```bash
curl -X PUT http://localhost:8000/revision/1
```

## How to Test

1. **Start the server** and visit **http://localhost:8000/docs**
2. **Sample problems are automatically loaded** - go to `/problems` to see them
3. **Add your own problems** using the `/problem` endpoint
4. **Check revisions** using `/revisions/today`
5. **View stats** on the `/dashboard` endpoint

