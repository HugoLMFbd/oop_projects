from datetime import datetime


class Bike:

    def __init__(self, name: str, years: str, tYpe: str, Id: int):
        self.bike_id = Id
        self.name = name
        self.years = years
        self.type = tYpe
        self.status = '**AVAILABLE**'

    def __repr__(self):
        return f'ID: ->>{self.bike_id}<<- Bike name: {self.name} || Year of manufactured: {self.years} || Type of Bike: {self.type}||' \
               f'Availability Status : {self.status}\n'

    def __str__(self):
        return f'ID: ->>{self.bike_id}<<- Bike name: {self.name} || Year of manufactured: {self.years} || Type of Bike: {self.type}||' \
               f'Availability Status : {self.status}\n{"-" * 25} '


class Person:

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


class Client(Person):
    def __init__(self, name: str, address: str, bike: object, client_id: int):
        super().__init__(name, address)
        self.bike_rented = bike
        self.client_id = client_id
        self.own_bill = object

    def __repr__(self):
        return f'Client name: {self.name}\n{self.bike_rented}\n ID: {self.client_id}'

    def __str__(self):
        return f'Client name: {self.name}\nRented Bike:  {self.bike_rented}\nID: {self.client_id}'


class Partner(Person):

    def __init__(self, name: str, address: str, bike: object, Id):
        self.partner_id = Id
        self.bike_own = bike
        super().__init__(name, address)

    def __repr__(self) -> str:
        return f'Partner Name: {self.name}\n{self.name}\'s Bike:  {self.bike_own}\nID: {self.partner_id}'

    def __str__(self) -> str:
        return f'Partner Name: {self.name}\n{self.name}\'s Bike:  {self.bike_own}\nID: {self.partner_id}'


class Bill:

    def __init__(self, client_name: object, time_used: float):
        self.bill_day_of_issue = datetime.now()
        self.client_name = client_name.name
        self.bike_rented = client_name.bike_rented.name
        self.bill_status = 'PENDING'
        self.paying_method = 'CASH'
        self.bike_time_used = time_used
        self.total_to_pay = 0.0

    def __repr__(self) -> str:
        return f'{"_"*30}\nDate:     {self.bill_day_of_issue}\n{"-" * 30}\nClient Name: {self.client_name}\nYou rented bike ' \
               f'name: {self.bike_rented} STATUS: {self.bill_status}\n{"-" * 30}\nPaying_method: {self.paying_method} TOTAL: {self.total_to_pay}€' \
               f'\n{"_"*30}'

    def __str__(self) -> str:
        return f'{"_"*30}\nDate:\n     {self.bill_day_of_issue}\n{"-" * 30}\nClient Name: {self.client_name}\nYou rented bike ' \
               f'name: {self.bike_rented}\n{"-" * 30}\nPaying_method: {self.paying_method} TOTAL: {self.total_to_pay}€' \
               f'\n{"_"*30}'


# Bikes

bike1 = Bike('Yamaha', '2001', 'standard', 123)
bike2 = Bike('Colnago', '2019', 'motored', 321)

# Clients

angela = Client('Angela', 'Rathausstr 3', bike1, 1)
stuart = Client('Stuart', 'Kalerhautstr. 11', bike2, 2)
ines = Client('Ines', 'Grünerweg. 22', bike1, 3)

# Partner

andrea = Partner('Andrea', 'Standoriastr. 4', bike2, 11)
samuel = Partner('Samuel', 'Elliferstr. 23', bike1, 12)

# Lists

clients = [angela, stuart, ines]
partners = [samuel, andrea]
bikes = [bike1, bike2]
