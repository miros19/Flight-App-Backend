from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from config import SessionLocal, engine
from data_generator import DataGenerator
import db_operations as db_ops
import models
from routes import router
from sqlalchemy.orm import Session

generator = DataGenerator()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_frames():
    global generator
    frames = generator.generate_frames()
    with SessionLocal.begin() as db:
        for frame in frames:
            db_ops.new_frame(db = db, frame= frame)
        db.commit()

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_frames, "interval", seconds = 1)
    scheduler.start()
    yield

models.Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan = lifespan)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}