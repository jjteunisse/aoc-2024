from bisect import insort
from collections import defaultdict
from itertools import pairwise

Regions = list[tuple[int, int, list[str, ...]]]

def get_regions(data: str) -> Regions:
	grid = [list(line) for line in data.split('\n')]
	y_max, x_max = len(grid), len(grid[0])

	regions = []
	todo_global = [(y, x) for y in range(y_max) for x in range(x_max)]
	while todo_global != []:
		region = []
		todo_local = {todo_global[0]}
		done_local = []
		while todo_local != set():
			y, x = todo_local.pop()
			done_local.append((y, x))
			todo_global.remove((y, x))

			borders = []
			if y == 0 or grid[y - 1][x] != grid[y][x]:
				borders.append('N')
			elif (y - 1, x) not in done_local:
				todo_local.add((y - 1, x))

			if x == x_max - 1 or grid[y][x + 1] != grid[y][x]:
				borders.append('E')
			elif (y, x + 1) not in done_local:
				todo_local.add((y, x + 1))

			if y == y_max - 1 or grid[y + 1][x] != grid[y][x]:
				borders.append('S')
			elif (y + 1, x) not in done_local:
				todo_local.add((y + 1, x))

			if x == 0 or grid[y][x - 1] != grid[y][x]:
				borders.append('W')
			elif (y, x - 1) not in done_local:
				todo_local.add((y, x - 1))

			region.append((y, x, borders))

		regions.append(region)

	return regions

def part_1(regions: Regions) -> int:
	return sum([
		len(region) * sum([len(plot[2]) for plot in region])
		for region in regions
	])

def part_2(regions: Regions) -> int:
	result = 0
	for region in regions:
		sides = 0
		direction_borders = {d: defaultdict(list) for d in ['N', 'E', 'S', 'W']}
		for plot in region:
			y, x, borders = plot
			for d in borders:
				k, v = (y, x) if d in ['N', 'S'] else (x, y)
				insort(direction_borders[d][k], v)

		sides = 0
		for db in direction_borders.values():
			for k, v in db.items():
				sides += 1
				for v1, v2 in pairwise(v):
					if v2 != v1 + 1:
						sides += 1

		result += len(region) * sides

	return result

def run(data: str, parts: list[str]):
	regions = get_regions(data)
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(regions)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(regions)}.')