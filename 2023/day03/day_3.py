import re
import os

# Any number adjacent to a symbol, even diagonally,
# is a "part number" and should be included in your sum.
# (Periods (.) do not count as a symbol.)


## Directory ##
fpath = f"{os.getcwd()}\\2023\\day3\\puzzle.txt"


## Solution - Part 1 ##
with open(fpath, "r") as file_reader:
    puzzle = file_reader.read().split("\n")

index_sym: dict[int, list[int]] = {}
for i, row in enumerate(puzzle):
    for n, char in enumerate(row):
        

print(puzzle[0])
print(puzzle[1])
print(puzzle[2])

re_find_num = re.compile(r"[0-9]+")
re_find_sym = re.compile(r"")

test = puzzle[1]
print(test)
re.search(r"[^0-9\.]", test)