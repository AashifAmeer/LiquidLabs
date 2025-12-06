from contextlib import asynccontextmanager
from fastapi import FastAPI
from App.ApiLayer.postsApi import router as posts_router
from App.DbLayer.db_connection import initialize_db
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("\nStarting Liquid Labs Posts API...")

    # nitialize database
    initialize_db()
    
    # Print helpful usage instructions
    logger.info(" API is ready to use.")
    logger.info(" Use the following endpoints:")
    logger.info(" Welcome endpoint : http://127.0.0.1:8000")
    logger.info(" GET all posts    : http://127.0.0.1:8000/posts")
    logger.info(" GET a post by ID : http://127.0.0.1:8000/posts/{id} (replace {id} with a number)")
    logger.info(" To stop the server, press CTRL+C in the terminal.\n")

    yield

    # Shutdown: 
    logger.info(" Shutting down Liquid Labs Posts API...")

# Create FastAPI instance
app = FastAPI(
    title="Liquid Labs Posts API", 
    version="1.0.0",
    description="An API to fetch and cache posts from a public API using FastAPI and SQLite.",
    lifespan=lifespan
    )

# Include the posts router
app.include_router(posts_router)

# Home route
@app.get("/")
async def home():
    return {"message": "Welcome to the Liquid Labs Posts API! - By Aashif Ameer"}