"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import delivery_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class DeliveryController(GeneralController):
    """
    Realisation of Delivery controller.
    """
    _service = delivery_service


    def callGetMaxCargo(self):
        result = self._service.callGetMaxCargo()
        return result
