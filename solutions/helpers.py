import os
import re
import glob
import pathlib
import importlib
from datetime import datetime
from typing import Union

import click
from solutions.solution import Solution


def get_latest_year() -> int:
    """Returns the last year if we are not in december yet otherwise returns the current year."""
    today = datetime.now()
    if today.month < 12:
        return today.year - 1
    return today.year


def get_solution(year: int, day: int) -> Solution:
    """Import the correct solution and return an instance of it"""
    module_name = f"solutions._{year}._{day:02}"
    class_name = f"Day{day:02}"

    module = importlib.import_module(module_name)
    solution_cls = getattr(module, class_name)
    return solution_cls()


def display_solution(solution: Solution) -> None:
    """Display the first and second parts of the solution"""
    part_one, part_two = solution()

    def part_name(part: int) -> str:
        color = "green" if part == 1 else "red"
        return click.style(f"Part {part}:", fg=color)

    click.secho(f"Day {solution.day}, {solution.year}", bold=True)
    click.echo(f"{part_name(1)} {part_one}")
    click.echo(f"{part_name(2)} {part_two}")


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
