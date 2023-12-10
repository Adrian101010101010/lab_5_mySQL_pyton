"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Department(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(45), nullable=False)
    number = db.Column(db.String(45), nullable=False)
    contacts = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Department({self.id}, '{self.location}', '{self.number}', '{self.contacts}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "location": self.location,
            "number": self.number,
            "contacts": self.contacts,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Department:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Department(
            location=dto_dict.get("location"),
            number=dto_dict.get("number"),
            contacts=dto_dict.get("contacts"),
        )
        return obj
 