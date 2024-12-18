def check_subeq(test: int, nums: list[int], p2: bool) -> bool:
	if len(nums) == 1:
		return test == nums[0]
	elif test < 0:
		return False
	else:
		if check_subeq(test - nums[-1], nums[:-1], p2):
			return True

		d, m = divmod(test, nums[-1])
		if m == 0 and check_subeq(d, nums[:-1], p2):
			return True

		if p2:
			d, m = divmod(test, 10 ** len(str(nums[-1])))
			return m == nums[-1] and check_subeq(d, nums[:-1], p2)

def solve(data: str, *, p2: bool) -> int:
	result = 0
	for line in data.split('\n'):
		test, nums = line.split(': ')
		test = int(test)
		nums = [int(x) for x in nums.split(' ')]

		if check_subeq(test, nums, p2):
			result += test

	return result

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, p2=False)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, p2=True)}.')