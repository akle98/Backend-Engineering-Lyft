import unittest

from tire.carrigan_tire import Carrigan_tire
from tire.octoprime_tire import Octoprime_tire

class TestCarriganTire(unittest.TestCase):
    def test_needs_serivce(self):
        tire_wear = [0.1,0.4,0.9,0.8]
        tire = Carrigan_tire(tire_wear)
        self.assertTrue(tire.needs_service())
    def test_no_need_service(self):
        tire_wear = [0.1,0.4,0.8,0.8]
        tire = Carrigan_tire(tire_wear)
        self.assertFalse(tire.needs_service())
class TestOctoprimeTire(unittest.TestCase):
    def test_needs_serivce(self):
        tire_wear = [0.9,0.9,0.9,0.8]
        tire = Octoprime_tire(tire_wear)
        self.assertTrue(tire.needs_service())
    def test_no_need_service(self):
        tire_wear = [0.7,0.9,0.7,0.5]
        tire = Octoprime_tire(tire_wear)
        self.assertFalse(tire.needs_service()) 