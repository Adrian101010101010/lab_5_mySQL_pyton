"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import ParcelHasCourier


class ParcelHasCourierDAO(GeneralDAO):
    """
    Realisation of ParcelHasCourier data access layer.
    """
    _domain_type = ParcelHasCourier

    def find_parcels_by_courier(self, courier_id: int) :
        """
                    Finds libraries associated with a specific user by user_id.
                    :param user_id: ID of the user
                    :return: List of libraries associated with the user
                    """
        return self._session.query(ParcelHasCourier).filter(ParcelHasCourier.courier_id == courier_id).all()


    def find_by_courier_id(self, courier_id: int) -> List[object]:
        """
        Gets ParcelHasCourier objects from the database table by field 'courier_id'.
        :param courier_id: courier_id value
        :return: search objects
        """
        return self._session.query(ParcelHasCourier).filter(ParcelHasCourier.courier_id == courier_id).all()

    def find_by_parcel_id(self, parcel_id: int) -> List[object]:
        """
        Gets ParcelHasCourier objects from the database table by field 'parcel_id'.
        :param parcel_id: parcel_id value
        :return: search objects
        """
        return self._session.query(ParcelHasCourier).filter(ParcelHasCourier.parcel_id == parcel_id).all()
