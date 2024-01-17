from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class NutritionalSuplement(db.Model, IDto):
    __tablename__ = "nutritional_suplement"

    idnutritional_suplements = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    effect = db.Column(db.String(100), nullable=False)
    period_of_using_in_month = db.Column(db.Integer, nullable=False)
    count_of_day = db.Column(db.Integer, nullable=False)
    main_component = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"NutritionalSupplement({self.idnutritional_suplements}, '{self.name}', '{self.description}', " \
               f"'{self.effect}', {self.period_of_using_in_month}, {self.count_of_day}, '{self.main_component}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idnutritional_suplements": self.idnutritional_suplements,
            "name": self.name,
            "description": self.description,
            "effect": self.effect,
            "period_of_using_in_month": self.period_of_using_in_month,
            "count_of_day": self.count_of_day,
            "main_component": self.main_component,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> NutritionalSuplement:
        obj = NutritionalSuplement(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            effect=dto_dict.get("effect"),
            period_of_using_in_month=dto_dict.get("period_of_using_in_month"),
            count_of_day=dto_dict.get("count_of_day"),
            main_component=dto_dict.get("main_component"),
        )
        return obj
