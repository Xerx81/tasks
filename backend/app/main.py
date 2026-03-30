from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import auth, task
from app.db.session import engine
from app.db.base import Base

# Database
Base.metadata.create_all(bind=engine)

# App
app = FastAPI()

# Routes
app.include_router(auth.router)
app.include_router(task.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}
