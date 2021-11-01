import os
from typing import Optional

import click

from solutions.solution_manager import SolutionManager
from solutions.helpers import (
    get_latest_year,
    get_solution,
    display_solution,
    proceed_with_overwrite,
    find_all_solutions,
)


@click.group(invoke_without_command=True)
@click.option("--year", type=int, default=get_latest_year())
@click.option("--day", type=int, default=None)
@click.option("--timeit", is_flag=True, default=False)
@click.option("--number", "-n", "number", type=int, default=1000)
def cli(year: int, day: Optional[int], timeit: bool, number: int):
    if not day:
        click.echo("Advent of Code")
        return

    try:
        solution = get_solution(year, day)
    except ModuleNotFoundError:
        click.echo(f"Solution for day {day} of {year} not found!")
        click.echo(
            f"You can create a new implementation by running 'aoc create --year {year} --day {day}'"
        )
        return

    display_solution(solution, timeit, number)


@cli.command()
@click.option("--from-scratch", type=bool, is_flag=True, default=False)
def init(from_scratch: bool):

    solutions = find_all_solutions()
    for year, day in solutions:
        manager = SolutionManager(year, day)

        if from_scratch:
            manager.delete()
            continue

        if not manager.has_input_file:
            click.echo(f"Created input file for solution at day {day:02}, {year}")
            manager.create_input_file()


@cli.command()
@click.option("--year", type=int, default=get_latest_year())
@click.option("--day", type=int)
@click.option("--name", type=str)
@click.option("--force", type=bool, is_flag=True, default=False)
@click.option("-y", "confirm", type=bool, is_flag=True, default=False)
def create(year: int, day: int, name: Optional[str], force: bool, confirm: bool):
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
    if not day:
        click.echo("Please specify a day.")
        return

    manager = SolutionManager(year, day, name)

    if not os.path.exists(manager.solution_filepath):
        click.echo(f"Solution for day {day}, {year} not found!")
        return

    manager.delete()
    click.echo(f"Deleted file {manager.solution_filepath}")
    click.echo(f"Deleted file {manager.input_filepath}")
