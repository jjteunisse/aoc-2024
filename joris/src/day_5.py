def solve(data: str, *, part: int) -> int:
	rules, updates = data.split('\n\n')
	rules = [rule.split('|') for rule in rules.split('\n')]
	updates = [update.split(',') for update in updates.split('\n')]

	rules_per_num = {}
	for rule in rules:
		before, after = rule
		if before not in rules_per_num: rules_per_num[before] = []
		if after not in rules_per_num: rules_per_num[after] = []
		rules_per_num[before].append(after)

	result = 0
	for update in updates:
		relevant_rules = {
			k: [x for x in v if x in update]
			for k, v in rules_per_num.items()
			if k in update
		}
		sort_key = lambda x: len(relevant_rules[x])
		update_sorted = sorted(update, key=sort_key, reverse=True)
		if part == 1 and update == update_sorted:
			result += int(update[len(update) // 2])
		elif part == 2 and update != update_sorted:
			result += int(update_sorted[len(update_sorted) // 2])

	return result

def run(data: str, parts: list[str]):
	if 'p1' in parts:
		print(f'The answer to part 1 is: {solve(data, part=1)}.')
	if 'p2' in parts:
		print(f'The answer to part 2 is: {solve(data, part=2)}.')