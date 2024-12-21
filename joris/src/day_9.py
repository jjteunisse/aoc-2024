def part_1(data: str) -> int:
	result = []
	for i, digit in enumerate(data):
		if i % 2 == 0:
			result += int(digit) * [str(i // 2)]
		else:
			result += int(digit) * ['.']

	j = len(result) - 1
	for i, content in enumerate(result):
		if content == '.':
			while result[j] == '.':
				j -= 1
			if j > i:
				result[i] = result[j]
				result[j] = '.'
			else:
				break

	return sum([i * int(x) for i, x in enumerate(result) if x != '.'])

def part_2(data: str) -> int:
	pass

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')