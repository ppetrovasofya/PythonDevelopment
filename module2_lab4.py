import doctest


class Car:
    def __init__(self, mark: str, country: str):
        """
            Создание и подготовка к работе объекта "Автомобиль"
            :param mark: Марка автомобиля
            :param country: Страна выпуска автомобиля
            Примеры:
        >>> car = Car("Lada", "Russia")
        """

        if not isinstance(mark, str):
            raise TypeError("Марка машины должна быть типа str")
        self.mark = mark
        if not isinstance(country, str):
            raise TypeError("Страна выпуска машины должна быть типа str")
        self.country = country

    def car_wheels(self):
        return f"Автомобиль марки {self.mark} имеет колеса"

    def __str__(self):
        return f"Автомобиль марки {self.mark} был выпущен в {self.country}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.mark!r}, country={self.country!r})"


class LightAuto(Car):
    def __init__(self, mark: str, country: str, max_speed: float):
        """ 
            Создание и подготовка к работе дочернего класса "Легковой авомобиль"
            В дочернем классе появляется новый параметр 
            :param max_speed: Максимальная скорость автомобиля
            Пример:
        >>> passenger = LightAuto("Lada", "Russia", 200)
        """
        super().__init__(mark, country)
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed < 0:
            raise ValueError("Максимальная скорость должна быть больше 0")
        self.max_speed = max_speed

    def speed_(self, car_speed: float):
        """"
        Метод, вычисляющий, может ли машина развить определенную скорость
        :param car_speed: скорость автомобиля (не максимальная)
        Примеры:
        >>> passenger = LightAuto("Lada", "Russia", 200)
        >>> passenger.speed_(100)
        """
        if not isinstance(car_speed, (float, int)):
            raise TypeError("Скорость автомобиля должна быть  типа int или float")
        if car_speed < 0:
            raise ValueError("Скорость не может быть меньше нуля")

    def __str__(self):
        return f"{super().__str__()} и имеет максимальную скорость {self.max_speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.mark!r}, country={self.country!r}, max_speed={self.max_speed!r})"


class Truck(Car):
    def __init__(self, mark: str, country: str, max_weight: float):
        """
        Создание и подготовка к работе дочернео класса "Грузовой автомобиль"
        в дочернем классе появляется новый параметр
        :param max_weight: Максимальный вес груза для машины
        Примеры:
        >>> cargo = Truck("Volkswagen", "Germany", 2000)
        """
        super().__init__(mark, country)
        if not isinstance(max_weight, (int, float)):
            raise TypeError("Максимальный вес должен быть типа float или int")
        if max_weight < 0:
            raise ValueError("Максимальный вес не может быть меньше нуля")
        self.max_weight = max_weight

    def __str__(self):
        return f"{super().__str__()} и имеет максимальную вместимость {self.max_weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.mark!r}, country={self.country!r}, max_weight={self.max_weight!r})"

    def overweight(self, current_weight: float):
        """"
        Метод, который вычисляет, будет ли перегруз или нет
        :param current_weight: вес груза
        Примеры:
        >>> truck = Truck("Volkswagen", "Germany", 5000)
        >>> truck.overweight(1000)
        """
        if not isinstance(current_weight, (int, float)):
            raise TypeError("Максимальный вес должен быть типа float или int")
        if current_weight < 0:
            raise ValueError("Максимальный вес не может быть меньше нуля")
        if current_weight > self.max_weight:
            raise ValueError("Перегруз")


if __name__ == "__main__":
    doctest.testmod()
