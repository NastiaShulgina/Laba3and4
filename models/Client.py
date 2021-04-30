from models import Customer, Services


class Client(Customer):
    def __init__(self, full_name: str, sex: str, age: int, services: Services,
                 price_limit: int, needed_services=list):
        super().__init__(full_name, sex, age, services)
        self.price_limit = price_limit
        self.needed_services = needed_services

    def __str__(self):
        return f"Full name: {self.full_name}\nSex: {self.sex}\nAge: {self.age}\nServices: {self.services}\n\
        Price limit: {self.price_limit}\nNeeded services: {self.needed_services}\n"
