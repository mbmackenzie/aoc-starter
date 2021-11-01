from typing import Any, Optional

from abc import ABC, abstractmethod
from timeit import timeit as get_best_time

from .input_reader import InputReader


class NotImplemented(Exception):
    """Not implemented exception."""


class SolutionResult:
    """Class for storing the result of a solution."""

    def __init__(self, result: Any, time: Optional[float]) -> None:
        """Initialize the solution result."""
        self.result = result
        self.time = time


class Solution(ABC):
    """Base class for a solution"""

    def __init__(self, year: int, day: int, name: Optional[str] = None):
        self.year = year
        self.day = day
        self.name = name
        self.data = self._read_data()

    def _read_data(self) -> Any:
        return InputReader(self.year, self.day).as_list(int)

    @abstractmethod
    def part_one(self) -> Any:
        ...

    @abstractmethod
    def part_two(self) -> Any:
        ...

    def _make_solution_result(
        self, func_name: str, timeit: bool, number: int
    ) -> SolutionResult:
        func = getattr(self, func_name)
        return SolutionResult(
            result=func(), time=get_best_time(func, number=number) if timeit else None
        )

    def __call__(
        self, timeit: bool = False, number: int = 1000
    ) -> tuple[SolutionResult, SolutionResult]:
        return (
            self._make_solution_result("part_one", timeit, number),
            self._make_solution_result("part_two", timeit, number),
        )
