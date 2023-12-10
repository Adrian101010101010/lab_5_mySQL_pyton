"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "city"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"City({self.id}, '{self.city_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "city_name": self.city_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = City(
            city_name=dto_dict.get("city_name"),
        )
        return obj
