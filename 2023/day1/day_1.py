import re
from typing import Dict


## Directory ##
fpath = './2023/day1/puzzle.txt'


## Part 1 ##
# On each line, the calibration value can be found by combining the first digit and the last digit 
# (in that order) to form a single two-digit number.


### Long Solution - by array ###

def get_digits(line:str) -> int:
    left, right = 0, -1
    left_okay, right_okay = False, False
    
    while not left_okay:
        if not line[left].isdigit():
            left += 1
        else:
            left_okay = True
    
    while not right_okay:
        if not line[right].isdigit():
            right -= 1
        else:
            right_okay = True
    
    return int(line[left] + line[right]) 


answer = 0
with open(fpath) as lines:
    for line in lines:
        answer += get_digits(line)
print(f'Part 1: {answer}')


### Shorter - with regex ### 
find_digit = re.compile(r'(?=(\d{1}))')

answer = 0
with open(fpath) as lines:
    for line in lines:
        res = find_digit.findall(line)
        first, last = res[0], res[-1]
        answer += int(first + last)
        
print(f'Part 1: {answer}')


## Part 2 ##
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".


def convert_word_to_digit(text:str, map_dict:Dict[str, str]) -> str:
    get_digit = map_dict.get(text)
    if get_digit is not None:
        return get_digit
    return text

digit_to_num = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    }


# Main  - Part 2 #
find_digit = re.compile(r'(?=(\d{1}|one|two|three|four|five|six|seven|eight|nine))')

answer = 0
with open(fpath) as lines:
    for line in lines:
        res = find_digit.findall(line)
        first, last = res[0], res[-1]
        first, last = convert_word_to_digit(first, digit_to_num) + convert_word_to_digit(last, digit_to_num)
        combine = int(first + last)
        answer += combine

print(f'Part 2: {answer}')
