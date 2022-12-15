#!/usr/bin/python

def replace_letters(word, letters, positions):

	ret = list(word)
	for i in range(0, len(positions)):
		ret[positions[i]] = letters[i]
	return ''.join(ret)

def every_permutation(word):

	if len(word) < 2:
		return word
	l = []
	for i in range(0, len(word)):
		m = word[i]
		remaining = str(word[:i]) + str(word[i + 1:])
		for p in every_permutation(remaining):
			l.append(m + p)
	return l

def transform(grid, word, positions, valid_words=[]):

	ret = []
	for letters in every_permutation(word):
		possible_grid = replace_letters(grid, letters, positions)
		if len(valid_words) == 0:
			ret.append(possible_grid)
		else:
			if ((possible_grid[0:3] in valid_words) & (possible_grid[3:6] in valid_words) & (possible_grid[6:] in valid_words)):
				ret.append(possible_grid)
	return ret

grid = 'FORMATION'

transformations = [
	['PART', [1, 3, 6]],
	['EYES', [4, 8]],
	['UNCURL', [0, 5, 7]]
]

words3 = []
words9 = []

# words.txt needs to exist, and contain a list of valid English words. All words that don't have three or nine letters are ignored.
# A good place to get such a list is https://github.com/dwyl/english-words

with open('words.txt', 'r') as fp:
	for word_enc in fp.readlines():
		word = word_enc.strip().upper().replace("'", "").replace(".", "").replace("-", "")
		if len(word) == 3:
			words3.append(word)
		if len(word) == 9:
			if word[2] == 'R': # We can cheat a bit, as we know the third letter has to be 'R'
				words9.append(word)

progress = [grid]

for t in transformations:
	new_progress = []
	for g in progress:
		new_progress = new_progress + transform(g, t[0], t[1], words3)
	progress = new_progress

possible_solutions = []
for possible_solution in progress:

	if not(possible_solution in words9): # Don't add if it's not a valid word
		continue
	if possible_solution in possible_solutions: # Don't add if we've already added it
		continue

	possible_solutions.append(possible_solution)

print(possible_solutions) # Hopefully we have just one item in our list!
