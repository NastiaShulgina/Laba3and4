from enum import Enum

class Services(Enum):
    COMPANY_REGISTRATION = 0
    PROVIDING_CONSULTATION = 1
    BUSINESS_PAPERS_PREPARATION = 2
    FIRM_RESALE_GUARANTEE = 3
    ASSISTANCE_IN_REAL_ESTATE_TRANSACTIONS = 4
    APPLICATION_REGISTRATION = 5
    COPYRIGHT_REGISTRATION_AND_PROTECTION = 6
    CONSULTATION = 7
    COURT_PROCEEDINGS = 8


class Customer:
    def __init__(self, full_name: str, sex: str, age: int, services: Services):
        self.full_name = full_name
        self.sex = sex
        self.age = age 
        self.services = services

    def __str__(self):
        return f"Full name: {self.full_name}\n Sex: {self.sex}\n Age: {self.age}\n Services: {self.services}"
