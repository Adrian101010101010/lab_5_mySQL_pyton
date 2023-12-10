"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Delivery
from sqlalchemy import text

class DeliveryDAO(GeneralDAO):
    """
    Realisation of Delivery data access layer.
    """
    _domain_type = Delivery

    def find_by_recipient(self, recipient: str) -> List[object]:
        """
        Gets Delivery objects from the database table by field 'recipient'.
        :param recipient: recipient value
        :return: search objects
        """
        return self._session.query(Delivery).filter(Delivery.recipient == recipient).order_by(Delivery.recipient).all()

    def find_by_cargo_volume(self, cargo_volume: str) -> List[object]:
        """
        Gets Delivery objects from the database table by field 'cargo_volume'.
        :param cargo_volume: cargo_volume value
        :return: search objects
        """
        return self._session.query(Delivery).filter(Delivery.cargo_volume == cargo_volume).order_by(Delivery.cargo_volume).all()

    def callGetMaxCargo(self):
        try:
            result = self._session.execute(text("CALL callGetMaxCargo()"))
            return result.scalar()
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
