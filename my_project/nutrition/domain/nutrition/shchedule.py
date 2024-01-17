from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Shchedule(db.Model, IDto):
    __tablename__ = "shchedule"

    idshcedule = db.Column(db.Integer, primary_key=True, nullable=False)
    day = db.Column(db.Integer, db.ForeignKey("day.idday"), nullable=False)
    sportsmen = db.Column(db.Integer, db.ForeignKey("sportsmen.idsportsmen"), nullable=False)

    def __repr__(self) -> str:
        return f"Shchedule({self.idshcedule}, {self.day}, {self.sportsmen})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idshcedule": self.idshcedule,
            "day": self.day,
            "sportsmen": self.sportsmen,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Shchedule:
        obj = Shchedule(
            day=dto_dict.get("day"),
            sportsmen=dto_dict.get("sportsmen"),
        )
        return obj
