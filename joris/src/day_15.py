import colorama as cr

type Grid = list[list[str]]
type Point = tuple[int, int]

def find_robot(grid: Grid) -> Point:
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == '@':
				return y, x

def get_targets(grid: Grid, ry: int, rx: int, dy: int) -> list[Point]:
	todo = [(ry, rx)]
	targets = []
	while todo != []:
		ty, tx = todo[0]
		if grid[ty][tx] != '@':
			targets.append((ty, tx))

		ty += dy
		if grid[ty][tx] == '#':
			return []
		elif grid[ty][tx] == '[':
			if (ty, tx) not in todo:
				todo.append((ty, tx))
			if (ty, tx + 1) not in todo:
				todo.append((ty, tx + 1))
		elif grid[ty][tx] == ']':
			if (ty, tx - 1) not in todo:
				todo.append((ty, tx - 1))
			if (ty, tx) not in todo:
				todo.append((ty, tx))

		del todo[0]

	return targets

def print_grid(grid: Grid):
	for line in grid:
		for char in line:
			color = None
			match char:
				case '@': color = cr.Fore.RED
				case '.': color = cr.Fore.WHITE
				case '#': color = cr.Fore.BLUE
				case 'O' | '[' | ']': color = cr.Fore.GREEN
			print(color + char, end='')
		print()
	print()

def resize_grid(grid: Grid) -> Grid:
	new_grid = []
	for line in grid:
		new_line = []
		for char in line:
			match char:
				case '#': new_line += ['#', '#']
				case 'O': new_line += ['[', ']']
				case '@': new_line += ['@', '.']
				case '.': new_line += ['.', '.']
		new_grid.append(new_line)

	return new_grid

def solve(data: str, *, part: int) -> int:
	cr.init(autoreset=True)

	grid, moves = data.split('\n\n')
	grid = [list(line) for line in grid.split('\n')]
	if part == 2: grid = resize_grid(grid)
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

			elif grid[ry + dy][rx + dx] in '[]':
				if move in '><':
					x_off = dx
					while grid[ry][rx + x_off] in '[]':
						x_off += dx
					if grid[ry][rx + x_off] == '.':
						block = '[]' if move == '>' else ']['
						for x in range(dx, dx + x_off, dx):
							grid[ry][rx + x] = block[x % 2]
					else:
						continue

				elif move in '^v':
					targets = get_targets(grid, ry, rx, dy)
					if targets != []:
						for t in reversed(targets):
							ty, tx = t
							grid[ty + dy][tx] = grid[ty][tx]
							grid[ty][tx] = '.'
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
		if char in 'O['
	])

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part=1)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part=2)}.')