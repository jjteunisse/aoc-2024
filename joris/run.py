# (venv) > py run.py [day] [-cp] [-lp] [-p1] [-p2] [-t]

from cProfile import Profile
from line_profiler import LineProfiler
from os import listdir
from sys import argv, path
from time import time
from types import FunctionType

if __name__ == '__main__':
	days = sorted([
		int(f[4:].split('.')[0])
		for f in listdir('src/')
		if f.startswith('day')
	])

	if len(argv) > 1 and all([x.isdigit() for x in argv[1]]):
		days = [argv[1]]

	ranking = []
	for d in days:
		if len(days) > 1:
			print(f'\nRunning day {d}...')

		env = 'tst' if '-t' in argv else 'prd'

		parts = ['p1', 'p2']
		if   '-p1' in argv: parts.remove('p2')
		elif '-p2' in argv: parts.remove('p1')

		path.append('src')
		module = __import__(f'day_{d}')
		data = open(f'data/{env}/day_{d}.txt').read()
		if '-cp' in argv:
			profiler = Profile()
			profiler.enable()
			module.run(data, parts)
			profiler.disable()
			print()
			profiler.print_stats(sort='tottime')
		elif '-lp' in argv:
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
		else:
			start = time()
			module.run(data, parts)
			runtime = time() - start
			ranking.append((d, runtime))
			print(f'Runtime: {runtime:.3f} seconds.')

	if len(days) > 1 and '-cp' not in argv and '-lp' not in argv:
		ranking.sort(key=lambda tup: tup[1])
		total_runtime = sum(tup[1] for tup in ranking)
		print(f'\nRuntime ranking:')
		for i, tup in enumerate(ranking):
			print(f'Rank {i + 1:>02} - Day {tup[0]:>02} - {tup[1]:.3f} seconds.')
		print(' ' * 19 + '-' * 14)
		print(f'{' ' * 12} Total {total_runtime:.3f} seconds.')