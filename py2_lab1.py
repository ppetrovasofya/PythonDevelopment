import doctest


class Rectangle:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: Длина прямоугольника
        :param width: Ширина прямоугольника

        Примеры:
        >>> rectangle = Rectangle(23, 4.5)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина прямоугольника должна быть типа int или float")
        if length < 0:
            raise ValueError("Длина прямоугольника не может быть отрицательным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть типа int или float")
        if width < 0:
            raise ValueError("Ширина прямоугольника не может быть отрицательным числом")
        self.width = width

    def square(self) -> float:
        """
        Вычисляет площадь прямоугольника

        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(26.7, 7)
        >>> rectangle.square()
        """
        ...

    def perimeter(self) -> float:
        """
        Вычисляет периметр прямоугольника

        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(8, 2.3)
        >>> rectangle.perimeter()
        """
        ...


class Employee:
    def __init__(self, name: str, salary: float, position: str):
        """
        Создание и подготовка к работе объекта "Работник"

        :param name: Имя работника
        :param salary: Зарплата работника
        :param position: Должность работника

        Примеры:
        >>> employee = Employee("John", 23596.7, "Web Developer")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя сотрудника должно быть типа str")
        self.name = name

        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата работника должна быть типа int или float")
        if salary < 0:
            raise ValueError("Зарплата работника не может быть отрицательным числом")
        self.salary = salary

        if not isinstance(position, str):
            raise TypeError("Должность сотрудника должна быть типа str")
        self.position = position

    def salary_raise(self, bonus: float) -> None:
        """
        Начисление премии к зарплате
        :param bonus: Размер премии
        :raise ValueError: Если размер премии работника меньше нуля, вызываем ошибку

        :return: Зарплата работника после начисления премии

        Примеры:
        >>> employee = Employee("John", 23596.7, "Web Developer")
        >>> employee.salary_raise(1056)
        """
        ...

    def change_position(self, new_position: str) -> None:
        """
        Меняет должность сотрудника

        :return: Новая должность сотрудника

        Примеры:
        >>> employee = Employee("John", 23596.7, "Web Developer")
        >>> employee.change_position("Team Leader")
        """
        ...


class Film:
    def __init__(self, title: str, rating: float, age_limit: float):
        """
        Создание и подготовка к работе объекта "Фильм"

        :param title: Название фильма
        :param rating: Рейтинг фильма
        :param age_limit: Возрастное огранчиение фильма

        Примеры:
        >>> film = Film("Drive", 8.3, 18)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название фильма должно быть типа str")
        self.title = title

        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг фильма должен быть типа int или float")
        if rating < 1 or rating > 10:
            raise ValueError("Рейтинг фильма должен быть от 1 до 10")
        self.rating = rating

        if not isinstance(age_limit, (int, float)):
            raise TypeError("Возрастное ограничение должно быть типа int или float")
        if age_limit < 0:
            raise ValueError("Возрастное огранчиение должно быть больше или равно нулю")
        self.age_limit = age_limit

    def update_rating(self, new_rate: float) -> None:
        """
        Меняет рейтинг фильма

        :return: Обновленный рейтинг фильма

        Примеры:
        >>> film = Film("Drive", 8.3, 18)
        >>> film.update_rating(7)
        """
        ...

    def is_allowed(self) -> bool:
        """
        Функция котоаря проверяет разрешен ли фильм для всех возрастов

        :return: Разрешен ли фильм для всех возрастов (с 0 лет)

        Примеры:
        >>> film = Film("Drive", 8.3, 18)
        >>> film.is_allowed()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
