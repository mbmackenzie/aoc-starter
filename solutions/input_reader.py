from typing import Callable, Optional


class InputReader:
    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day
        self.filename = f"inputs/_{year}/_{day:02}.txt"
        self.__content = self.__read_file()

    def __read_file(self) -> list:
        with open(self.filename, "r") as f:
            return f.readlines()

    def as_list(self, mutate: Optional[Callable] = None) -> list:
        if mutate:
            return [mutate(x) for x in self.__content]

        return [x.strip() for x in self.__content]
