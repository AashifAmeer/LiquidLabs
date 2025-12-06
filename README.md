Liquid Labs Posts API Project - Aashif Ameer

This is a simple Fast API project that fetches posts from the public JSONPlaceholder API, caches them
locally in an SQLite database, and serves them through REST endpoints. Built with a layered architecture
and desgined for mainatability.

Tech Stack
Backend      : Python3.12+, FastAPI, HTTPX
Database     : SQLite (File-based)
Architecture : N-Tier Architecture (API Layer, Business Logic Layer, Database Layer) 

Project Structure

LiquidLabs/
│── App/
│   ├── ApiLayer/
│   │   └── postsApi.py
│   ├── ServiceLayer/
│   │   └── posts_service.py
│   ├── DbLayer/
│   │   ├── db_connection.py
│   │   └── Repositories/
│   │       └── posts_repository.py
│   ├── Schemas/
│   │   └── post_model.py
│── Instance/
│   └── liquidlabs.db   (will be Auto-created)
│── main.py
│── requirements.txt
│── README.md

