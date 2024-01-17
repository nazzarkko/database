from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Trainer(db.Model, IDto):
    __tablename__ = "trainer"

    idtrainers = db.Column(db.Integer, primary_key=True, nullable=False)
    sport = db.Column(db.Integer, db.ForeignKey("sport.idsport"), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    sportsmen = db.Column(db.Integer, db.ForeignKey("sportsmen.idsportsmen"), nullable=False)

    def __repr__(self) -> str:
        return f"Trainer({self.idtrainers}, {self.sport}, '{self.name}', '{self.surname}', {self.sportsmen})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idtrainers": self.idtrainers,
            "sport": self.sport,
            "name": self.name,
            "surname": self.surname,
            "sportsmen": self.sportsmen,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Trainer:
        obj = Trainer(
            sport=dto_dict.get("sport"),
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            sportsmen=dto_dict.get("sportsmen"),
        )
        return obj
