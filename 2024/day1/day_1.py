"""
2024 Day 1 Solution - Part 1
"""

puzzle_fpath = "2024\\day1\\puzzle.txt"

list_a = []
list_b = []

with open(puzzle_fpath) as lines:
    for line in lines:
        result: list[str] = line.split(" ")
        list_a.append(result[0])
        list_b.append(result[-1])

list_a_sort: list[int] = [int(num) for num in sorted(list_a)]
list_b_sort: list[int] = [int(num) for num in sorted(list_b)]

answer = []
for i, num_a in enumerate(list_a_sort):
    ans = abs(num_a - list_b_sort[i])
    answer.append(ans)

print(sum(answer))


"""
2024 Day 1 Solution - Part 2
"""

from collections import Counter

count = Counter(list_b_sort)

answer_2 = []
for num in list_a_sort:
    if count[num]:
        answer_2.append(num * count[num])

print(sum(answer_2))
