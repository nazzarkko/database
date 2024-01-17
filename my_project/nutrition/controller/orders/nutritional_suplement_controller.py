from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import nutritional_suplement_service


class NutritionalSuplementController(GeneralController):
    _service = nutritional_suplement_service
