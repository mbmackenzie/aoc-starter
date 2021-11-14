import os
from typing import Callable
from typing import Optional


class InputReader:
    def __init__(self, year: int, day: int, input: Optional[str] = None):
        self.year = year
        self.day = day
        self.filename = input if input else f"inputs/_{year}/_{day:02}.txt"
        self._file_exits = os.path.exists(self.filename)

        if self._file_exits:
            self.__content = self.__read_file()
        else:
            self.__content = None

    @property
    def content(self) -> str:
        if not self._file_exits:
            raise FileNotFoundError(f"File {self.filename} not found")

        return self.__content

    def __read_file(self) -> list:
        with open(self.filename, "r") as f:
            return f.readlines()

    def as_list(self, mutate: Optional[Callable] = None) -> list:
        if mutate:
            return [mutate(x) for x in self.content]

        return [x.strip() for x in self.content]

    def reformat(self, formater: Callable, **kwargs) -> None:
        if self.__content:
            self.__content = formater(self.content, **kwargs)
