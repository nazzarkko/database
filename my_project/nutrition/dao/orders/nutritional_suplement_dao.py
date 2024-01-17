from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import NutritionalSuplement


class NutritionalSupplementDAO(GeneralDAO):
    _domain_type = NutritionalSuplement

    def find_by_name(self, name: str) -> list[NutritionalSuplement]:
        session = self.get_session()
        supplements = session.query(NutritionalSuplement).filter(NutritionalSuplement.name == name).order_by(
            NutritionalSuplement.name
        ).all()
        return [supplement.put_into_dto() for supplement in supplements]

    def get_supplements_by_effect(self, effect: str) -> list[NutritionalSuplement]:
        session = self.get_session()
        supplements = session.query(NutritionalSuplement).filter(NutritionalSuplement.effect == effect).order_by(
            NutritionalSuplement.name
        ).all()
        return [supplement.put_into_dto() for supplement in supplements]
