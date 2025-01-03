def part_1(data: str) -> int:
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

			n_borders = 0
			if y == 0 or grid[y - 1][x] != grid[y][x]:
				n_borders += 1
			elif (y - 1, x) not in done_local:
				todo_local.add((y - 1, x))

			if y == y_max - 1 or grid[y + 1][x] != grid[y][x]:
				n_borders += 1
			elif (y + 1, x) not in done_local:
				todo_local.add((y + 1, x))

			if x == 0 or grid[y][x - 1] != grid[y][x]:
				n_borders += 1
			elif (y, x - 1) not in done_local:
				todo_local.add((y, x - 1))

			if x == x_max - 1 or grid[y][x + 1] != grid[y][x]:
				n_borders += 1
			elif (y, x + 1) not in done_local:
				todo_local.add((y, x + 1))

			region.append((grid[y][x], (y, x), n_borders))

		regions.append(region)

	return sum([len(r) * sum([tup[2] for tup in r]) for r in regions])

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')