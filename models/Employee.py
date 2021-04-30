from models import Customer, Services


class Employee(Customer):
    def __init__(self, full_name: str, sex: str, age: int, services: Services,
                 price_of_one_service: int, years_of_experience: int, salary: int, skills: list):
        super().__init__(full_name, sex, age, services)
        self.price_of_one_service = price_of_one_service
        self.years_of_experience = years_of_experience
        self.salary = salary
        self.skills = skills

    def __str__(self):
        return f"Full name: {self.full_name}\nSex: {self.sex}\nAge: {self.age}\nServices: {self.services}\n" \
            f"Price of one service: {self.price_of_one_service}\nYears or experience: {self.years_of_experience}\n" \
            f"Salary: {self.salary}\n\ Skills: {self.skills}"
