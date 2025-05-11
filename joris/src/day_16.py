import colorama as cr

type Grid = list[list[str]]
type Point = tuple[int, int]

def find_char(grid: Grid, char_to_find: str) -> Point:
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == char_to_find:
				return y, x

def print_grid(grid: Grid):
	color = None
	for line in grid:
		for char in line:
			match char:
				case 'S': color = cr.Fore.RED
				case 'E': color = cr.Fore.GREEN
				case '#': color = cr.Fore.BLUE
				case '.': color = cr.Fore.WHITE
			print(color + char, end='')
		print()
	print()

def part_1(data: str) -> int:
	cr.init(autoreset=True)

	grid = [list(line) for line in data.split('\n')]
	sy, sx, sd = find_char(grid, 'S') + ('E',)
	ey, ex = find_char(grid, 'E')

	dirs = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
	scores = {
		(y, x): {d: None for d in dirs}
		for y in range(len(grid))
		for x in range(len(grid[0]))
		if grid[y][x] != '#'
	}

	todo = [(0, sy, sx, sd)]
	min_score = None
	while todo:
		# print(f'New iteration: {todo[0]} {len(todo)=}')
		score, y, x, d = todo.pop(0)

		if (y, x) == (ey, ex):
			if min_score == None or score < min_score:
				min_score = score
			continue

		if min_score != None and score > min_score:
			continue

		if scores[(y, x)][d] != None and score > scores[(y, x)][d]:
			continue

		scores[(y, x)][d] = score

		dy, dx = dirs[d]
		if grid[y + dy][x + dx] != '#':
			todo.append((score + 1, y + dy, x + dx, d))
		if d in ['N', 'S']:
			todo.append((score + 1000, y, x, 'W'))
			todo.append((score + 1000, y, x, 'E'))
		elif d in ['W', 'E']:
			todo.append((score + 1000, y, x, 'N'))
			todo.append((score + 1000, y, x, 'S'))

	return min_score

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')