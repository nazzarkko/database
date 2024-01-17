from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Place


class PlaceDAO(GeneralDAO):
    _domain_type = Place

    def find_by_name(self, name: str) -> list[Place]:
        session = self.get_session()
        places = session.query(Place).filter(Place.name == name).order_by(Place.name).all()
        return [place.put_into_dto() for place in places]
