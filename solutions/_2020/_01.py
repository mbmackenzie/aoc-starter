"""Day 01: Report Repair"""

from functools import reduce
from itertools import combinations

from solutions.solution import Solution

TEST_DATA = [2018, 2, 1, 1]


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

    data: list[int]

    def __init__(self):
        super().__init__(2020, 1)

    def part_one(self) -> int:
        """Find two numbers in data that add to 2020 and return their product"""
        return generic_solution(self.data, 2, 2020)

    def part_two(self) -> int:
        """Find three numbers in data that add to 2020 and return their product"""
        return generic_solution(self.data, 3, 2020)


if __name__ == "__main__":
    print("n_terms = 2 ->", generic_solution(TEST_DATA, 2, 2020))
    print("n_terms = 3 ->", generic_solution(TEST_DATA, 3, 2020))
