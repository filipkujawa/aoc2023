with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]

result = 0

for r, row in enumerate(lines):
    for c, cell in enumerate(row):
        if cell != "*":
            continue
        
        cords = set()
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= len(lines) or cc < 0 or cc >= len(row) or not lines[cr][cc].isdigit():
                    continue
                while cc > 0 and lines[cr][cc - 1].isdigit():
                    cc -= 1
                
                cords.add((cr, cc))
        
        if len(cords) != 2:
            continue
        
        nums = []

        for cr, cc in cords:
            s = ""
            while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                s += lines[cr][cc]
                cc += 1
            
            nums.append(int(s))
        
        result += nums[0] * nums[1]

print(result)