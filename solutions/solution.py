from typing import Any, Callable, Optional

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

    def __str__(self) -> str:
        """Return the string representation of the solution result."""
        return f"{self.result}"

    def __repr__(self):
        return self.__str__()


class Solution(ABC):
    """Base class for a solution"""

    def __init__(self, year: int, day: int, name: Optional[str] = None):
        self.year = year
        self.day = day
        self.name = name

        self.input = InputReader(year, day)
        self._reformat_data()

        self.data = None

    @abstractmethod
    def part_one(self) -> Any:
        ...

    @abstractmethod
    def part_two(self) -> Any:
        ...

    def _reformat_data(self) -> None:
        pass

    def _get_data(self) -> list[str]:
        return self.input.as_list()

    def _get_data_for_part_one(self) -> list[str]:
        return self._get_data()

    def _get_data_for_part_two(self) -> list[str]:
        return self._get_data()

    def _set_data_for_part_one(self) -> None:
        self.data = self._get_data_for_part_one()

    def _set_data_for_part_two(self) -> None:
        self.data = self._get_data_for_part_two()

    def _make_solution_result(
        self, func_name: str, timeit: bool, number: int
    ) -> SolutionResult:

        part_func = getattr(self, func_name)
        data_func = getattr(self, f"_set_data_for_{func_name}")

        data_func()
        return SolutionResult(
            result=part_func(),
            time=get_best_time(part_func, number=number) if timeit else None,
        )

    def __call__(
        self, timeit: bool = False, number: int = 1000
    ) -> tuple[SolutionResult, SolutionResult]:
        return (
            self._make_solution_result("part_one", timeit, number),
            self._make_solution_result("part_two", timeit, number),
        )

    def __str__(self) -> str:
        return f"Day {self.day}, {self.year}" + (f" - {self.name}" if self.name else "")
