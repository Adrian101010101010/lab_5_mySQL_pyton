"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import regione_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class RegioneController(GeneralController):
    """
    Realisation of Regione controller.
    """
    _service = regione_service
