from controllers import PartnerManagement
from controllers import ClientManagement
from controllers import RentManagement


def main_menu():
    print("1. Rent a Bike")
    print("2. Return a Bike")
    print("3. List Bikes")
    print("4. List Bills")
    print("5. Incoming Report")
    print("0. Exit")
    opt = int(input("Type an option >> "))
    return opt


if __name__ == '__main__':
    partners_management = PartnerManagement().load_all_partners()
    clients_management = ClientManagement().load_all_clients()
    rent_management = RentManagement(partners_management, clients_management)

    option = -1
    while option != 0:

        option = main_menu()
        if option == 1:
            rent_management.rent()
        elif option == 2:
            rent_management.return_bicycle()
        if option == 3:
            print(rent_management.bicycles_list())
        elif option == 4:
            print(rent_management.bills_list())
        elif option == 5:
            print(rent_management.report())
