from tire.tire import Tire


class Carrigan_tire(Tire):
    def __init__(self,tire_wear) -> None:
        self.tire_wear = tire_wear
        
    def needs_service(self):
        for i in self.tire_wear:
            if i >= 0.9:
                return True
        return False