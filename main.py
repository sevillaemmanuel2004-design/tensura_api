from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from database import engine
import models

app = FastAPI(title="Tensura Fanbase API")
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def serve_home():
    return FileResponse("index.html")
    
# 1️⃣ Get All Characters
@app.get("/characters")
def get_characters(db: Session = Depends(get_db)):
    try:
        return db.query(models.Character).all()
    except Exception as e:
        return {"error": str(e)}

# 2️⃣ Get Specific Character
@app.get("/characters/{character_id}")
def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(models.Character).filter(
        models.Character.id == character_id
    ).first()

    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    return character

# 3️⃣ Get Actors
@app.get("/actors")
def get_actors(db: Session = Depends(get_db)):
    try:
        return db.query(models.Character).all()
    except Exception as e:
        return {"error": str(e)}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
