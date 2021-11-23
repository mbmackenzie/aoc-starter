---
marp: true
theme: uncover
class: invert
---

# Advent of Code

_adventofcode.com_

---

### What is it?

> **Advent of Code** is an advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

Every day from December 01-25, answer two problems using the provided input.

---

### Skils to develop

**Familiarity with python** - _Practice using the python standard library._

</br>

**Python best practices** - _software principles, type annotations with mypy, testing with pytest..._

</br>

**Using git and GitHub** - _Make commits, push code, share our code, and get feedback._

---

### Starter Code (python)

https://github.com/mbmackenzie/advent-of-code

Clone and pip install the repository.

Now the `aoc` command should be available and you can do a few things:

```bash
# create a python file for 2021 day 1
aoc create --day 1

# run your solution for day 1 using the input
aoc --day 1 -i input.txt
```

---

#### solutions/\_2021 modules

Basic implementations

```python
def _part_one(self) -> int:
    """Implement your solution for part 1"""

def _part_two(self) -> int:
    """Implement your solution for part 2"""

def _get_data(self) -> list:
    """Read and mutate the input data"""

def _reformat_data(self) -> None:
    """Change the shape of the input data"""
```

###### Access the data in the `_part_one` or `_part_two` by using `self.data`.
