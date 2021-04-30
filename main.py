from models import *
from manager import *

advocate1 = Advocate("Petro Petrenko", "Male", 50, Services.COURT_PROCEEDINGS, 12000, 20, 90000, Services.COURT_PROCEEDINGS,
              5, 6, 7)
advocate2 = Advocate("Iryna Irynenko", "Male", 50, Services.COURT_PROCEEDINGS, 4000, 20, 90000, Services.COURT_PROCEEDINGS,
              5, 6, 7)
advocate3 = Advocate("Detro Detrenko", "Male", 50, Services.COURT_PROCEEDINGS, 7000, 20, 90000, Services.COURT_PROCEEDINGS,
              5, 6, 7)
advocate4 = Advocate("Zetro Zetrenko", "Male", 50, Services.CONSULTATION, 10000, 20, 90000, Services.COPYRIGHT_REGISTRATION_AND_PROTECTION,
              5, 6, 7)
all_advocates = [advocate1, advocate2, advocate3, advocate4]
manager_object = UserManager(all_advocates)


out = manager_object.search_by_services_and_sort_by_names(Services.COURT_PROCEEDINGS, False)
for i in out:
    print(i)

print("----------------------------------------------------------------------------------------")

out1 = manager_object.sort_by_price(False)
for i in out1:
    print(i)
