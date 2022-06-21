import controllers as con
from fastapi import APIRouter

import db
from models import Bike

rusty_bikes_routes = APIRouter()
partners_controller = con.PartnerManagement().load_all_partners()
clients_controller = con.ClientManagement().load_all_clients()
rent_controller = con.RentManagement(partners_controller, clients_controller)


@rusty_bikes_routes.get('/bikes')
def get_bike():
    db.load_bikes()
    return rent_controller.bicycles_list()


@rusty_bikes_routes.get('/clients')
def get_client():
    return rent_controller.clients_list()


@rusty_bikes_routes.post('/bikes')
def post_bike(bike: Bike):
    rent_controller.add_bike(bike)


@rusty_bikes_routes.get('/bills')
def get_bill():
    return rent_controller.bills_list()


@rusty_bikes_routes.delete('/bikes/{id_}')
def delete_bike(Id: int):
    rent_controller.remove_bike_id(Id)
