from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session

import db_operations as db_op

import json

router = APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/planes")
async def get_planes(db:Session = Depends(get_db)):
    frames = db_op.get_frames(db)
    return frames

@router.get("/plane")
async def get_plane_history(icao: str, db:Session = Depends(get_db)):
    frames = db_op.get_plane_frames_history(db, icao)
    return frames