# > py run.py [-cp] [-d<day>] [-lp] [-p<part>] [-t]

from cProfile import Profile
from line_profiler import LineProfiler
from sys import argv, path
from time import time

if __name__ == '__main__':
	day = next((x[1:] for x in argv if x.startswith('-d')), 'd1')
	parts = next(([x[1:]] for x in argv if x.startswith('-p')), ['p1', 'p2'])
	env = 'tst' if '-t' in argv else 'prd'

	path.append('src')
	data = open(f'data/{env}/{day}.txt').read()

	module = __import__(day)
	if '-cp' in argv:
		profiler = Profile()
		profiler.enable()
		module.run(data, parts)
		profiler.disable()
		profiler.print_stats(sort='tottime')
	elif '-lp' in argv:
		profiler = LineProfiler()
		for func in dir(module):
			if not func.startswith('_'):
				profiler.add_function(getattr(module, func))
		profiler.enable()
		module.run(data, parts)
		profiler.disable()
		profiler.print_stats()
	else:
		start = time()
		module.run(data, parts)
		print(f'Total runtime: {time() - start:.3f} seconds.')