from my_project.nutrition.dao.orders import sportsmen_dao
from my_project.nutrition.service.general_service import GeneralService

class SportsmenService(GeneralService):
    _dao = sportsmen_dao

    def find_by_sport(self, sport_id: int):
        return self._dao.find_by_sport(sport_id)

    def find_by_competitions_past(self, competitions_past_id: int):
        return self._dao.find_by_competitions_past(competitions_past_id)
