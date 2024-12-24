def solve(data: str, *, n_blinks: int) -> int:
	stones = {int(x): 1 for x in data.split(' ')}
	known = {0: [1]}
	for _ in range(n_blinks):
		new_stones = {}
		for stone, n in stones.items():
			if stone not in known:
				d, m = divmod(len(str(stone)), 2)
				if m % 2 == 0:
					known[stone] = [int(str(stone)[:d]), int(str(stone)[d:])]
				else:
					known[stone] = [stone * 2024]

			for k in known[stone]:
				if k not in new_stones:
					new_stones[k] = n
				else:
					new_stones[k] += n

		stones = new_stones

	return sum(stones.values())

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, n_blinks=25)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, n_blinks=75)}.')