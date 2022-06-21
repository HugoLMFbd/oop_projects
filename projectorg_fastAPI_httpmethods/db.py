from models import Bike
from models import Client
from models import Partner
from models import Bill_

# Bikes

bike1 = Bike(name='Yamaha', years='2001', type='standard', bike_id=123)
bike2 = Bike(name='Colnago', years='2019', type='motored', bike_id=321)

# Clients

angela = Client('Angela', 'Rathausstr 3', bike1, 1)
stuart = Client('Stuart', 'Kalerhautstr. 11', bike2, 2)
ines = Client('Ines', 'Grünerweg. 22', bike1, 3)

# Partner

andrea = Partner('Andrea', 'Standoriastr. 4', bike2, 11)
samuel = Partner('Samuel', 'Elliferstr. 23', bike1, 12)

# Bills
bill1 = Bill_(angela, 24)
bill2 = Bill_(stuart, 51)

# Lists

clients = [angela, stuart, ines]
partners = [samuel, andrea]
bikes = [bike1, bike2]
bills = [bill1, bill2]
