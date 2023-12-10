"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class PostOffice(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "post_office"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    number = db.Column(db.String(45), nullable=False)
    users = db.relationship('User', backref='post_office', lazy=True)

    def __repr__(self) -> str:
        return f"Post_office({self.id}, '{self.number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without a relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "number": self.number,
            "users": [user.put_into_dto() for user in self.users],
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Post_office:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Post_office(
            number=dto_dict.get("number"),
        )
        return obj
