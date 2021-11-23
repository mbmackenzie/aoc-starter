import os
from typing import Optional

import click

from aoc_framework.helpers import display_solution
from aoc_framework.helpers import find_all_solutions
from aoc_framework.helpers import get_latest_year
from aoc_framework.helpers import get_solution
from aoc_framework.helpers import proceed_with_overwrite
from aoc_framework.solution_manager import SolutionManager


@click.group()
def cli():
    """Advent of Code"""


@cli.command()
@click.option("--year", type=int, default=get_latest_year())
@click.option("--day", type=int)
@click.option("--timeit", is_flag=True, default=False)
@click.option("--number", "-n", "number", type=int, default=1000)
@click.option("--module", "-m", "module_name", type=str, default="solutions")
@click.option("--input", "-i", "input_file", type=str, default="input.txt")
def run(
    year: int, day: int, timeit: bool, number: int, module_name: str, input_file: str,
):
    """Run a solution module"""
    if not day:
        click.echo("Please specify a day.")
        return

    try:
        solution = get_solution(year, day, module_name, input_file)
    except ModuleNotFoundError:
        click.echo(f"Solution for day {day} of {year} not found!")
        click.echo(
            f"You can create a new implementation by running 'aoc create --year {year} --day {day}'"
        )
        return

    display_solution(solution, timeit, number)


@cli.command()
def init(from_scratch: bool):
    """Initialize a new solution package"""


@cli.command()
@click.option("--year", type=int, default=get_latest_year())
@click.option("--day", type=int)
@click.option("--name", type=str)
@click.option("--force", type=bool, is_flag=True, default=False)
@click.option("-y", "confirm", type=bool, is_flag=True, default=False)
def create(year: int, day: int, name: Optional[str], force: bool, confirm: bool):
    """Create a soution module"""
    if not day:
        click.echo("Please specify a day.")
        return

    overwrite = proceed_with_overwrite(force, confirm)
    if force and not overwrite:
        click.echo("Exiting.")
        return

    try:
        manager = SolutionManager(year, day, name)
        manager.create(overwrite=overwrite)
    except FileExistsError:
        click.echo(
            f"Solution for day {day}, {year} already exists! "
            "Use --force to override this file."
        )
        return

    click.echo(f"Created solution template at {manager.solution_filepath}")
    click.echo(f"Created input file for solution at {manager.input_filepath}")


@cli.command()
@click.option("--year", type=int, default=get_latest_year())
@click.option("--day", type=int)
@click.option("--name", type=str)
def delete(year: int, day: int, name: Optional[str]):
    """Delete a solution module"""
    if not day:
        click.echo("Please specify a day.")
        return

    manager = SolutionManager(year, day, name)

    if not os.path.exists(manager.solution_filepath):
        click.echo(f"Solution for day {day}, {year} not found!")
        return

    manager.delete()
    click.echo(f"Deleted file {manager.solution_filepath}")
