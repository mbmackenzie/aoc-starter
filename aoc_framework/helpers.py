import glob
import importlib
import os
import pathlib
import re
import sys
from datetime import datetime
from typing import Union

import click

from aoc_framework.solution import Solution
from aoc_framework.solution import SolutionResult


def get_latest_year() -> int:
    """Returns the last year if we are not in december yet otherwise returns the current year."""
    today = datetime.now()
    if today.month < 12:
        return today.year - 1
    return today.year


def import_solution(year: int, day: int, module_name: str) -> Solution:
    """Import the correct solution"""
    module_path = str(pathlib.Path(os.getcwd()))
    sys.path.append(module_path)

    module_full_name = f"{module_name}._{year}._{day:02}"
    class_name = f"Day{day:02}"

    module = importlib.import_module(module_full_name)
    return getattr(module, class_name)


def get_solution(
    year: int, day: int, module_name: str, input_file: str = None
) -> Solution:
    """Import the correct solution and return an instance of it"""

    solution_cls = import_solution(year, day, module_name)
    solution_obj = solution_cls()

    solution_obj.change_input_file(input_file)
    return solution_obj


def display_solution(solution: Solution, timeit: bool, number: int) -> None:
    """Display the first and second parts of the solution"""
    part_one, part_two = solution(timeit, number)

    def part_name(part: int) -> str:
        color = "green" if part == 1 else "red"
        return click.style(f"Part {part}:", fg=color)

    def display_part(part: int, result: SolutionResult) -> None:
        time_res = f" ({result.avg_time:.05f} sec)" if timeit else ""
        click.echo(f"{part_name(part)} {result.result}{time_res}")

    click.secho(solution, bold=True)

    display_part(1, part_one)
    display_part(2, part_two)

    if timeit:
        click.secho(f"Times represent average of {number:,d} runs", fg="yellow")


def proceed_with_overwrite(force: bool, confirm: bool) -> bool:
    """
    Ask the user if he wants to overwrite the file and return True if he does.
    If force is True, always return True.
    If confirm is True, ask the user for confirmation.
    """
    if force:
        if not confirm:
            confirm = click.confirm(
                "This will overwrite the file. Are you sure you want to continue?",
            )

    return force and confirm


def find_all_solutions():
    solutions = []
    for file in glob.glob(os.path.join("solutions", "_*", "_*.py")):

        solution = get_solution_from_file_path(file)

        if solution:
            solutions.append(solution)

    return solutions


def get_solution_from_file_path(filepath: str) -> Union[tuple[int, int], None]:
    match_year = re.compile(r"_(20\d\d)").match
    match_day = re.compile(r"_(\d\d).py").match

    _, year_folder, day_file = pathlib.Path(filepath).parts

    if not match_day(day_file):
        return None

    year = int(match_year(year_folder).groups()[0])
    day = int(match_day(day_file).groups()[0])

    return year, day
