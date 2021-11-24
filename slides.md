---
marp: true
theme: uncover
class: invert
---

# Advent of Code

_[adventofcode.com](https://adventofcode.com/)_

---

### What is it?

> **Advent of Code** is an advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

<br>

Every day from December 01-25, answer two problems using the provided input.

---

### Skils to develop

**Familiarity with python** - _practice using the python standard library._

</br>

**Python best practices** - _software design principles, type annotations, testing..._

</br>

**Using git and GitHub** - _make commits, push code, share code, and get feedback._

---

### Starter Code (python)

[mbmackenzie/adventofcode-framework](https://github.com/mbmackenzie/adventofcode-framework)

</br>

Use the `aoc` command:

```bash
# create a python file for 2021 day 1
aoc create 01 --year 2021

# run your solution for day 1 using the input
aoc run 01 --year 2021 -i input.txt
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
