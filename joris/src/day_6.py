class Dir: N, E, S, W = [-1, 0], [0, 1], [1, 0], [0, -1]

def find_guard(grid: list[list[str]]) -> list[int]:
	for y, line in enumerate(grid):
		if '^' in line:
			return [y, line.index('^')]

def is_within_bounds(next_guard_pos: list[int], grid_dims: list[int]) -> bool:
	return (
		0 <= next_guard_pos[0] < grid_dims[0] and
		0 <= next_guard_pos[1] < grid_dims[1]
	)

def print_grid(grid: list[list[str]]):
	for line in grid: print(line)

def move(guard_pos: list[int], guard_dir: list[int]) -> list[int]:
	return [sum(x) for x in zip(guard_pos, guard_dir)]

def rotate_right(guard_pos: list[int]) -> list[int]:
	match guard_pos:
		case Dir.N: return Dir.E
		case Dir.E: return Dir.S
		case Dir.S: return Dir.W
		case Dir.W: return Dir.N

def solve_grid(grid: list[list[str]]):
	grid_dims = [len(grid), len(grid[0])]
	guard_pos = find_guard(grid)
	guard_dir = Dir.N
	y, x = guard_pos
	grid[y][x] = 'X'
	while True:
		next_guard_pos = move(guard_pos, guard_dir)
		y_next, x_next = next_guard_pos
		if is_within_bounds(next_guard_pos, grid_dims):
			if grid[y_next][x_next] != '#':
				grid[y_next][x_next] = 'X'
				guard_pos = next_guard_pos
			else:
				guard_dir = rotate_right(guard_dir)
		else:
			break

def part_1(data: str) -> int:
	grid = [list(line) for line in data.split('\n')]
	solve_grid(grid)
	# print_grid(grid)
	return ''.join([''.join(line) for line in grid]).count('X')

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')