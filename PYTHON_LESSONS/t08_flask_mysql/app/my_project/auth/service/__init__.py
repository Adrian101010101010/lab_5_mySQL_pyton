"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.client_service import ClientService
from .orders.client_type_service import ClientTypeService
from .orders.city_service import CityService
from .orders.courier_has_delivery_service import CourierHasDeliveryService
from .orders.parcel_has_courier_service import ParcelHasCourierService
from .orders.operator_service import OperatorService
from .orders.department_service import DepartmentService
from .orders.regione_service import RegioneService
from .orders.parcel_service import ParcelService
from .orders.delivery_service import DeliveryService
from .orders.courier_service import CourierService
from .orders.user_service import UserService
from .orders.post_office_service import PostOfficeService

client_service = ClientService()
client_type_service = ClientTypeService()
city_service = CityService()
courier_has_delivery_service = CourierHasDeliveryService()
parcel_has_courier_service = ParcelHasCourierService()
operator_service = OperatorService()
department_service = DepartmentService()
regione_service = RegioneService()
parcel_service = ParcelService()
delivery_service = DeliveryService()
courier_service = CourierService()
user_service = UserService()
post_office_service = PostOfficeService()
