from bisect import insort_left

N_DIGITS = 10

class Block:
	def __init__(self, _start: int, _size: int, _id: int):
		self.start, self.size, self.id = _start, _size, _id

	def __lt__(self, other): return self.start < other.start

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
	free = {int(i): [] for i in range(N_DIGITS)}
	used = []
	start = 0
	for i, digit in enumerate(data):
		size = int(digit)
		if i % 2 == 0:
			used.append(Block(start, size, i // 2))
		else:
			free[size].append(Block(start, size, None))
		start += size

	result = 0
	for used_block in reversed(used):
		target_block = None
		for i in range(used_block.size, N_DIGITS):
			if (
				free[i] != [] and
				free[i][0].start < used_block.start and
				(target_block is None or free[i][0].start < target_block.start)
			):
				target_block = free[i][0]

		if target_block is not None:
			used_block.start = target_block.start
			if target_block.size != used_block.size:
				new_block = Block(
					target_block.start + used_block.size,
					target_block.size - used_block.size,
					target_block.id
				)
				insort_left(free[new_block.size], new_block)
			del free[target_block.size][0]

		for i in range(used_block.size):
			result += (used_block.start + i) * used_block.id

	return result

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')