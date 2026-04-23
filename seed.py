from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Character, Actor

Base.metadata.create_all(bind=engine)

db: Session = SessionLocal()

# Actors (Japanese Voice Actors)
actors = [
    Actor(name="Miho Okasaki", nationality="Japanese"),  # Rimuru
    Actor(name="Rina Hidaka", nationality="Japanese"),   # Milim
    Actor(name="Takahiro Sakurai", nationality="Japanese"), # Diablo / Guy vibe
    Actor(name="Yukari Tamura", nationality="Japanese"), # Ramiris
    Actor(name="Daisuke Ono", nationality="Japanese"),   # Leon
]

db.add_all(actors)
db.commit()

# Fetch actors
rimuru_actor = db.query(Actor).filter_by(name="Miho Okasaki").first()
milim_actor = db.query(Actor).filter_by(name="Rina Hidaka").first()

characters = [
    Character(
        name="Rimuru Tempest",
        title="New Demon Lord",
        description="A former human reincarnated as a slime who becomes one of the strongest beings.",
        category="Demon Lord",
        actor_id=rimuru_actor.id
    ),
    Character(
        name="Milim Nava",
        title="Destroyer",
        description="One of the oldest Demon Lords with overwhelming power.",
        category="Demon Lord",
        actor_id=milim_actor.id
    ),
    Character(
        name="Guy Crimson",
        title="Primordial Red",
        description="The oldest and strongest Demon Lord.",
        category="Demon Lord"
    ),
    Character(
        name="Ramiris",
        title="Labyrinth Queen",
        description="Controls labyrinths and reincarnation cycles.",
        category="Demon Lord"
    ),
    Character(
        name="Leon Cromwell",
        title="Hero King",
        description="A composed Demon Lord tied to summoned heroes.",
        category="Demon Lord"
    ),
    Character(
        name="Luminous Valentine",
        title="Vampire Queen",
        description="Rules a religious empire with control over life and death.",
        category="Demon Lord"
    ),
    Character(
        name="Dagruel",
        title="Titan King",
        description="Embodiment of raw strength.",
        category="Demon Lord"
    ),
    Character(
        name="Dino",
        title="Sleeping Demon Lord",
        description="Lazy but extremely powerful.",
        category="Demon Lord"
    ),
    Character(
        name="Clayman",
        title="Manipulator",
        description="A scheming Demon Lord defeated by Rimuru.",
        category="Former Demon Lord"
    ),
    Character(
        name="Frey",
        title="Harpy Queen",
        description="Steps down from Demon Lord status.",
        category="Former Demon Lord"
    ),
    Character(
        name="Carrion",
        title="Beast King",
        description="Relinquishes his Demon Lord title.",
        category="Former Demon Lord"
    ),
    Character(
        name="Diablo",
        title="Primordial Black",
        description="Rimuru's most loyal and dangerous subordinate.",
        category="Other"
    ),
]

db.add_all(characters)
db.commit()
db.close()
