from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import competition_past_service


class CompetitionPastController(GeneralController):
    _service = competition_past_service

    def find_by_place(self, place_id: int):

        return self._service.find_by_place(place_id)
