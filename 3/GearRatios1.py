with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]

cords = set()

for r, row in enumerate(lines):
    for c, cell in enumerate(row):
        if cell.isdigit() or cell == '.':
            continue
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= len(lines) or cc < 0 or cc >= len(row) or not lines[cr][cc].isdigit():
                    continue
                while cc > 0 and lines[cr][cc - 1].isdigit():
                    cc -= 1
                
                cords.add((cr, cc))
                
nums = []

for r, c in cords:
    s = ""
    while c < len(lines[r]) and lines[r][c].isdigit():
        s += lines[r][c]
        c += 1
    
    nums.append(int(s))

print(sum(nums))