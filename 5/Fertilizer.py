def get_input(file_path='input.txt'):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def process_intervals(seed_line, map_lines):
    seeds = [int(seed) for seed in seed_line.split()[1:]]
    changed = [False] * len(seeds)
    for line in map_lines:
        if line and not line.endswith(':'):
            map_values = [int(val) for val in line.split()]
            map_range = (map_values[1], map_values[1] + map_values[2] - 1)

            for i in range(len(seeds)):
                if not changed[i] and map_range[0] <= seeds[i] < map_range[1]:
                    seeds[i] = map_values[0] + seeds[i] - map_range[0]
                    changed[i] = True
        else:
            changed = [False] * len(seeds)

    return min(seeds)

def get_overlap(source_range, map_range, target_range):
    left = max(source_range[0], map_range[0])
    right = min(source_range[1], map_range[1])
    remaining = []

    if left <= right:
        if source_range[0] < left:
            remaining.append((source_range[0], left - 1))
        if source_range[1] > right:
            remaining.append((right + 1, source_range[1]))

        next_range = (left + target_range[0] - map_range[0], right + target_range[0] - map_range[0])
        return next_range, remaining

    return None, [source_range]

def find_min_after_mapping(seed_line, map_lines):
    next_intervals = [int(seed) for seed in seed_line.split()[1:]]
    next_intervals = [(next_intervals[i], next_intervals[i + 1] + next_intervals[i] - 1) for i in range(0, len(next_intervals), 2)]

    intervals = []
    for line in map_lines:
        if line and not line.endswith(':'):
            map_values = [int(val) for val in line.split()]
            map_ranges = [(map_values[1], map_values[1] + map_values[2] - 1), (map_values[0], map_values[0] + map_values[2] - 1)]

            remaining_intervals = []
            while intervals:
                interval = intervals.pop(0)
                next_interval, remaining = get_overlap(interval, map_ranges[0], map_ranges[1])
                if next_interval:
                    next_intervals.append(next_interval)
                remaining_intervals.extend(remaining)

            intervals = remaining_intervals
        else:
            intervals.extend(next_intervals)
            next_intervals = []

    intervals.extend(next_intervals)
    return min([i[0] for i in intervals])


input_lines = get_input()

result_a = process_intervals(input_lines[0], input_lines[1:])
result_b = find_min_after_mapping(input_lines[0], input_lines[1:])

print(f"A: {result_a}")
print(f"B: {result_b}")
