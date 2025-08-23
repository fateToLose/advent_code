import sys
from pathlib import Path

current_file = Path(__name__)
common_folder = current_file.parent.absolute() / "common"
sys.path.insert(0, str(common_folder))

from helper import read_as_matrix_int  # noqa: E402


# --- Part 1 --- #
def solution_part_one(data: list[list[int]]):
    def _find_save(row: list[int]) -> bool:
        for left, right in zip(row, row[1:]):
            if not 1 <= right - left <= 3:
                return False
        return True

    count = 0
    for row in data:
        if _find_save(row) or _find_save(row[::-1]):
            count += 1
    return count


# --- Part 2 --- #
def check_safe(data):
    for i in range(len(data) - 1):
        if not 1 <= data[i + 1] - data[i] <= 3:
            # print(f"Failed - {data[i + 1]} - {data[i]}")
            return False, i
    return True, -1


def loop_check_safe(data, allow_remove=True):
    res, idx = check_safe(data)
    if res:
        return True

    if allow_remove:
        return False

    if not res:
        # remove [i]
        new_arr = data[idx - 1 : idx] + data[idx + 1 :]
        # print(f"{new_arr} - remove {data[idx]}")
        res, idx = check_safe(new_arr)
        if res:
            return True
        print(f"{res} - {idx}")

    if not res:
        # remove [i + 1]
        new_arr = data[idx - 1 : idx] + data[idx + 1 :]
        # print(f"{new_arr} - remove {data[idx]}")
        res, idx = check_safe(new_arr)
        if res:
            return True
        print(f"{res} - {idx}")

    return False


def solution_part_two(data) -> int:
    count = 0
    for row in data:
        if loop_check_safe(row) or loop_check_safe(row[::-1]):
            count += 1
    return count


# --- Main --- #
if __name__ == "__main__":
    data = read_as_matrix_int(2, 2024)

    answer_one = solution_part_one(data)
    print(f"solution part 1: {answer_one}")

    answer_two = solution_part_two(data)
    print(f"solution part 2: {answer_two}")
