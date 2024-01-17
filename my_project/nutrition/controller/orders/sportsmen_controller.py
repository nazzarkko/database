from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import sportsmen_service


class SportsmenController(GeneralController):
    _service = sportsmen_service

    def find_by_sport(self, sport_id: int):
        return self._service.find_by_sport(sport_id)

    def find_by_competitions_past(self, competitions_past_id: int):
        return self._service.find_by_competitions_past(competitions_past_id)
