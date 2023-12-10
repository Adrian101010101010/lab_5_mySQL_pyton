"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List, Dict

from t08_flask_mysql.app.my_project.auth.service import courier_has_delivery_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CourierHasDeliveryController(GeneralController):
    """
    Realisation of CourierHasDelivery controller.
    """
    _service = courier_has_delivery_service

    def find_deliveries_by_courier(self, delivery_id: int) -> List[Dict[str, object]]:
        """
                    Finds libraries associated with a specific user by user_id.
                    :param user_id: ID of the user
                    :return: List of libraries associated with the user
                    """
        return list(map(lambda x: x.put_into_dto(), self._service.find_deliveries_by_courier(delivery_id)))

    def insert_into_docking_table_courier_has_delivery(self, corier_name, corier_phone, delivery_recipient):
         result = self._service.insert_into_docking_table_courier_has_delivery(corier_name, corier_phone, delivery_recipient)
         return result
