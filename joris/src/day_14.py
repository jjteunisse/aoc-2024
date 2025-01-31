from dataclasses import dataclass
from math import prod
import re

@dataclass
class Point:
	x: int
	y: int

@dataclass
class Robot:
	p: Point
	v: Point

	def move(self, dims: Point):
		self.p.x = (self.p.x + self.v.x) % dims.x
		self.p.y = (self.p.y + self.v.y) % dims.y

def part_1(data: str) -> int:
	robots = []
	for line in data.split('\n'):
		nums = [int(x) for x in re.findall(r'[-\d]+', line)]
		p = Point(x = nums[0], y = nums[1])
		v = Point(x = nums[2], y = nums[3])
		robots.append(Robot(p, v))

	dims = Point(x = 101, y = 103)
	for _ in range(100):
		for robot in robots:
			robot.move(dims)

	quad_dims = Point(x = dims.x // 2, y = dims.y // 2)
	quads = [0, 0, 0, 0]
	for robot in robots:
		if robot.p.x < quad_dims.x:
			if robot.p.y < quad_dims.y:
				quads[0] += 1
			elif robot.p.y > quad_dims.y:
				quads[1] += 1
		elif robot.p.x > quad_dims.x:
			if robot.p.y < quad_dims.y:
				quads[2] += 1
			elif robot.p.y > quad_dims.y:
				quads[3] += 1

	return prod(quads)

def part_2(data: str) -> int:
	# I checked the quads by hand, in search of anomalies;
	# the iteration below is the first anomaly not belonging
	# to the horizontal or vertical recurring patterns.
	return 7847

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')