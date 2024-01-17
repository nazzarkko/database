from my_project.nutrition.dao.orders import sport_dao
from my_project.nutrition.service.general_service import GeneralService

class SportService(GeneralService):
    _dao = sport_dao

    def find_by_team(self, team_name: str):
        return self._dao.find_by_team(team_name)
