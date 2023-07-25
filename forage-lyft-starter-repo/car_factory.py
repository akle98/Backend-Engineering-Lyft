from battery.nubbin_battery import Nubbin_Battery
from battery.spindler_battery import Spindler_Battery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    def create_calliope(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Spindler_Battery(current_date=current_date,last_service_date=last_service_date)
        car = Car(engine,battery)
        return car
    

    def create_glissade(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Spindler_Battery(current_date=current_date,last_service_date=last_service_date)
        car = Car(engine,battery)
        return car
    
    def create_panlindrome(current_date,last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        battery = Spindler_Battery(current_date=current_date,last_service_date=last_service_date)
        car = Car(engine,battery)
        return car
    
    def create_rorschach(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Nubbin_Battery(current_date=current_date,last_service_date=last_service_date)
        car = Car(engine,battery)
        return car
    
    def create_thovex(current_date,last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = Nubbin_Battery(current_date=current_date,last_service_date=last_service_date)
        car = Car(engine,battery)
        return car
