import re

red_limit = 12
green_limit = 13
blue_limit = 14

with open('input.txt', 'r') as file:
    lines = file.readlines()

total_sum = 0

for line in lines:
    id_value, sets_str = line.split(":")
    id = id_value.split(" ")[1]
    
    sets = sets_str.split(';')

    valid = all(
        int(re.sub('[^0-9]', '', color)) <= red_limit if "red" in color else
        int(re.sub('[^0-9]', '', color)) <= green_limit if "green" in color else
        int(re.sub('[^0-9]', '', color)) <= blue_limit
        for set_str in sets
        for color in set_str.split(',')
    )

    if valid:
        total_sum += int(id)

print(total_sum)
