from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import day_service


class DayController(GeneralController):
    _service = day_service

    def find_by_dish(self, dish_id: int):
        return self._service.find_by_dish(dish_id)

    def find_by_nutritional_suplement(self, nutritional_suplement_id: int):
        return self._service.find_by_nutritional_suplement(nutritional_suplement_id)
