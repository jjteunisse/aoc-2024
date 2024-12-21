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
	blocks = []
	for i, digit in enumerate(data):
		if i % 2 == 0:
			blocks.append([str(i // 2), int(digit)])
		else:
			blocks.append(['.', int(digit)])

	i = len(blocks) - 1
	while i > 0:
		if blocks[i][0] != '.':
			j = 0
			while j < i:
				if blocks[j][0] == '.':
					if blocks[j][1] == blocks[i][1]:
						blocks[i], blocks[j] = blocks[j], blocks[i]
						break
					elif blocks[j][1] > blocks[i][1]:
						blocks[j][1] -= blocks[i][1]
						blocks.insert(j, blocks[i][:])
						blocks[i+1][0] = '.'
						break
				j += 1
		i -= 1

	result = []
	for b in blocks: result += [b[0]] * b[1]

	return sum([i * int(x) for i, x in enumerate(result) if x != '.'])

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')