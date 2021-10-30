from typing import Any, Optional

from abc import ABC, abstractmethod

from .input_reader import InputReader


class NotImplemented(Exception):
    """Not implemented exception."""


class Solution(ABC):
    """Base class for a solution"""

    def __init__(self, year: int, day: int, name: Optional[str] = None):
        self.year = year
        self.day = day
        self.name = name
        self.data = self._read_data()

    def _read_data(self) -> Any:
        return InputReader(self.year, self.day).as_list()

    @abstractmethod
    def part_one(self) -> Any:
        ...

    @abstractmethod
    def part_two(self) -> Any:
        ...

    def __call__(self) -> tuple[Any, Any]:
        return self.part_one(), self.part_two()
