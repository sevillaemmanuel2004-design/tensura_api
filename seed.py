from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Character, Actor

Base.metadata.create_all(bind=engine)


def seed_data():
    db: Session = SessionLocal()

    # 🛑 Prevent duplicate seeding
    if db.query(Character).first():
        print("Database already seeded.")
        db.close()
        return

    # =====================
    # ACTORS
    # =====================
    actors = [
        Actor(name="Miho Okasaki", nationality="Japanese"),
        Actor(name="Rina Hidaka", nationality="Japanese"),
        Actor(name="Takahiro Sakurai", nationality="Japanese"),
        Actor(name="Yukari Tamura", nationality="Japanese"),
        Actor(name="Daisuke Ono", nationality="Japanese"),
    ]

    db.add_all(actors)
    db.commit()

    # Fetch actors safely
    actor_map = {a.name: a for a in db.query(Actor).all()}

    # =====================
    # CHARACTERS
    # =====================
    characters = [
        Character(
            name="Rimuru Tempest",
            title="New Demon Lord",
            description="A slime who becomes one of the strongest beings.",
            category="Demon Lord",
            actor_id=actor_map["Miho Okasaki"].id
        ),
        Character(
            name="Milim Nava",
            title="Destroyer",
            description="One of the oldest Demon Lords.",
            category="Demon Lord",
            actor_id=actor_map["Rina Hidaka"].id
        ),
        Character(
            name="Guy Crimson",
            title="Primordial Red",
            description="The strongest Demon Lord.",
            category="Demon Lord"
        ),
        Character(
            name="Ramiris",
            title="Labyrinth Queen",
            description="Controls labyrinths and reincarnation.",
            category="Demon Lord"
        ),
        Character(
            name="Leon Cromwell",
            title="Hero King",
            description="A Demon Lord tied to heroes.",
            category="Demon Lord"
        ),
        Character(
            name="Luminous Valentine",
            title="Vampire Queen",
            description="Rules life and death.",
            category="Demon Lord"
        ),
        Character(
            name="Dagruel",
            title="Titan King",
            description="Embodiment of strength.",
            category="Demon Lord"
        ),
        Character(
            name="Dino",
            title="Sleeping Demon Lord",
            description="Lazy but powerful.",
            category="Demon Lord"
        ),
        Character(
            name="Clayman",
            title="Manipulator",
            description="Defeated schemer.",
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
            description="Relinquishes title.",
            category="Former Demon Lord"
        ),
        Character(
            name="Diablo",
            title="Primordial Black",
            description="Rimuru’s most loyal subordinate.",
            category="Other"
        ),
    ]

    db.add_all(characters)
    db.commit()
    db.close()

    print("Seed completed successfully!")


if __name__ == "__main__":
    seed_data()
