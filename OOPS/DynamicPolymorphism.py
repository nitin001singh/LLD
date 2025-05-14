from abc import ABC, abstractmethod

# Abstract Base Class: Car
class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass


# Derived Class: ManualCar
class ManualCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.current_gear = 0

    def shift_gear(self, gear):
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")

    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return
        self.current_speed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")


# Derived Class: ElectricCar
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery_level = 100

    def charge_battery(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} : Battery fully charged!")

    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return
        if self.battery_level <= 0:
            print(f"{self.brand} {self.model} : Battery dead! Cannot accelerate.")
            return
        self.battery_level -= 10
        self.current_speed += 15
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h. Battery at {self.battery_level}%.")

    def brake(self):
        self.current_speed -= 15
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Regenerative braking! Speed is now {self.current_speed} km/h. Battery at {self.battery_level}%.")


# Main execution
if __name__ == "__main__":
    my_manual_car = ManualCar("Suzuki", "WagonR")
    my_manual_car.start_engine()
    my_manual_car.accelerate()
    my_manual_car.accelerate()
    my_manual_car.brake()
    my_manual_car.stop_engine()

    print("----------------------")

    my_electric_car = ElectricCar("Tesla", "Model S")
    my_electric_car.start_engine()
    my_electric_car.accelerate()
    my_electric_car.accelerate()
    my_electric_car.brake()
    my_electric_car.stop_engine()
