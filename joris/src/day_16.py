import colorama as cr
import sys

type Grid = list[list[str]]
type Point = tuple[int, int]

def find_char(grid: Grid, query: str) -> Point:
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char == query:
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

	dirs = {
		'N': (-1, 0), 'S': (1, 0),
		'W': (0, -1), 'E': (0, 1),
	}
	turn_dirs = {
		'N': ['W', 'E'], 'S': ['W', 'E'],
		'W': ['N', 'S'], 'E': ['N', 'S'],
	}

	min_scores = {
		(y, x): {d: sys.maxsize for d in dirs}
		for y in range(len(grid))
		for x in range(len(grid[0]))
		if grid[y][x] != '#'
	}
	min_end_score = sys.maxsize

	todo = [(sy, sx, sd, 0)]
	while todo:
		y, x, d, score = todo.pop(0)
		if score < min_end_score and score < min_scores[(y, x)][d]:
			min_scores[(y, x)][d] = score
			if (y, x) == (ey, ex):
				min_end_score = score
			else:
				dy, dx = dirs[d]
				if grid[y + dy][x + dx] != '#':
					todo.append((y + dy, x + dx, d, score + 1))
				for td in turn_dirs[d]:
					todo.append((y, x, td, score + 1000))

	return min_end_score

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')