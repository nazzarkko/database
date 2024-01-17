from abc import ABC, abstractmethod
from typing import Dict


class IDto(ABC):
    """
    Interface to put and extract DTO objects to/from domain objects.
    """

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

    @classmethod
    @abstractmethod
    def create_from_dto(cls, dto_dict: Dict[str, object]) -> object:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
