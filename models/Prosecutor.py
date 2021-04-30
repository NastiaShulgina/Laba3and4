from models import Employee
from models import Services


class Prosecutor(Employee):
    def __init__(self, full_name: str, sex: str, age: int, services: Services,
                 price_of_one_service: int, years_of_experience: int, salary: int, skills: list,
                 corruptibility: bool, investigation_management: bool):
        super().__init__(full_name, sex, age, services, price_of_one_service, years_of_experience, salary, skills)
        self.full_name = full_name
        self.sex = sex
        self.age = age
        self.services = services
        self.price_of_one_service = price_of_one_service
        self.years_of_experience = years_of_experience
        self.salary = salary
        self.skills = skills
        self.corruptibility = corruptibility
        self.investigation_management = investigation_management

    def __str__(self):
        return f"Full name: {self.full_name}\nSex: {self.sex}\nAge: {self.age}\nServices: {self.services}\n" \
               f"Price of one service: {self.price_of_one_service}\nYears or experience: {self.years_of_experience}" \
               f"\nSalary: {self.salary}\nSkills: {self.skills}\nCorruptibility: {self.corruptibility}\n" \
               f"Investigation management: {self.investigation_management}"
