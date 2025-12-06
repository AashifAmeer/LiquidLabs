# Liquid Labs Posts API Project - Aashif Ameer

This is a simple Fast API project built using **FastAPI(Python) + SQLite** that fetches posts from the public JSONPlaceholder API, caches them
locally in an SQLite database, and serves them through REST endpoints. Built with a layered architecture
and desgined for mainatability.

## Tech Stack
- Backend      : Python 3.12+, FastAPI, HTTPX
- Database     : SQLite (File-based), Raw SQL queries (no ORM)
- Architecture : N-Tier Architecture (API Layer, Service Layer, Database Layer) 

## Project Overview
- On startup, the app checks if the SQLite database and posts table exist, if not, will be created on build.
- When requests posts:
  - First check cache (SQLite)
  - if found, then return cache data
  - if not, then fetch from public API: [https://jsonplaceholder.typicode.com/posts]
- Fetched posts are stored in SQLite for future requests.
- Completely built using raw SQL queries. (No ORM is used).
- Supports error handling

## Architecture
1. API Layer
   - Handles routes and HTTP responses.
2. Service Layer
   - Handles business logic, caching, API calls
4. Database Layer
   - Database queries, DB initialization and connections
  
## Setup Instructions

### 1. Clone the project from the Github repository
```bash
git clone https://github.com/Aashif/LiquidLabsPosts.git
```
### 2. Redirect to project folder
```bash
cd LiquidLabsPosts
```
### 3. Create a virtual environment
```bash
python -m venv venv
```
### 4. Activate virtual environment
```bash
# Windows:
venv/Scripts\activate
# Linux/Mac
source venv/bin/activate
```
### 5. Install dependencies
```bash
pip install -r requirements.txt
```
### 6. Run the FastAPI server
```bash
uvicorn main:app --reload --host localhost
```
### 7. Test API endpoints using Postman or any other tools.
  - [http://localhost:8000/api/posts]    : Retrieve all posts
  - [http://localhost:8000/api/posts/1]  : Retrieve a post by ID
