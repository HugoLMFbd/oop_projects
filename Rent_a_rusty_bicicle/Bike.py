class Bike:

    def __init__(self, bike_name, age, type):
        self.bike_name = bike_name
        self.age = age
        self.type = type
        self.available = True


class Management(Bike):

    def __init__(self, bike_name, age, type):
        self.bike_list = []
        super().__init__(bike_name, age, type)
        self.bike_name = bike_name
        self.age = age

    def change_availability(self):
        if self.available:
            self.available = False
        else:
            self.available = True
