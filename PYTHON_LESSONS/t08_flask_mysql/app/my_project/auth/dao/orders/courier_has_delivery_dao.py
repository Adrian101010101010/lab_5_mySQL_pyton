"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import CourierHasDelivery
from sqlalchemy import text

class CourierHasDeliveryDAO(GeneralDAO):
    """
    Realisation of CourierHasDelivery data access layer.
    """
    _domain_type = CourierHasDelivery

    def find_by_courier_id(self, courier_id: int) -> List[object]:
        """
        Gets CourierHasDelivery objects from the database table by field 'courier_id'.
        :param courier_id: courier_id value
        :return: search objects
        """
        return self._session.query(CourierHasDelivery).filter(CourierHasDelivery.courier_id == courier_id).all()

    def find_by_delivery_id(self, delivery_id: int) -> List[object]:
        """
        Gets CourierHasDelivery objects from the database table by field 'delivery_id'.
        :param delivery_id: delivery_id value
        :return: search objects
        """
        return self._session.query(CourierHasDelivery).filter(CourierHasDelivery.delivery_id == delivery_id).all()

    def insert_into_docking_table_courier_has_delivery(self, courier_has_delivery_corier_name,
                                                       courier_has_delivery_corier_phone,
                                                       courier_has_delivery_delivery_recipient):
        try:
            self._session.execute(text(
                f"CALL insert_into_docking_table_courier_has_delivery('{courier_has_delivery_corier_name}',"
                f" '{courier_has_delivery_corier_phone}', '{courier_has_delivery_delivery_recipient}')",
            ))
            self._session.commit()
            return "insert_into_docking_table_courier_has_delivery OK"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
