import unittest
from datetime import date

from battery.nubbin_battery import Nubbin_Battery
from battery.spindler_battery import Spindler_Battery

class TestNubbinBattery(unittest.TestCase):
    def test_need_service(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2020-06-15")
        battery = Nubbin_Battery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())


    def test__no_need_service(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2022-06-15")
        battery = Nubbin_Battery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_need_service(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2019-06-15")
        battery = Spindler_Battery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())


    def test__no_need_service(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2022-06-15")
        battery = Spindler_Battery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())
if __name__=="__main__":
    unittest.main()