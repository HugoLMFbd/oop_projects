import db


class BillingManagement:

    def __init__(self, bill: object):
        self.bill_list = []
        self.bill = bill

    def paying_method(self):
        print('>>>>>Type a paying method<<<<<')
        print('| 1. CREDIT CARD || 2. GIFT CARD || 3. PAYPAL || 4. CASH')
        intp = int(input('>>>'))
        if intp == 1:
            self.bill.paying_method = 'CREDIT CARD'
            self.bill.bill_status = 'DONE'
            self.bill_list.append(self.bill)
        elif intp == 2:
            self.bill.paying_method = 'GIFT CARD'
            self.bill.bill_status = 'DONE'
            self.bill_list.append(self.bill)
        elif intp == 3:
            self.bill.paying_method = 'PAYPAL'
            self.bill.bill_status = 'DONE'
            self.bill_list.append(self.bill)
        elif intp == 4:
            self.bill.bill_status = 'DONE'
            self.bill_list.append(self.bill)
        else:
            print('Paying method not selected')
        return self.bill


class RentManagement:

    def __init__(self, partnermagnagement, clientmanagement):
        self.partner_management = partnermagnagement
        self.client_management = clientmanagement
        self.bill_list = []

    def rent(self):
        print('>>>>>>Available Bike(s)<<<<<<<<\n')
        [print(bike) for bike in self.bicycles_list() if bike.status == '**AVAILABLE**']
        Id = int(input('Type the ID of the bicycle you want to rent: '))
        name = input('Type your name>>')
        for bike in self.bicycles_list():
            if bike.bike_id == Id:
                for client in self.client_management.list_of_clients:
                    client.bike_rented = bike
                    if client.name == name:
                        bike.status = '**NOT AVAILABLE**'
                        bill = db.Bill(client, time_used=int)
                        client.own_bill = bill
                        self.bill_list.append(bill)

    def return_bicycle(self):
        name = input('Your name: ')
        for client in self.client_management.list_of_clients:
            if client.name == name:
                bike = client.bike_rented
                bike.status = '**AVAILABLE**'
                client.bike = 'No Bike'
                hours = float(input('Bike use in ours: '))
                bill = client.own_bill
                bill.bike_time_used = hours
                bill.total_to_pay = hours * 1.75
                pay_method = BillingManagement(bill)
                pay_method.paying_method()

                print(f'***YOUR BILL***\n{bill}')

    def bicycles_list(self) -> object:
        bikes = [partner.bike_own for partner in self.partner_management.list_of_partners]
        return bikes

    def bills_list(self) -> list:
        return self.bill_list

    def report(self) -> str:
        total = 0.0
        num_bills = 0
        for bill in self.bill_list:
            total += bill.total_to_pay
            num_bills += 1
        if total != 0:
            return f'The total incoming today: {total}\n Num of Clients Serverd Today: {num_bills}'
        else:
            return f'The bicycle has not yet been returned'


class ClientManagement:

    def __init__(self):
        self.list_of_clients = []

    def load_all_clients(self) -> object:
        list(self.list_of_clients.append(client) for client in db.clients)
        return self

    def search_client_by_index(self, index: int):
        self.load_all_clients()
        print(self.list_of_clients[index])

    def add_client(self, name: str, address: str, bike: object, Id: int):
        self.list_of_clients.append(db.Client(name, address, bike, Id))
        db.clients.append(db.Client(name, address, bike, Id))

    def remove_client(self, Id: int):
        self.load_all_clients()
        list(db.clients.remove(client) for client in db.clients if client.client_id == Id)

    def print_list_of_clients(self):
        self.load_all_clients()
        print(f'{self.list_of_clients}')


class PartnerManagement:

    def __init__(self):
        self.list_of_partners = []

    def load_all_partners(self) -> object:
        list(self.list_of_partners.append(partner) for partner in db.partners)
        return self

    def search_partner_by_index(self, index: int):
        self.load_all_partners()
        if index in range(len(self.list_of_partners)):
            print(self.list_of_partners[index])
        else:
            print('Out of Range')

    def add_partner(self, name: str, address: str, bike: object, new_id: int):
        self.list_of_partners.append(db.Partner(name, address, bike, new_id))
        db.partners.append(db.Partner(name, address, bike, new_id))

    def remove_partner(self, Id: int):
        self.load_all_partners()
        list(db.partners.remove(partner) for partner in db.partners if partner.partner_id == Id)

    def print_list_of_partners(self):
        self.load_all_partners()
        print(f'{self.list_of_partners}')
