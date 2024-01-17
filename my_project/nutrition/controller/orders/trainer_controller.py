from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import trainer_service


class TrainerController(GeneralController):
    _service = trainer_service

    def find_by_sportsmen(self, sportsmen_id: int):
        return self._service.find_by_sportsmen(sportsmen_id)
