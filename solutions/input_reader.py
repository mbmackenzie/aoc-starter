import pandas as pd


class InputReader:
    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day
        self.filename = f"inputs/_{year}/_{day:02}.txt"
        self.__content = self.__read_file()

    def __read_file(self) -> list:
        with open(self.filename, "r") as f:
            return f.readlines()

    def as_list(self, cast_as: str = "int") -> list:
        if cast_as == "int":
            return [int(x) for x in self.__content]
        elif cast_as == "float":
            return [float(x) for x in self.__content]
        else:
            return [x.strip() for x in self.__content]


if __name__ == "__main__":
    input_reader = InputReader(2020, 1)
    print(input_reader.as_list())
