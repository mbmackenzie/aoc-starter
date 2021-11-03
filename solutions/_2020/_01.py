"""Day 01: Report Repair"""

from functools import reduce
from itertools import combinations

from solutions.solution import Solution


def generic_solution(data: list[int], n_terms: int, target_sum: int) -> int:
    """
    Find the n_terms numbers in data that add to target_sum. return their product
    
    Returns -1 if no valid combination is found
    """
    combinations_list = list(combinations(data, n_terms))
    for combination in combinations_list:
        if sum(combination) == target_sum:
            return reduce(lambda x, y: x * y, combination)

    return -1


class Day01(Solution):
    """Solution to day one of the 2020 Advent of Code"""

    def __init__(self):
        super().__init__(2020, 1, "Report Repair")

    def part_one(self) -> int:
        """Find two numbers in data that add to 2020 and return their product"""
        return generic_solution(self.data, 2, 2020)

    def part_two(self) -> int:
        """Find three numbers in data that add to 2020 and return their product"""
        return generic_solution(self.data, 3, 2020)

    def _get_data(self) -> list[int]:
        """Read the data from the file"""
        return self.input.as_list(int)
