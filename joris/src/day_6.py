from bisect import bisect
from itertools import cycle

class Dir: N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

def find_guard(grid: list[list[str]]) -> tuple[int]:
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == '^':
				return (y, x)

def grid_solve(
	grid: list[list[str]], y: int, x: int, y_dir: int, x_dir: int
) -> dict[tuple[int], tuple[int]]:

	y_max, x_max = len(grid), len(grid[0])

	directions = cycle([Dir.N, Dir.E, Dir.S, Dir.W])
	while next(directions) != (y_dir, x_dir): pass

	visited = {}
	while True:
		if (y, x) not in visited:
			visited[(y, x)] = (y_dir, x_dir)

		y_next, x_next = y + y_dir, x + x_dir
		if (0 <= y_next < y_max) and (0 <= x_next < x_max):
			if grid[y_next][x_next] != '#':
				y, x = y_next, x_next
			else:
				y_dir, x_dir = next(directions)
		else:
			return visited

def obstacle_solve(
	y: int, x: int, d: tuple[int],
	row_obs: dict[int, list[int]], col_obs: dict[int, list[int]]
) -> bool:

	directions = cycle([Dir.N, Dir.E, Dir.S, Dir.W])
	while next(directions) != d: pass

	visited = {}
	while True:
		loc = (y, x)
		d = next(directions)

		if loc not in visited: visited[loc] = d
		elif visited[loc] == d: return False

		match d:
			case Dir.N:
				b = bisect(col_obs[x], y)
				if b == 0: return True
				else: y = col_obs[x][b - 1] + 1
			case Dir.E:
				b = bisect(row_obs[y], x)
				if b == len(row_obs[y]): return True
				else: x = row_obs[y][b] - 1
			case Dir.S:
				b = bisect(col_obs[x], y)
				if b == len(col_obs[x]): return True
				else: y = col_obs[x][b] - 1
			case Dir.W:
				b = bisect(row_obs[y], x)
				if b == 0: return True
				else: x = row_obs[y][b - 1] + 1

def transposed(grid: list[list[str]]):
	return list(map(list, zip(*grid)))

def part_1(data: str) -> int:
	grid = [list(line) for line in data.split('\n')]
	y, x = find_guard(grid)
	y_dir, x_dir = Dir.N

	visited = grid_solve(grid, y, x, y_dir, x_dir)

	return len(visited)

def part_2(data: str) -> int:
	grid = [list(line) for line in data.split('\n')]
	y, x = find_guard(grid)
	y_dir, x_dir = Dir.N

	visited = grid_solve(grid, y, x, y_dir, x_dir)
	del visited[(y, x)]

	row_obs = {
		y: [x for x, char in enumerate(line) if char == '#']
		for y, line in enumerate(grid)
	}
	col_obs = {
		x: [y for y, char in enumerate(line) if char == '#']
		for x, line in enumerate(transposed(grid))
	}

	n_stuck = 0
	for obs_p, d in visited.items():
		obs_y, obs_x = obs_p
		y_dir, x_dir = d

		row_obs[obs_y] = sorted(row_obs[obs_y] + [obs_x])
		col_obs[obs_x] = sorted(col_obs[obs_x] + [obs_y])

		y, x = obs_y - y_dir, obs_x - x_dir
		solved = obstacle_solve(y, x, d, row_obs, col_obs)
		if not solved: n_stuck += 1

		row_obs[obs_y].remove(obs_x)
		col_obs[obs_x].remove(obs_y)

	return n_stuck

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')