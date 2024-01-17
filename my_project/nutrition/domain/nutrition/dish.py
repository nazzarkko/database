from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Dish(db.Model, IDto):
    __tablename__ = "dish"

    iddish = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Dish({self.iddish}, '{self.name}', {self.calories})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "iddish": self.iddish,
            "name": self.name,
            "calories": self.calories,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Dish:
        obj = Dish(
            name=dto_dict.get("name"),
            calories=dto_dict.get("calories"),
        )
        return obj
