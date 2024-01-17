from my_project.nutrition.dao.orders import nutritional_suplement_dao
from my_project.nutrition.service.general_service import GeneralService

class NutritionalSuplementService(GeneralService):
    _dao = nutritional_suplement_dao
