from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import dish_service


class DishController(GeneralController):
    _service = dish_service
