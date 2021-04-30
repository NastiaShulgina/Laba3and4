import unittest
from manager import *
from models import *


class TestManager(unittest.TestCase):
    def setUp(self):
        self.advocate1 = Advocate("Petro Petrenko", "Male", 50, Services.COURT_PROCEEDINGS, 12000, 20, 90000,
                                  Services.COURT_PROCEEDINGS,
                                  5, 6, 7)
        self.advocate2 = Advocate("Iryna Irynenko", "Female", 50, Services.COURT_PROCEEDINGS, 4000, 20, 90000,
                                  Services.COURT_PROCEEDINGS,
                                  5, 6, 7)
        self.advocate3 = Advocate("Detro Detrenko", "Male", 50, Services.COURT_PROCEEDINGS, 7000, 20, 90000,
                                  Services.COURT_PROCEEDINGS,
                                  5, 6, 7)
        self.advocate4 = Advocate("Zetro Zetrenko", "Male", 50, Services.CONSULTATION, 10000, 20, 90000,
                                  Services.COPYRIGHT_REGISTRATION_AND_PROTECTION, 5, 6, 7)
        all_advocates = [self.advocate1, self.advocate2, self.advocate3, self.advocate4]
        self.manager_object = UserManager(all_advocates)

    def test_search_by_services_and_sort_by_names(self):
        self.assertEqual(self.manager_object.search_by_services_and_sort_by_names(Services.COURT_PROCEEDINGS, False),
                         [self.advocate3, self.advocate2, self.advocate1])

    def test_sort_by_price(self):
        self.assertEqual(self.manager_object.sort_by_price(False),
                         [self.advocate2, self.advocate3, self.advocate4, self.advocate1])


if __name__ == "__main__":
    unittest.main()
