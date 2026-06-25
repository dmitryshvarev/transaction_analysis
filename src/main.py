#from src.views import get_home_page_info
from src.services import phone_number_search
from src.utils import get_transactions_for_analysis

#print(get_home_page_info("2020-05-20 06:00:00"))
print(phone_number_search(get_transactions_for_analysis(r"..\data\operations.xlsx", "2020-07-22 10:30:00")))

