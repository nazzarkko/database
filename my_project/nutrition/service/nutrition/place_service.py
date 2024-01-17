from my_project.nutrition.dao.orders import place_dao
from my_project.nutrition.service.general_service import GeneralService

class PlaceService(GeneralService):
    _dao = place_dao
