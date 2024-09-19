# On each line, the calibration value can be found by combining the first digit and the last digit 
# (in that order) to form a single two-digit number.


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



# Main #
fpath = './2023/puzzle.txt'
answer = 0

with open(fpath) as lines:
    for line in lines:
        answer += get_digits(line)
answer