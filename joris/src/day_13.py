import re
import sympy as sp

def solve(data: str, *, part: int) -> int:
	total_cost = 0
	for block in data.split('\n\n'):
		ax, ay, bx, by = [int(x) for x in re.findall(r'\+(\d+)', block)]
		xt, yt = [int(x) for x in re.findall(r'=(\d+)', block)]

		if part == 1:
			i = 0
			while xt >= 0 and yt >= 0:
				if xt % ax == 0 and yt % ay == 0 and xt // ax == yt // ay:
					total_cost += (xt // ax) * 3 + i
					break
				xt -= bx
				yt -= by
				i += 1

		elif part == 2:
			xt += int(1E13)
			yt += int(1E13)
			a, b = sp.symbols('a, b')
			result = sp.solve(
				[a * ax + b * bx - xt, a * ay + b * by - yt],
				a, b
			)
			if (
				isinstance(result[a], sp.core.numbers.Integer) and
				isinstance(result[b], sp.core.numbers.Integer)
			):
				total_cost += 3 * result[a] + result[b]

	return total_cost

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part=1)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part=2)}.')