from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import CompetitionPast


class CompetitionPastDAO(GeneralDAO):
    _domain_type = CompetitionPast

    def find_by_name(self, name: str) -> list[CompetitionPast]:
        session = self.get_session()
        competitions = session.query(CompetitionPast).filter(CompetitionPast.name == name).order_by(
            CompetitionPast.name
        ).all()
        return [competition.put_into_dto() for competition in competitions]

    def get_competitions_by_year(self, year: str) -> list[CompetitionPast]:
        session = self.get_session()
        competitions = session.query(CompetitionPast).filter(CompetitionPast.year == year).order_by(
            CompetitionPast.name
        ).all()
        return [competition.put_into_dto() for competition in competitions]
