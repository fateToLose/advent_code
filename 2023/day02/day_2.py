import re
import math

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?


## Directory ##
fpath = './2023/day2/puzzle.txt'


## Solution - Part 1 ##
max_cube = {
    'red': 12,
    'green': 13,
    'blue': 14,
    }


list_colours = [
    'red',
    'green',
    'blue',
    ]


def count_balls(game: str, colours: list[str] = list_colours) -> dict[str, int]:
    counter = {}
    for colour in colours:
        found_balls = re.findall(fr'(\d*) {colour}', game, re.I)
        found_balls = [int(ball) for ball in found_balls]
        count_balls = max(found_balls)
        
        counter[colour] = count_balls
    return counter


def validate_rules(answer: dict[str, int], rule: dict[str, int] = max_cube) -> bool:
    for colour in rule.keys():
        if answer[colour] > rule[colour]:
            return False
    return True


valid_game = []
with open(fpath) as lines:
    for idx, line in enumerate(lines, start=1):
        counter = count_balls(line)
        if validate_rules(counter):
            valid_game.append(idx)

answer = sum([int(id) for id in valid_game])
print(answer)

# re.findall(r'(\d+) (red|green|blue)', line) #* Faster approach 

##### Part 2 #####
# As you continue your walk, the Elf poses a second question: in each game you played, 
# what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# For each game, find the minimum set of cubes that must have been present. 
# What is the sum of the power of these sets?


## Solution - Part 2 ##
min_balls = []
with open(fpath) as lines:
    for line in lines:
        line = line.lower()
        
        counter = count_balls(line)
        min_balls.append([count for colour, count in counter.items()])

sum_all_min = [math.prod(agg) for agg in min_balls]
answer = sum(sum_all_min)
print(answer)

