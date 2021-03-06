from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin


class Favorite(TimeMixin, Base):  # type: ignore
    __tablename__ = "favorites"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="favorites", uselist=False)
    levelId = Column(Integer, ForeignKey("levels.id"))
    level = relationship("Level", back_populates="favorites", uselist=False)
