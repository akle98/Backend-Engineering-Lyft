from utils import add_years_to_date
from battery.battery import Battery

class Spindler_Battery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.threshold_year = 3

    def needs_service(self):
        serviced_date = add_years_to_date(self.last_service_date, self.threshold_year)
        return serviced_date < self.current_date
