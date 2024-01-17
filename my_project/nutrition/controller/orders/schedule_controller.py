from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import shchedule_service


class ShcheduleController(GeneralController):
    _service = shchedule_service

    def find_by_day(self, day_id: int):
        return self._service.find_by_day(day_id)

    def find_by_sportsmen(self, sportsmen_id: int):
        return self._service.find_by_sportsmen(sportsmen_id)
