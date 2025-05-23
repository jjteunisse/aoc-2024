def evolve(secret: int) -> int:
	secret ^= (secret << 6) & 0xFFFFFF
	secret ^= (secret >> 5) & 0xFFFFFF
	secret ^= (secret << 11) & 0xFFFFFF
	return secret

def part_1(data: str) -> int:
	secrets = [int(x) for x in data.split('\n')]

	for monkey_id, secret in enumerate(secrets):
		for _ in range(2000):
			secret = evolve(secret)
		secrets[monkey_id] = secret

	return sum(secrets)

def part_2(data: str) -> int:
	secrets = [int(x) for x in data.split('\n')]

	prices_per_seq = {}
	for monkey_id, secret in enumerate(secrets):
		seq, prev_price = (), 0
		for _ in range(2000):
			secret = evolve(secret)

			price = secret % 10
			diff = price - prev_price
			prev_price = price

			seq += (diff,)
			if len(seq) == 4:
				if seq not in prices_per_seq:
					prices_per_seq[seq] = {}
				if monkey_id not in prices_per_seq[seq]:
					prices_per_seq[seq][monkey_id] = price
				seq = seq[1:]

	return max([
		sum(prices.values())
		for seq, prices in prices_per_seq.items()
	])

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')