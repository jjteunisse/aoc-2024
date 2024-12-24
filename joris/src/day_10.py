def solve(data: str, *, part_2: bool) -> int:
	grid = [[int(char) for char in line] for line in data.split('\n')]

	heads = [
		(y, x)
		for y, line in enumerate(grid)
		for x, digit in enumerate(line)
		if digit == 0
	]

	y_max, x_max = len(grid), len(grid[0])
	score = 0
	for i, head in enumerate(heads):
		peaks = []
		trails = [head]
		while trails != []:
			y, x = trails.pop(0)
			height = grid[y][x]
			if height == 9 and (part_2 or (y, x) not in peaks):
				peaks.append((y, x))
			else:
				if y > 0 and grid[y - 1][x] == height + 1:
					trails.append((y - 1, x))
				if y < y_max - 1 and grid[y + 1][x] == height + 1:
					trails.append((y + 1, x))
				if x > 0 and grid[y][x - 1] == height + 1:
					trails.append((y, x - 1))
				if x < x_max - 1 and grid[y][x + 1] == height + 1:
					trails.append((y, x + 1))
		score += len(peaks)

	return score

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part_2=False)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part_2=True)}.')