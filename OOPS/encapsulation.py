class SportsCar:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._is_engine_on = False
        self._current_speed = 0
        self._current_gear = 0
        self._tyre_company = None

    def get_speed(self):
        return self._current_speed

    def get_tyre_company(self):
        return self._tyre_company

    def set_tyre_company(self, company):
        self._tyre_company = company

    def start_engine(self):
        self._is_engine_on = True
        print(f"{self._brand} {self._model} : Engine starts with a roar!")

    def shift_gear(self, gear):
        self._current_gear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self._current_gear}")

    def accelerate(self):
        if not self._is_engine_on:
            print(f"{self._brand} {self._model} : Engine is off! Cannot accelerate.")
            return
        self._current_speed += 20
        print(f"{self._brand} {self._model} : Accelerating to {self._current_speed} km/h")

    def brake(self):
        self._current_speed -= 20
        if self._current_speed < 0:
            self._current_speed = 0
        print(f"{self._brand} {self._model} : Braking! Speed is now {self._current_speed} km/h")

    def stop_engine(self):
        self._is_engine_on = False
        self._current_gear = 0
        self._current_speed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")

if __name__ == "__main__":
    my_sports_car = SportsCar("Ford", "Mustang")

    my_sports_car.start_engine()
    my_sports_car.shift_gear(1)
    my_sports_car.accelerate()
    my_sports_car.shift_gear(2)
    my_sports_car.accelerate()
    my_sports_car.brake()
    my_sports_car.stop_engine()

    # Trying to change internal speed directly (which should be avoided)
    # my_sports_car._current_speed = 500  # Not recommended

    print("Current Speed of My Sports Car is", my_sports_car.get_speed())

    my_sports_car.set_tyre_company("Michelin")
    print("Tyres provided by", my_sports_car.get_tyre_company())
