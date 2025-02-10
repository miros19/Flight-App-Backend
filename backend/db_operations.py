from sqlalchemy.orm import Session
from models import PlaneFrame


def get_frames(db: Session, limit:int = 10):
    return db.query(PlaneFrame).order_by(PlaneFrame.timestamp.desc()).limit(limit).all()

def get_plane_frames_history(db: Session, icao:str, limit:int = 50):
    return db.query(PlaneFrame).filter(PlaneFrame.icao == icao).order_by(PlaneFrame.timestamp.desc()).limit(limit).all()

def new_frame(db: Session, frame:dict):
    _frame = PlaneFrame(**frame)
    db.add(_frame)
    return _frame
    