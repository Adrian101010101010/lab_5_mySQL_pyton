"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Regione(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "regione"

    name = db.Column(db.String(50), primary_key=True)

    def __repr__(self) -> str:
        return f"Regione('{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Regione:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Regione(
            name=dto_dict.get("name"),
        )
        return obj
