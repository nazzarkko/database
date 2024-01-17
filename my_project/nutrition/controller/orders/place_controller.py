from my_project.nutrition.controller.general_controller import GeneralController
from my_project.nutrition.service import place_service


class PlaceController(GeneralController):
    _service = place_service

    def find_by_address(self, address: str):
        return self._service.find_by_address(address)
