import os
from pathlib import Path
from typing import Optional

TEMPLATE_PATH = os.path.join("solutions", "assets", "solution_template.txt")


def read_solution_template() -> str:
    """Read the template file"""
    with open(TEMPLATE_PATH) as f:
        return f.read()


def create_dir(dirpath: Path) -> None:
    """Create a directory"""
    if os.path.exists(dirpath):
        return

    os.mkdir(dirpath)

    if dirpath.parts[0] == "solutions":
        save_file(os.path.join(dirpath, "__init__.py"))


def save_file(filepath: Path, content: Optional[str] = None) -> None:
    """Save the content to disk"""
    if not filepath.parent.exists():
        create_dir(filepath.parent)

    with open(filepath, "w") as f:
        if content:
            f.write(content)


def delete_file(filepath: str) -> None:
    """Delete a file"""
    if os.path.exists(filepath):
        os.remove(filepath)


class SolutionManager:
    """Manage the creation and deletion a solution"""

    year: int
    day: int
    name: Optional[str]

    def __init__(self, year: int, day: int, name: Optional[str] = None):
        self.year = year
        self.day = day
        self.name = name

    @property
    def solution_filepath(self) -> Path:
        filepath = os.path.join("solutions", f"_{self.year}", f"_{self.day:02}.py")
        return Path(filepath)

    @property
    def has_solution_file(self) -> bool:
        """Check if the solution file exists"""
        return self.solution_filepath.exists()

    def create(self, overwrite: Optional[bool] = False) -> None:
        """Create the solution."""

        if os.path.exists(self.input_filepath) and not overwrite:
            raise FileExistsError()

        template = self._create_solution_template()

        self.create_solution_file(template)

    def delete(self) -> None:
        """Delete the solution"""
        delete_file(self.solution_filepath)

    def create_solution_file(self, template: str) -> None:
        """Save the solution file"""
        save_file(self.solution_filepath, template)

    def _create_solution_template(self) -> str:
        """Create a template for a solution and return the filepath"""
        template = read_solution_template()
        return self._format_solution_template(template)

    def _format_solution_template(self, template: str) -> str:
        """Format the template for a solution"""

        name = self.name if self.name else ""
        docstring = f"Day {self.day}" + (f": {self.name}" if self.name else "")
        return template.format(
            year=self.year, day=self.day, name=name, docstring=docstring
        )