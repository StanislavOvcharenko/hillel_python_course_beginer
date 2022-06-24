from datetime import date


class Car():
    max_speed = 220

    def __init__(self):
        self.color = "red"
        self.engine = "2.0"

    def get_atr(self):
        return self.color, self.engine

    @classmethod
    def change_max_speed(cls, speed):
        cls.max_speed = speed
        return cls.max_speed

    @staticmethod
    def km_to_mile(km):
        return km / 1.609


if __name__ == "__main__":
    mazda = Car()
    print(mazda.change_max_speed(200))
    print(mazda.km_to_mile(100))
    print(hasattr(Car, "get_atr"))
