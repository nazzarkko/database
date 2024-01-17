from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Sport(db.Model, IDto):
    __tablename__ = "sport"

    idsport = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    team = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Sport({self.idsport}, '{self.name}', '{self.team}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idsport": self.idsport,
            "name": self.name,
            "team": self.team,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Sport:
        obj = Sport(
            name=dto_dict.get("name"),
            team=dto_dict.get("team"),
        )
        return obj
