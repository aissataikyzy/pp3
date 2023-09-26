def second_most_repeated_word(sequence):
	word_count = {}
	for word in sequence:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	max_freq = 0
	second_max_freq = -1
	for word, freq in word_count.items():
		if freq > max_freq:
			second_max_freq = max_freq
			max_freq = freq
		elif freq > second_max_freq and freq < max_freq:
			second_max_freq = freq
	for word, freq in word_count.items():
		if freq == second_max_freq:
			return word

sequence = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
print(second_most_repeated_word(sequence)) 
