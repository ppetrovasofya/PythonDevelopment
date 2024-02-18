class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self):
        return self.name

    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        if not isinstance(duration, float):
            raise TypeError("Количество страниц должно быть вещественным числом")
        if duration < 0:
            raise ValueError("Продолжительность не может быть отрицательным числом")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


print(PaperBook("name", "author", 6).__repr__())
