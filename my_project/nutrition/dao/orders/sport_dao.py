from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Sport


class SportDAO(GeneralDAO):
    _domain_type = Sport

    def find_by_name(self, name: str) -> list[Sport]:
        session = self.get_session()
        sports = session.query(Sport).filter(Sport.name == name).order_by(Sport.name).all()
        return [sport.put_into_dto() for sport in sports]

    def get_sports_by_team(self, team: str) -> list[Sport]:
        session = self.get_session()
        sports = session.query(Sport).filter(Sport.team == team).order_by(Sport.name).all()
        return [sport.put_into_dto() for sport in sports]
