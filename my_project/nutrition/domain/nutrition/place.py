from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class Place(db.Model, IDto):
    __tablename__ = "place"

    idplace = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    adress = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Place({self.idplace}, '{self.name}', '{self.adress}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idplace": self.idplace,
            "name": self.name,
            "adress": self.adress,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Place:
        obj = Place(
            name=dto_dict.get("name"),
            adress=dto_dict.get("adress"),
        )
        return obj
