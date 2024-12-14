# (venv) > py run.py <day> [-cp] [-lp] [-p1] [-p2] [-t]

from cProfile import Profile
from line_profiler import LineProfiler
from sys import argv, path
from time import time
from types import FunctionType

if __name__ == '__main__':
	day = f'day_{argv[1]}'
	env = 'tst' if '-t' in argv else 'prd'

	parts = ['p1', 'p2']
	if   '-p1' in argv: parts.remove('p2')
	elif '-p2' in argv: parts.remove('p1')

	path.append('src')
	module = __import__(day)
	data = open(f'data/{env}/{day}.txt').read()
	if '-cp' in argv:
		profiler = Profile()
		profiler.enable()
		module.run(data, parts)
		profiler.disable()
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
		profiler.print_stats()
	else:
		start = time()
		module.run(data, parts)
		print(f'Total runtime: {time() - start:.3f} seconds.')