Grid = list[list[str]]

class Dir: N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

def find_guard(grid: Grid) -> tuple[int]:
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == '^':
				return (y, x)

def rotate_right(y_dir: int, x_dir: int) -> tuple[int]:
	match (y_dir, x_dir):
		case Dir.N: return Dir.E
		case Dir.E: return Dir.S
		case Dir.S: return Dir.W
		case Dir.W: return Dir.N

def solve_grid_lite(grid: Grid, y: int, x: int, y_dir: int, x_dir: int, h_bible, v_bible) -> bool:
	# NOTE: This function modifies the original grid.
	y_max, x_max = len(grid), len(grid[0])
	known = {}
	while True:
		y_dir, x_dir = rotate_right(y_dir, x_dir)
		if (y, x) not in known:
			known[(y, x)] = []
		elif (y_dir, x_dir) in known[(y, x)]:
			# Previous position reached; infinite loop.
			return False

		known[(y, x)].append((y_dir, x_dir))
		match (y_dir, x_dir):
			case Dir.N:
				if v_bible[x] == [] or y < v_bible[x][0]:
					return True
				else:
					i = len(v_bible[x]) - 1
					while v_bible[x][i] > y: i -= 1
					y = v_bible[x][i] + 1
			case Dir.E:
				if h_bible[y] == [] or x > h_bible[y][-1]:
					return True
				else:
					i = 0
					while h_bible[y][i] < x: i += 1
					x = h_bible[y][i] - 1
			case Dir.S:
				if v_bible[x] == [] or y > v_bible[x][-1]:
					return True
				else:
					i = 0
					while v_bible[x][i] < y: i += 1
					y = v_bible[x][i] - 1
			case Dir.W:
				if h_bible[y] == [] or x < h_bible[y][0]:
					return True
				else:
					i = len(h_bible[y]) - 1
					while h_bible[y][i] > x: i -= 1
					x = h_bible[y][i] + 1

def solve_grid(grid: Grid, y: int, x: int, y_dir: int, x_dir: int) -> dict:
	# NOTE: This function modifies the original grid.
	y_max, x_max = len(grid), len(grid[0])
	known = {}
	while True:
		grid[y][x] = 'X'
		if (y, x) not in known:
			known[(y, x)] = [(y_dir, x_dir)]
		else:
			known[(y, x)].append((y_dir, x_dir))

		y_next, x_next = y + y_dir, x + x_dir
		if (0 <= y_next < y_max) and (0 <= x_next < x_max):
			if grid[y_next][x_next] != '#':
				y, x = y_next, x_next
			else:
				y_dir, x_dir = rotate_right(y_dir, x_dir)
		else:
			# Guard went out of bounds; grid solved succesfully.
			return known

def part_1(data: str) -> int:
	grid = [list(line) for line in data.split('\n')]
	guard_y, guard_x = find_guard(grid)
	y_dir, x_dir = Dir.N
	solve_grid(grid, guard_y, guard_x, y_dir, x_dir)
	return ''.join([''.join(line) for line in grid]).count('X')

def part_2(data: str) -> int:
	original_grid = [list(line) for line in data.split('\n')]
	guard_y, guard_x = find_guard(original_grid)
	y_dir, x_dir = Dir.N
	y_max, x_max = len(original_grid), len(original_grid[0])

	grid_copy = [line[:] for line in original_grid]
	known = solve_grid(grid_copy, guard_y, guard_x, y_dir, x_dir)
	del known[(guard_y, guard_x)]#.remove((y_dir, x_dir))

	stuck = []
	h_bible = {
		x: [y for y, char in enumerate(line) if char == '#']
		for x, line in enumerate(grid_copy)
	}
	grid_copy = list(map(list, zip(*grid_copy)))
	v_bible = {
		y: [x for x, char in enumerate(line) if char == '#']
		for y, line in enumerate(grid_copy)
	}
	grid_copy = list(map(list, zip(*grid_copy)))
	for i, obs_p in enumerate(known.keys()):
		obs_y, obs_x = obs_p
		original_grid[obs_y][obs_x] = '#'
		v_bible[obs_x] = sorted(v_bible[obs_x] + [obs_y])
		h_bible[obs_y] = sorted(h_bible[obs_y] + [obs_x])
		if known[obs_p] != []:
			y_dir, x_dir = known[obs_p][0]
			guard_y, guard_x = obs_y - y_dir, obs_x - x_dir
			result = solve_grid_lite(grid_copy, guard_y, guard_x, y_dir, x_dir, h_bible, v_bible)
			if not result:
				stuck.append((obs_p, guard_y, guard_x))
		original_grid[obs_y][obs_x] = '.'
		v_bible[obs_x].remove(obs_y)
		h_bible[obs_y].remove(obs_x)

	return len(stuck)

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')