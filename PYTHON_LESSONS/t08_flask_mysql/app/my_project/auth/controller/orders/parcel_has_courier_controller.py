"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List, Dict

from t08_flask_mysql.app.my_project.auth.service import parcel_has_courier_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ParcelHasCourierController(GeneralController):
    """
    Realisation of  ParcelHasCourier controller.
    """
    _service = parcel_has_courier_service

    def find_parcels_by_courier(self, courier_id: int) -> List[Dict[str, object]]:
        """
                    Finds libraries associated with a specific user by user_id.
                    :param user_id: ID of the user
                    :return: List of libraries associated with the user
                    """
        return list(map(lambda x: x.put_into_dto(), self._service.find_parcels_by_courier(courier_id)))
