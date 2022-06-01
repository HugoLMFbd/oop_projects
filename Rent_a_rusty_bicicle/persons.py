import db


class Person:

    def __init__(self, name, bike):
        self.name = name
        self.bike_rented = bike
        self.renter = bool


class Client(Person):
    def __init__(self, name, bike: object):
        super().__init__(name, bike)
        self.renter = None
        self.bike_rented = bike

        if self.renter is None and bike.name in db.bikes.name:
            if Partner().rent_:
                self.renter = True
        else:
            self.renter = False


class Partner(Person):

    def __init__(self, name, client: object, own_bike: object):
        super().__init__(name, own_bike)
        self.bike_rented = False
        self.own_bike = own_bike
        self.renter = client

    def rent_(self):
        if self.renter.renter:
            self.bike_rented = True
        else:
            self.bike_rented = False
