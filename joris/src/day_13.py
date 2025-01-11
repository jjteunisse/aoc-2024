import re

def solve(data: str, *, part: int) -> int:
	result = 0
	for block in data.split('\n\n'):
		ax, ay, bx, by, x, y = [int(x) for x in re.findall(r'\d+', block)]

		if part == 2:
			x, y = x + int(1E13), y + int(1E13)

		ad, am = divmod(x * by + y * -bx, ax * by + ay * -bx)
		if am == 0:
			bd, bm = divmod(x - ad * ax, bx)
			if bm == 0:
				result += 3 * ad + bd

	return result

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part=1)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part=2)}.')