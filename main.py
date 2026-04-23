from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Base
import models

app = FastAPI(title="Tensura Fanbase API")

# ✅ Create tables ONCE (safe place)
Base.metadata.create_all(bind=engine)

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home
@app.get("/")
def serve_home():
    return FileResponse("index.html")

# ✅ Startup seeding (FIXED)
@app.on_event("startup")
def startup():
    db = SessionLocal()

    if db.query(models.Character).count() == 0:
        db.add_all([
            models.Character(
                name="Rimuru Tempest",
                title="Demon Lord",
                description="Slime turned strongest being",
                category="Demon Lord"
            ),
            models.Character(
                name="Milim Nava",
                title="Destroyer",
                description="One of the oldest Demon Lords",
                category="Demon Lord"
            ),
            models.Character(
                name="Guy Crimson",
                title="Primordial Red",
                description="Strongest Demon Lord",
                category="Demon Lord"
            )
        ])
        db.commit()

    db.close()

# --------------------------
# CHARACTERS
# --------------------------

@app.get("/characters")
def get_characters(db: Session = Depends(get_db)):
    return db.query(models.Character).all()

@app.get("/characters/{character_id}")
def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(models.Character).filter(
        models.Character.id == character_id
    ).first()

    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    return {
        "id": character.id,
        "name": character.name,
        "title": character.title,
        "description": character.description,
        "category": character.category,
        "actor_id": character.actor_id
    }

# --------------------------
# ACTORS (FIXED)
# --------------------------

@app.get("/actors")
def get_actors(db: Session = Depends(get_db)):
    return db.query(models.Actor).all()
