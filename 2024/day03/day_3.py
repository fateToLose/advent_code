import re
import sys
from pathlib import Path

current_file = Path(__name__)
common_folder = current_file.parent.absolute()
sys.path.insert(0, str(common_folder))

from common.helper import read_as_raw


# --- Part 1 --- #
def solution_part_one(data: str) -> int:
    all_mul = re.findall(r"mul\((\d*),(\d*)\)", data)

    total_sum = 0
    for first, second in all_mul:
        total_sum += int(first) * int(second)
    return total_sum


def solution_part_two(data: str) -> int:
    found_regex = re.findall(r"mul\((\d*),(\d*)\)|(do\(\))|(don't\(\))", data)

    total_sum = 0
    to_calculate = True
    for first, second, do, dont in found_regex:
        if dont:
            to_calculate = False
        if do:
            to_calculate = True

        if first and second:
            total_sum += (int(first) * int(second)) * to_calculate

    return total_sum


# --- Main --- #
if __name__ == "__main__":
    data = read_as_raw(3, 2024)

    solution_one = solution_part_one(data)
    print(f"Solution Part One - {solution_one}")

    solution_two = solution_part_two(data)
    print(f"Solution Part One - {solution_two}")
