from models import Employee, Services


class Advocate(Employee):
    def __init__(self, full_name: str, sex: str, age: int, services: Services,
                 price_of_one_service: int, years_of_experience: int, salary: int, skills: list,
                 won_court_proceedings_amount: int, conducted_proceedings_amount: int, recommendations_amount):
        super().__init__(full_name, sex, age, services, price_of_one_service, years_of_experience, salary, skills)
        self.full_name = full_name
        self.sex = sex
        self.age = age
        self.services = services
        self.price_of_one_service = price_of_one_service
        self.years_of_experience = years_of_experience
        self.salary = salary
        self.skills = skills
        self.won_court_proceedings_amount = won_court_proceedings_amount
        self.conducted_proceedings_amount = conducted_proceedings_amount
        self.recommendations_amount = recommendations_amount

    def __str__(self):
        return f"Full name: {self.full_name}\nSex: {self.sex}\nAge: {self.age}\nServices: {self.services}\n" \
               f"Price of one service: {self.price_of_one_service}\nYears or experience: {self.years_of_experience}" \
               f"\nSalary: {self.salary}\n Skills: {self.skills}\nWon court proceedings amount: " \
               f"{self.won_court_proceedings_amount}\n Conducted proceedings amount: " \
               f"{self.conducted_proceedings_amount}\nRecommendations amount: {self.recommendations_amount}"
