def evolve(secret: int) -> int:
	secret = (secret ^ secret << 6) & 0xFFFFFF
	secret = (secret ^ secret >> 5) & 0xFFFFFF
	secret = (secret ^ secret << 11) & 0xFFFFFF
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
		seq, price = tuple(), 0
		for _ in range(2000):
			new_secret = evolve(secret)
			new_price = new_secret % 10

			diff = new_price - price
			seq = ((diff,) + seq)[:4]
			if seq not in prices_per_seq:
				prices_per_seq[seq] = {}
			if monkey_id not in prices_per_seq[seq]:
				prices_per_seq[seq][monkey_id] = new_price

			secret, price = new_secret, new_price

	return max([sum(prices.values()) for seq, prices in prices_per_seq.items()])

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {part_1(data)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {part_2(data)}.')