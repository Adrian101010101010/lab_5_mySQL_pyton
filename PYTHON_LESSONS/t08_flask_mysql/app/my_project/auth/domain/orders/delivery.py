"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Delivery(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "delivery"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    recipient = db.Column(db.String(45), nullable=False)
    cargo_volume = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Delivery({self.id}, '{self.recipient}', '{self.cargo_volume}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "recipient": self.recipient,
            "cargo_volume": self.cargo_volume,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Delivery:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Delivery(
            recipient=dto_dict.get("recipient"),
            cargo_volume=dto_dict.get("cargo_volume"),
        )
        return obj
