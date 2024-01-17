from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Sportsmen(db.Model, IDto):
    __tablename__ = "sportsmen"

    idsportsmen = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    sport = db.Column(db.Integer, db.ForeignKey("sport.idsport"), nullable=False)
    height = db.Column(db.DECIMAL(5, 2), nullable=False)
    weight = db.Column(db.DECIMAL(4, 1), nullable=False)
    competitions_past = db.Column(db.Integer, db.ForeignKey("competition_past.idcompetitions_past"), nullable=False)

    def __repr__(self) -> str:
        return f"Sportsmen({self.idsportsmen}, '{self.name}', '{self.surname}', {self.sport}, {self.height}, {self.weight}, {self.competitions_past})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idsportsmen": self.idsportsmen,
            "name": self.name,
            "surname": self.surname,
            "sport": self.sport,
            "height": float(self.height),
            "weight": float(self.weight),
            "competitions_past": self.competitions_past,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Sportsmen:
        obj = Sportsmen(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            sport=dto_dict.get("sport"),
            height=dto_dict.get("height"),
            weight=dto_dict.get("weight"),
            competitions_past=dto_dict.get("competitions_past"),
        )
        return obj
