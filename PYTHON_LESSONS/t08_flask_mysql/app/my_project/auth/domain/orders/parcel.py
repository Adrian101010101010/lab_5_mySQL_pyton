"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Parcel(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "parcel"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    description = db.Column(db.String(45), nullable=False)
    weight = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Parcel({self.id}, '{self.description}', '{self.weight}', '{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "description": self.description,
            "weight": self.weight,
            "status": self.status,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Parcel:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Parcel(
            description=dto_dict.get("description"),
            weight=dto_dict.get("weight"),
            status=dto_dict.get("status"),
        )
        return obj
