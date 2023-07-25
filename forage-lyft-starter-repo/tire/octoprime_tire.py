from tire.tire import Tire


class Octoprime_tire(Tire):
    def __init__(self,tire_wear) -> None:
        self.tire_wear = tire_wear
        
    def needs_service(self):
        res = 0
        for i in self.tire_wear:
            res += i
        if res >= 3.0:
            return True
        else: 
            return False