def get_lists(data: str) -> tuple[list[int], list[int]]:
	left, right = [], []
	for line in data.split('\n'):
		nums = line.split('   ')
		left.append(int(nums[0]))
		right.append(int(nums[1]))
	return left, right

def part_1(data: str) -> int:
	left, right = get_lists(data)
	matches = zip(sorted(left), sorted(right))
	diff = [abs(l - r) for l, r in matches]
	return sum(diff)

def part_2(data: str) -> int:
	left, right = get_lists(data)
	counts = {num: right.count(num) for num in set(left) | set(right)}
	scores = [num * counts[num] for num in left]
	return sum(scores)

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')