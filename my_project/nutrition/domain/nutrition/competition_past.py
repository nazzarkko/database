from __future__ import annotations

from my_project import db
from my_project.nutrition.domain.i_dto import IDto


class CompetitionPast(db.Model, IDto):
    __tablename__ = "competition_past"

    idcompetitions_past = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    year = db.Column(db.String(45), nullable=False)

    # Foreign key relationship
    place = db.Column(db.Integer, db.ForeignKey("place.idplace"), nullable=False)
    place_data = db.relationship("Place", backref=db.backref("competition_past_data", lazy="dynamic"))

    def __repr__(self) -> str:
        return f"CompetitionPast({self.idcompetitions_past}, '{self.name}', '{self.year}', {self.place})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "idcompetitions_past": self.idcompetitions_past,
            "name": self.name,
            "year": self.year,
            "place": self.place,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> CompetitionPast:
        obj = CompetitionPast(
            name=dto_dict.get("name"),
            year=dto_dict.get("year"),
            place=dto_dict.get("place"),
        )
        return obj
