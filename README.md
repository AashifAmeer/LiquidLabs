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

### Clone the project from the Github repository
[git clone https://github.com/Aashif/LiquidLabsPosts.git]

### Redirect to prject folder
cd LiquidLabsPosts


   
