from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    nationality = Column(String)

    characters = relationship("Character", back_populates="actor")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    description = Column(String)
    category = Column(String)  # Demon Lord, Former, Other

    actor_id = Column(Integer, ForeignKey("actors.id"))
    actor = relationship("Actor", back_populates="characters")
