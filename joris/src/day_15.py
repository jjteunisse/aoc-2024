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
		print(f'Iteration {i} (next: {move})')
		print_grid(grid)
		if move == '<':
			if grid[ry][rx - 1] in ['.', 'O']:
				if grid[ry][rx - 1] == 'O':
					x_off = 2
					while grid[ry][rx - x_off] == 'O':
						x_off += 1
					if grid[ry][rx - x_off] == '.':
						grid[ry][rx - x_off] = 'O'
					else:
						continue
				grid[ry][rx] = '.'
				rx -= 1
				grid[ry][rx] = '@'
		elif move == '^':
			if grid[ry - 1][rx] in ['.', 'O']:
				if grid[ry - 1][rx] == 'O':
					y_off = 2
					while grid[ry - y_off][rx] == 'O':
						y_off += 1
					if grid[ry - y_off][rx] == '.':
						grid[ry - y_off][rx] = 'O'
					else:
						continue
				grid[ry][rx] = '.'
				ry -= 1
				grid[ry][rx] = '@'
		elif move == '>':
			if grid[ry][rx + 1] in ['.', 'O']:
				if grid[ry][rx + 1] == 'O':
					x_off = 2
					while grid[ry][rx + x_off] == 'O':
						x_off += 1
					if grid[ry][rx + x_off] == '.':
						grid[ry][rx + x_off] = 'O'
					else:
						continue
				grid[ry][rx] = '.'
				rx += 1
				grid[ry][rx] = '@'
		elif move == 'v':
			if grid[ry + 1][rx] in ['.', 'O']:
				if grid[ry + 1][rx] == 'O':
					y_off = 2
					while grid[ry + y_off][rx] == 'O':
						y_off += 1
					if grid[ry + y_off][rx] == '.':
						grid[ry + y_off][rx] = 'O'
					else:
						continue
				grid[ry][rx] = '.'
				ry += 1
				grid[ry][rx] = '@'

	result = 0
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == 'O':
				result += y * 100 + x

	return result

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')