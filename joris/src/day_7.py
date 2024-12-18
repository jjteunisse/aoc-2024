def check_subeq(test: int, result: int, nums: list[int], concat: bool) -> bool:
	if nums == []:
		return result == test
	elif result > test:
		return False
	else:
		return (
			check_subeq(test, result + nums[0], nums[1:], concat) or
			check_subeq(test, result * nums[0], nums[1:], concat) or
			(
				concat and
				check_subeq(test, int(f'{result}{nums[0]}'), nums[1:], concat)
			)
		)

def solve(data: str, *, concat: bool) -> int:
	result = 0
	for i, line in enumerate(data.split('\n')):
		test, nums = line.split(': ')
		test = int(test)
		nums = [int(x) for x in nums.split(' ')]

		if check_subeq(test, nums[0], nums[1:], concat):
			result += test

	return result

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, concat=False)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, concat=True)}.')