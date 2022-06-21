from datetime import datetime
from uuid import uuid1
from datetime import date
from pydantic import BaseModel


class Bill:

    def __init__(self, bike: object, hours):
        self.date = date.today()
        self.bike = bike
        self.hours = hours
        self.amount_pay = None

    def __repr__(self):
        return f'{self.date}\n your rented bike: {self.bike}\n Total to pay: {self.amount_pay} '


class Bike(BaseModel):

    bike_id: int
    name: str
    years: str
    type: str
    status = '**AVAILABLE**'

    def __repr__(self):
        return f'ID: ->>{self.bike_id}<<- Bike name: {self.name} || Year of manufactured: {self.years} || ' \
               f'Type of Bike: {self.type}||' \
               f'Availability Status : {self.status}\n'

    def __str__(self):
        return f'ID: ->>{self.bike_id}<<- Bike name: {self.name} || Year of manufactured: {self.years} || ' \
               f'Type of Bike: {self.type}||' \
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
        return f'Partner Name: {self.name}\n{self.name}\'s Bike:  {self.bike_own.name}\nID: {self.partner_id}'

    def __str__(self) -> str:
        return f'Partner Name: {self.name}\n{self.name}\'s Bike:  {self.bike_own.name}\nID: {self.partner_id}'


class Bill_:

    def __init__(self, client_name: object, time_used: float):
        self.bill_day_of_issue = datetime.now()
        self.client_name = client_name.name
        self.bike_rented = client_name.bike_rented.name
        self.bill_status = 'PENDING'
        self.paying_method = 'CASH'
        self.bike_time_used = time_used
        self.total_to_pay = time_used * 1.75

    def __repr__(self) -> str:
        return f'{"_" * 30}\nDate:     {self.bill_day_of_issue}\n{"-" * 30}\nClient Name: {self.client_name}' \
               f'\nYou rented bike ' \
               f'name: {self.bike_rented} STATUS: {self.bill_status}\n{"-" * 30}\nPaying_method: ' \
               f'{self.paying_method} TOTAL: {self.total_to_pay}€' \
               f'\n{"_" * 30}'

    def __str__(self) -> str:
        return f'{"_" * 30}\nDate:\n     {self.bill_day_of_issue}\n{"-" * 30}\nClient Name: ' \
               f'{self.client_name}\nYou rented bike ' \
               f'name: {self.bike_rented}\n{"-" * 30}\nPaying_method: {self.paying_method} TOTAL: ' \
               f'{self.total_to_pay}€\n{"_" * 30}'


class IdGenerator:
    def __init__(self):
        self.key = uuid1().version
        self.gen_id_num()

    def __repr__(self) -> str:
        return f'{self.id_number}'

    def __str__(self) -> str:
        return f'{self.id_number}'

    def gen_id_num(self) -> int:
        return self.key + 1
    # Todo try to generated an sort Ids


class BillMethods(Bill_):

    def __init__(self, bike: object, hours):
        super().__init__(bike, hours)
        self.total_bills = []

    def print_all_bills(self):
        for bill in self.total_bills:
            print(bill)

    def total_per_day_or_per_hours(self):
        day = self.hours / 24
        if day < 1:
            self.amount_pay = self.hours * 1.75
            self.total_bills.append(self.amount_pay)
            print('Calculating per hour...')
            self.print_total_cost()
        elif day > 0.99:
            self.amount_pay = day * 30
            self.total_bills.append(self.amount_pay)
            print('Calculating per day...')
            self.print_total_cost()

    def print_total_cost(self):
        if self.amount_pay is None:
            raise Exception('Have to calculate Total_per_day_or_per_hour')
        else:
            return print(f'{self.amount_pay}')

    def __repr__(self):
        super().__repr__()
