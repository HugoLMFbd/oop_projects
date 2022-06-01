from persons import Partner, Client
import Bike
import db

class Management:
    def __init__(self):
        self.bicycles_list = list
        self.bills_list = list
        self.report = list


    def add_bike_to_rented(self, bike):
        self.bicycles_list.append(bike)


class RentManagement(Management):
    def __init__(self):
        super().__init__()

    def rent_a_bike(self, bike, client):
        self.bicycles_list.append(bike)
        bike.change_availability()
        print(f'{client.name} You have rented a bike. Thank you! ')

    def return_a_bycke(self, bike):
        self.bicycles_list.remove(bike)
        bike.change_availability()
        print(f'The bike {bike} is returned to the store.')

    def print_list_of_bikes(self):
        print(self.bicycles_list)


class ClientManagement:

    def __init__(self):
        self.list_of_clients = self.load_clients()

    @staticmethod
    def load_clients():
        for client in db.clients:
            return client

    def find_client(self, client):
        client.load_clients()
        for cl in self.list_of_clients:
            if client == cl:
                print(client)



class PartnerManagement():
    def __init__(self):
        self.partner_list = []

    def add_partner(self, name, client, bike: object):
        self.partner_list.append(Partner(name, client, bike))


