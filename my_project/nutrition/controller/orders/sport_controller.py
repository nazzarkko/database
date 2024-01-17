from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import sport_service


class SportController(GeneralController):
    _service = sport_service

    def find_by_team(self, team_name: str):
        return self._service.find_by_team(team_name)
