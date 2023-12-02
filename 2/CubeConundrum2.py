import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

total_sum = 0

for line in lines:
    _, id_and_sets = line.split(" ", 1)
    id, sets_str = id_and_sets.split(":", 1)
    
    sets = sets_str.split(';')

    max_red = max_green = max_blue = 0
    
    for color_set in sets:
        colors = color_set.split(',')

        for color in colors:
            color_value = int(re.sub('[^0-9]', '', color))
            
            if "red" in color and color_value > max_red:
                max_red = color_value
            elif "green" in color and color_value > max_green:
                max_green = color_value
            elif "blue" in color and color_value > max_blue:
                max_blue = color_value
                    
    total_sum += max_red * max_green * max_blue

print(total_sum)
