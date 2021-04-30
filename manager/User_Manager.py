class UserManager():
    def __init__(self, court_list: list):
        self.court_list = court_list

    def search_by_services_and_sort_by_names(self, skill, order):
        out = list()
        out = [out for service in self.court_list if service.skills == skill]
        out = sorted(self.court_list, key=lambda x: x.full_name.lower(), reverse=order)
        return out

    def sort_by_price(self, order):
        out = sorted(self.court_list, key=lambda x: x.price_of_one_service, reverse=order)
        return out
