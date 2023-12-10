"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Courier(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "courier"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    surname = db.Column(db.String(45))
    phone = db.Column(db.String(45))
    birthday = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Courier({self.id}, '{self.name}', '{self.surname}', '{self.phone}', '{self.birthday}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "birthday": str(self.birthday),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Courier:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Courier(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phone=dto_dict.get("phone"),
            birthday=dto_dict.get("birthday"),
        )
        return obj
