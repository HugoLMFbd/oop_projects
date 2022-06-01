class Bill:

    def __init__(self, bike, hours):
        self.amount_pay = None
        self.bike = bike
        self.hours = hours
        self.total_bills = []

    def print(self):
        return print(f'{self.amount_pay}')

    def total_per_hour(self):
        self.amount_pay = self.hours * 1.75
        self.total_bills.append(self.amount_pay)

    def print_all_bills(self):
        for bill in self.total_bills:
            print(bill)

    def total_per_day(self):
        day = self.hours / 24
        if day < 1:
            self.amount_pay = self.hours * 1.75
            self.total_bills.append(self.amount_pay)
        elif day > 0.99:
            self.amount_pay = day * 30
            self.total_bills.append(self.amount_pay)




