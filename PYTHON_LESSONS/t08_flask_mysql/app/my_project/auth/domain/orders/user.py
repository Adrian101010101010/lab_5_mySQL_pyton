"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    place_of_delivery = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"User({self.id}, '{self.name}', '{self.surname}', '{self.phone}', '{self.birthday}', '{self.place_of_delivery}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "birthday": str(self.birthday),
            "place_of_delivery": self.place_of_delivery,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = User(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phone=dto_dict.get("phone"),
            birthday=dto_dict.get("birthday"),
            place_of_delivery=dto_dict.get("place_of_delivery")
        )
        return obj
