"""
File: anagram.py
Name: Ester
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic_lst = []


def main():
    """
    # create a input word function
    # print all the anagrams for the word input by user
    """
    print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')
    read_dictionary()
    count = 0
    ####################
    while True:
        start = time.time()
        s = input('Find anagram for: ')
        if s == EXIT:
            break
        else:
            print('Searching...')
            ans_lst = find_anagrams(s)
            for ele in ans_lst:
                count += 1
                print('Found: ', ele)
                print('Searching...')
            print(len(ans_lst), ' anagrams: ', ans_lst)
            count = 0
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    # read dictionary and store data by a list
    global dic_lst
    with open(FILE, 'r') as f:
        dic_lst += [line.replace('\n', "") for line in f]
        # for line in f:
        #     token.append(line.replace('\n', ""))


def find_anagrams(s):
    """
    :param s: str, the input word
    :return: lst, append word if founded in the dictionary
    """
    return find_anagram_helper(s, "", [], len(s))


def find_anagram_helper(s, cur_s, lst, len_s):
    if len_s == len(cur_s):
        if cur_s in dic_lst:
            if cur_s not in lst:
                # print('Found: ', cur_s)
                # print('Searching...')
                lst.append(cur_s)
    else:
        for i in range(len(s)):
            cur_s += s[i]
        # for ch in s:
        #     cur_s += ch
            if has_prefix(cur_s):
                s1 = s[:i]+s[i+1:]
                find_anagram_helper(s1, cur_s, lst, len_s)
            cur_s = cur_s[:-1]
    return lst


def has_prefix(sub_s):
    """
    :param sub_s: str, the current searching word
    :return: boolean
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
