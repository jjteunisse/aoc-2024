def find_valid_dirs(word: str, grid: list[list[str]], y: int, x: int) \
-> list[tuple[int]]:
	y_max, x_max = len(grid), len(grid[0])
	valid_dirs = []
	if grid[y][x] == word[0]:
		for y_dir in [-1, 0, 1]:
			for x_dir in [-1, 0, 1]:
				if (
					0 <= y + (len(word) - 1) * y_dir < y_max and
					0 <= x + (len(word) - 1) * x_dir < x_max and
					all([grid[y + i * y_dir][x + i * x_dir] == word[i]
						 for i in range(1, len(word))])
				):
					valid_dirs.append((y_dir, x_dir))
	return valid_dirs

def part_1(data: str) -> int:
	grid = [list(line) for line in data.split('\n')]
	n_times = 0
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			n_times += len(find_valid_dirs('XMAS', grid, y, x))
	return n_times

def part_2(data: str) -> int:
	grid = [list(line) for line in data.split('\n')]
	valid = []
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			for d in find_valid_dirs('MAS', grid, y, x):
				valid.append((y, x, d))
	# Determine the location of the 'A' for all diagonal 'MAS' instances.
	a_locs = [(y + d[0], x + d[1]) for (y, x, d) in valid if 0 not in d]
	# The 'X' shape effectively means that a single A has multiple diagonals.
	return len(a_locs) - len(set(a_locs))

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')