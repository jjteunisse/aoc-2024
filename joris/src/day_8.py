def solve(data: str, *, part_1: bool) -> int:
	grid = [list(line) for line in data.split('\n')]

	nodes = {}
	for y, line in enumerate(grid):
		for x, char in enumerate(line):
			if char != '.':
				if char not in nodes:
					nodes[char] = []
				nodes[char].append((y, x))

	y_max, x_max = len(grid), len(grid[0])
	antinodes = []
	for node_type in nodes:
		for y_self, x_self in nodes[node_type]:
			for y_other, x_other in nodes[node_type]:
				if (y_self, x_self) != (y_other, x_other):
					y_mirror, x_mirror = y_self, x_self
					if part_1:
						y_mirror += y_self - y_other
						x_mirror += x_self - x_other

					while 0 <= y_mirror < y_max and 0 <= x_mirror < x_max:
						if (y_mirror, x_mirror) not in antinodes:
							antinodes.append((y_mirror, x_mirror))

						if part_1: break

						y_mirror += y_self - y_other
						x_mirror += x_self - x_other

	return len(antinodes)

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part_1=True)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part_1=False)}.')