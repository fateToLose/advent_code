from pathlib import Path
from typing import Optional, Any

BASE_PATH = Path.cwd()


def read_as_raw(day: int, year: int) -> str:
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"
    with open(fpath) as f:
        return f.read().strip()


def read_as_lines(day: int, year: int) -> list[str]:
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"
    with open(fpath, "r") as file:
        return [line.strip() for line in file if line.strip()]


def read_as_matrix_int(day: int, year: int) -> list[list[int]]:
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"
    with open(fpath, "r") as file:
        return [[int(x) for x in line.strip().split()] for line in file]


def read_as_matrix_char(day: int, year: int) -> list[list[str]]:
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"
    with open(fpath, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]


def read_as_grid_char(day: int, year: int) -> list[list[str]]:
    """Read character grid as 2D list"""
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"
    with open(fpath, "r") as file:
        return [list(line.rstrip()) for line in file if line.strip()]


def read_grid_dict(day: int, year: int):
    """Read grid into dictionary with (row, col) keys"""
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"

    grid = {}
    with open(fpath, "r") as file:
        for row, line in enumerate(file):
            line = line.strip()
            if line:
                for col, char in enumerate(line):
                    grid[(row, col)] = char
    return grid


def read_two_columns(day: int, year: int, dtype=int) -> tuple[list[Any], list[Any]]:
    """Read two columns of data separated by whitespace"""
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"

    col1, col2 = [], []
    with open(fpath, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                a, b = line.split()
                col1.append(dtype(a))
                col2.append(dtype(b))
    return col1, col2


def read_two_columns_as_tuples(day: int, year: int, dtype=int):
    """Read two columns as list of tuples"""
    fpath = BASE_PATH / f"{year}/day{day:02d}/puzzle.txt"

    pairs = []
    with open(fpath, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                a, b = line.split()
                pairs.append((dtype(a), dtype(b)))
    return pairs
