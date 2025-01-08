import re
import sympy as sp

def solve(data: str, *, part: int) -> int:
	total_cost = 0
	for block in data.split('\n\n'):
		ax, ay, bx, by, x, y = [int(x) for x in re.findall(r'\d+', block)]
		if part == 2: x, y = x + int(1E13), y + int(1E13)

		a, b = sp.symbols('a, b')
		result = sp.solve([a * ax + b * bx - x, a * ay + b * by - y], a, b)
		if type(result[a]) == type(result[b]) == sp.core.numbers.Integer:
			total_cost += 3 * result[a] + result[b]

	return total_cost

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part=1)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part=2)}.')