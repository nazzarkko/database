from my_project.nutrition.dao.general_dao import GeneralDAO
from my_project.nutrition.domain import Trainer


class TrainerDAO(GeneralDAO):
    _domain_type = Trainer

    def find_by_name(self, name: str) -> list[Trainer]:
        session = self.get_session()
        trainers = session.query(Trainer).filter(Trainer.name == name).order_by(Trainer.name).all()
        return [trainer.put_into_dto() for trainer in trainers]

    def get_trainers_by_sport(self, sport_id: int) -> list[Trainer]:
        session = self.get_session()
        trainers = session.query(Trainer).filter(Trainer.sport == sport_id).order_by(Trainer.name).all()
        return [trainer.put_into_dto() for trainer in trainers]
