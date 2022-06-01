# Fill out the list with objects, not dictionaries
# ex.
# some_list = [Client("SomeValue, 1, "SomeOtherValue"), Client("SomeoneElse" ...
from persons import Client, Partner
from Bike import Bike

# Bikes

bike1 = Bike('yamaha', 7, 'standard')
bike2 = Bike('Colnago', 5, 'motored')
# Clients

angela = Client('Angela',bike1)
stuart = Client('Stuart', bike2)
ines = Client('Ines', bike1)
# Partner

andrea = Partner('Andrea', stuart, bike2)
samuel = Partner('Samuel', ines, bike1)

# Lists
clients = [angela, stuart, ines]

partners = [samuel, andrea]

bikes = [bike1, bike2]
