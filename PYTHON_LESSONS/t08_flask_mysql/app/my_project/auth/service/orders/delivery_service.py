"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import delivery_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DeliveryService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = delivery_dao

    def callGetMaxCargo(self):
        result = self._dao.callGetMaxCargo()
        return result
