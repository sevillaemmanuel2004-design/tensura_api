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
            # 🔷 Demon Lords (Octagram)
            models.Character(
                name="Rimuru Tempest",
                title="Demon Lord",
                description="Slime who became one of the strongest beings",
                category="Demon Lord"
            ),
            models.Character(
                name="Milim Nava",
                title="Destroyer",
                description="Ancient and overwhelmingly powerful Demon Lord",
                category="Demon Lord"
            ),
            models.Character(
                name="Guy Crimson",
                title="Primordial Red",
                description="Strongest and oldest Demon Lord",
                category="Demon Lord"
            ),
            models.Character(
                name="Ramiris",
                title="Labyrinth Queen",
                description="Small fairy controlling labyrinth and reincarnation",
                category="Demon Lord"
            ),
            models.Character(
                name="Leon Cromwell",
                title="White Sword King",
                description="Calm Demon Lord with ties to heroes",
                category="Demon Lord"
            ),
            models.Character(
                name="Luminous Valentine",
                title="God of Death",
                description="Vampire queen ruling the Holy Empire",
                category="Demon Lord"
            ),
            models.Character(
                name="Dagruel",
                title="Titan Lord",
                description="Ancient giant Demon Lord with immense strength",
                category="Demon Lord"
            ),
            models.Character(
                name="Dino",
                title="Fallen Angel",
                description="Lazy but extremely powerful Demon Lord",
                category="Demon Lord"
            ),

            # 🔶 Former Demon Lords
            models.Character(
                name="Clayman",
                title="Marionette Master",
                description="Scheming Demon Lord who was defeated",
                category="Former Demon Lord"
            ),
            models.Character(
                name="Frey",
                title="Sky Queen",
                description="Harpy Queen who stepped down",
                category="Former Demon Lord"
            ),
            models.Character(
                name="Carrion",
                title="Beast King",
                description="Former Beast Demon Lord",
                category="Former Demon Lord"
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
