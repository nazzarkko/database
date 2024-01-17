from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Sportsmen


class SportsmenDAO(GeneralDAO):
    _domain_type = Sportsmen

    def find_by_name(self, name: str) -> list[Sportsmen]:
        session = self.get_session()
        athletes = session.query(Sportsmen).filter(Sportsmen.name == name).order_by(Sportsmen.name).all()
        return [athlete.put_into_dto() for athlete in athletes]

    def get_athletes_by_sport(self, sport_id: int) -> list[Sportsmen]:
        session = self.get_session()
        athletes = session.query(Sportsmen).filter(Sportsmen.sport == sport_id).order_by(Sportsmen.name).all()
        return [athlete.put_into_dto() for athlete in athletes]
