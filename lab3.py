class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def pages(self):
        return self._pages

    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self._pages = pages

    def __str__(self):
        return f"{super().__str__()}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def duration(self):
        return self._duration

    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Количество страниц должно быть вещественным числом")
        if duration < 0:
            raise ValueError("Продолжительность не может быть отрицательным числом")

    def __str__(self):
        return f"{super().__str__()}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"


print(PaperBook("name", "author", 6).__repr__())
print(AudioBook("name", "author", 4.2).__repr__())
