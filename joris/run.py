# (venv) > py run.py [day] [-cp] [-lp] [-p1] [-p2] [-t]

from cProfile import Profile
from line_profiler import LineProfiler
from os import listdir
from sys import argv, path
from time import time
from types import FunctionType

def cp(data: str, parts: list[str]):
	profiler = Profile()
	profiler.enable()
	module.run(data, parts)
	profiler.disable()
	print()
	profiler.print_stats(sort='tottime')

def lp(data: str, parts: list[str]):
	profiler = LineProfiler()
	for func in dir(module):
		if (
			isinstance(getattr(module, func), FunctionType) and
			not func.startswith('_')
		):
			profiler.add_function(getattr(module, func))
	profiler.enable()
	module.run(data, parts)
	profiler.disable()
	print()
	profiler.print_stats()

def show_ranking(ranking: list[tuple[int, str]]):
	ranking.sort(key=lambda tup: tup[1])
	total_runtime = sum([tup[1] for tup in ranking])
	print(f'\nRuntime ranking:')
	for i, tup in enumerate(ranking):
		print(f'Rank {i + 1:>02} - Day {tup[0]:>02} - {tup[1]:.3f} seconds.')
	print(' ' * 19 + '-' * 14)
	print(f'{' ' * 12} Total {total_runtime:.3f} seconds.')

if __name__ == '__main__':
	days = None
	if len(argv) > 1 and all([x.isdigit() for x in argv[1]]):
		days = [argv[1]]
	else:
		days = sorted([
			int(f[4:].split('.')[0])
			for f in listdir('src/')
			if f.startswith('day')
		])

	ranking = []
	for d in days:
		if len(days) > 1: print(f'\nRunning day {d}...')

		parts = ['p1', 'p2']
		if   '-p1' in argv: parts = ['p1']
		elif '-p2' in argv: parts = ['p2']

		env = 'tst' if '-t' in argv else 'prd'

		path.append('src')
		module = __import__(f'day_{d}')
		data = open(f'data/{env}/day_{d}.txt').read()
		if '-cp' in argv:
			cp(data, parts)
		elif '-lp' in argv:
			lp(data, parts)
		else:
			start = time()
			module.run(data, parts)
			runtime = time() - start
			ranking.append((d, runtime))
			print(f'Runtime: {runtime:.3f} seconds.')

	if len(days) > 1 and not ('-cp' in argv or '-lp' in argv):
		show_ranking(ranking)