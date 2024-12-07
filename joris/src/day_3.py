import re

def mul(instr: str) -> int:
	nums = [int(num) for num in re.findall(r'\d+', instr)]
	return nums[0] * nums[1]

def part_1(data: str) -> int:
	instructions = re.findall(r'mul\(\d+,\d+\)', data)
	return sum([mul(instr) for instr in instructions])

def part_2(data: str) -> int:
	instructions = re.findall(r'(?:mul\(\d+,\d+\)|do\(\)|don\'t\(\))', data)
	is_valid = True
	result = 0
	for instr in instructions:
		if instr == 'do()': is_valid = True
		elif instr == 'don\'t()': is_valid = False
		elif is_valid: result += mul(instr)
	return result

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')