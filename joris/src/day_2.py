def is_safe(report: list[int]) -> bool:
	diffs = [i - j for i, j in zip(report[:-1], report[1:])]
	return (all([0 < d <  4 for d in diffs]) or
		    all([0 > d > -4 for d in diffs]))

def part_1(data: str) -> int:
	reports = [
		[int(num) for num in line.split(' ')]
		for line in data.split('\n')
	]
	return len([r for r in reports if is_safe(r)])

def part_2(data: str) -> int:
	reports = [
		[int(num) for num in line.split(' ')]
		for line in data.split('\n')
	]

	safe, unsafe = [], []
	for r in reports:
		(safe if is_safe(r) else unsafe).append(r)

	for report in unsafe:
		variants = [
			report[:i] + report[i + 1:]
			for i in range(len(report))
		]
		if any([is_safe(v) for v in variants]):
			safe.append(report)

	return len(safe)

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')