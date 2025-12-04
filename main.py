from contextlib import asynccontextmanager
from fastapi import FastAPI
from App.ApiLayer.postsApi import router as posts_router
from App.DbLayer.db_connection import initialize_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize database
    print("Starting up...")

    initialize_db()
    
    yield
    # Shutdown: 
    print("Shutting down...")

app = FastAPI(title="Liquid Labs Posts API", lifespan=lifespan)
app.include_router(posts_router)

@app.get("/")
async def home():
    return {"message": "Welcome to the Liquid Labs Posts API! - By Aashif Ameer"}