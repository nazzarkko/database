from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Day(db.Model, IDto):
    __tablename__ = "day"

    idday = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    day = db.Column(db.String(45), nullable=False)

    # Foreign key relationships
    dish = db.Column(db.Integer, db.ForeignKey("dish.iddish"), nullable=False)
    dish_data = db.relationship("Dish", backref=db.backref("day_data", lazy="dynamic"))

    nutritional_suplement = db.Column(db.Integer, db.ForeignKey("nutritional_suplement.idnutritional_suplements"),
                                      nullable=False)
    nutritional_suplement_data = db.relationship("NutritionalSupplement",
                                                 backref=db.backref("day_data", lazy="dynamic"))

    def __repr__(self) -> str:
        return f"Day({self.idday}, '{self.day}', {self.dish}, {self.nutritional_suplement})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idday": self.idday,
            "day": self.day,
            "dish": self.dish,
            "nutritional_suplement": self.nutritional_suplement,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Day:
        obj = Day(
            day=dto_dict.get("day"),
            dish=dto_dict.get("dish"),
            nutritional_suplement=dto_dict.get("nutritional_suplement"),
        )
        return obj
