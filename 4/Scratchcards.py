from collections import defaultdict

with open('input.txt', 'r') as file:
    game_lines = file.readlines()

p1_total_score = 0
game_counts = defaultdict(lambda: 1)

for line in game_lines:
    game_info, moves_info = line.split(": ")
    game_id = int(game_info.split()[1])

    winning_numbers = list(map(int, moves_info.split(" | ")[0].split()))
    mine_numbers = list(map(int, moves_info.split(" | ")[1].split()))

    matching_numbers = len(set(winning_numbers).intersection(mine_numbers))
    score = 2 ** matching_numbers if matching_numbers > 0 else 1
    p1_total_score += score

    for next_game_id in range(game_id + 1, game_id + matching_numbers + 1):
        game_counts[next_game_id] += game_counts[game_id]

p2_total_games = sum(game_counts.values()) + 1

print("Part 1:", p1_total_score)
print("Part 2:", p2_total_games)
