"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Parcel


class ParcelDAO(GeneralDAO):
    """
    Realisation of Parcel data access layer.
    """
    _domain_type = Parcel

    def find_by_description(self, description: str) -> List[object]:
        """
        Gets Parcel objects from the database table by field 'description'.
        :param description: description value
        :return: search objects
        """
        return self._session.query(Parcel).filter(Parcel.description == description).order_by(Parcel.description).all()

    def find_by_weight(self, weight: str) -> List[object]:
        """
        Gets Parcel objects from the database table by field 'weight'.
        :param weight: weight value
        :return: search objects
        """
        return self._session.query(Parcel).filter(Parcel.weight == weight).order_by(Parcel.weight).all()

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Parcel objects from the database table by field 'status'.
        :param status: status value
        :return: search objects
        """
        return self._session.query(Parcel).filter(Parcel.status == status).order_by(Parcel.status).all()
