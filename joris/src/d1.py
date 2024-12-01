def part_1(data):
	for i in range(1000):
		print(data, i, end='\r')

def part_2(data):
	for i in range(10000):
		print(data, i, end='\r')

def run(data, parts):
	if 'p1' in parts: part_1(data)
	if 'p2' in parts: part_2(data)