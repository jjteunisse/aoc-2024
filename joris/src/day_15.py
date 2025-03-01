import colorama as cr

type Grid = list[list[str]]

def find_robot(grid: Grid) -> tuple[int, int]:
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == '@':
				return y, x

def print_grid(grid: Grid):
	for line in grid:
		for char in line:
			color = None
			match char:
				case '@': color = cr.Fore.RED
				case '#': color = cr.Fore.BLUE
				case 'O': color = cr.Fore.GREEN
				case '.': color = cr.Fore.WHITE
			print(color + char, end='')
		print()
	print()

def part_1(data: str) -> int:
	cr.init(autoreset=True)

	grid, moves = data.split('\n\n')
	grid = [list(line) for line in grid.split('\n')]
	moves = moves.replace('\n', '')
	ry, rx = find_robot(grid)

	for i, move in enumerate(moves):
		# == DEBUG ==
		# print(f'Iteration {i} (next: {move})')
		# print_grid(grid)

		dy, dx = 0, 0
		match move:
			case '^': dy = -1
			case '>': dx = 1
			case 'v': dy = 1
			case '<': dx = -1

		if grid[ry + dy][rx + dx] != '#':
			if grid[ry + dy][rx + dx] == 'O':
				y_off, x_off = dy, dx
				while grid[ry + y_off][rx + x_off] == 'O':
					y_off += dy
					x_off += dx
				if grid[ry + y_off][rx + x_off] == '.':
					grid[ry + y_off][rx + x_off] = 'O'
				else:
					continue
			grid[ry][rx] = '.'
			ry += dy
			rx += dx
			grid[ry][rx] = '@'

	return sum([
		y * 100 + x
		for y, line in enumerate(grid)
		for x, char in enumerate(line)
		if char == 'O'
	])

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')