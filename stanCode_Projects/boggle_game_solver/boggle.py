"""
File: boggle.py
Name: Ester
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# class TrieNode:
# 	def __init__(self):
# 		self.end = False
# 		self.children = {}
#
# class Trie:
# 	def __init__(self):
# 		self.ds = TrieNode()
#
# 	def insert(self, word):
# 		end = self.ds
# 		for ch in word:
# 			if ch not in end.children:
# 				end.children[ch] = TrieNode()
# 			end = end.children[ch]
# 		end.end = True


def main():
	"""
	TODO:
	"""
	###################
	word_lst = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	# word_lst = []
	# if not input_words(word_lst):
	# 	return

	start = time.time()
	# dict_lst = ['firm', 'form', 'foil', 'coif', 'coir']
	# count = 0
	dict_lst = read_dictionary()
	ans_lst = find_anagrams(dict_lst, word_lst)
	print(f'There are {len(ans_lst)} words in total')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagrams(dict_lst, word_lst):
	for x in range(len(word_lst)):
		for y in range(len(word_lst[0])):
			return helper(word_lst, dict_lst, "", x, y, [], [])


def helper(word_lst, dict_lst, cur_w, start_x, start_y, point_lst, ans_lst):
	# Base case
	if len(cur_w) >= 4:
		if cur_w in dict_lst:
			if cur_w not in ans_lst:
				ans_lst.append(cur_w)
				print(f'Found "{cur_w}"')
	# Recursive
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				point_x = start_x + i
				point_y = start_y + j
				if 0 <= point_x < len(word_lst) and 0 <= point_y < len(word_lst[0]):
					if (point_x, point_y) not in point_lst:
						# choose
						cur_w += word_lst[point_x][point_y]
						point_lst.append((point_x, point_y))
						# explore
						if has_prefix(cur_w, dict_lst):
							helper(word_lst, dict_lst, cur_w, point_x, point_y, point_lst, ans_lst)
						# un-choose
						cur_w = cur_w[:-1]
						point_lst.pop()
	return ans_lst


def input_words(word_lst):
	for i in range(4):
		row_lst = []
		row_word = input(f'{i + 1} row of letters: ').lower().strip().split()
		for ch in row_word:
			if len(ch) == 1 and ch.isalpha():
				row_lst.append(ch)
			else:
				print('Illegal')
				return
		word_lst.append(row_lst)
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	lst = []
	with open(FILE, 'r') as f:
		lst += [line.replace('\n', '') for line in f]
	return lst


def has_prefix(sub_s, dict_lst):
	"""
	:param dict_lst: (lst) words in "dictionary.txt"
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
