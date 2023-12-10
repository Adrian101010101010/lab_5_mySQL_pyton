"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.client_controller import ClientController
from .orders.client_type_controller import ClientTypeController
from .orders.city_controller import CityController
from .orders.courier_controller import CourierController
from .orders.courier_has_delivery_controller import CourierHasDeliveryController
from .orders.delivery_controller import DeliveryController
from .orders.department_controller import DepartmentController
from .orders.operator_controller import OperatorController
from .orders.parcel_controller import ParcelController
from .orders.parcel_has_courier_controller import ParcelHasCourierController
from .orders.regione_controller import RegioneController
from .orders.user_controller import UserController
from .orders.post_office_controller import PostOfficeController

client_controller = ClientController()
client_type_controller = ClientTypeController()
city_controller = CityController()
courier_controller = CourierController()
courier_has_delivery_controller = CourierHasDeliveryController()
delivery_controller = DeliveryController()
department_controller = DepartmentController()
operator_controller = OperatorController()
parcel_controller = ParcelController()
parcel_has_courier_controller = ParcelHasCourierController()
regione_controller = RegioneController()
user_controller = UserController()
post_office_controller = PostOfficeController()
