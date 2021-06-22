"""
File: anagram.py
Name: Kevin Chen
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

I'm too busy this week QQ.
Sorry for not having enough time to prune the recursive calls.
"""
import time

# Constants
FILE = 'dict/dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Create empty list to load data.
dictionary = []
total_list = []

def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    s = input('Find anagrams for: ')
    while True:
        if s == '-1':
            break
        else:
            print('Searching...')
            find_anagrams(s)
            s = input('Find anagrams for: ')


def read_dictionary():
    # load data into the dictionary(list) word by word
    global dictionary
    with open(FILE, 'r') as f:
        for word in f:
            dictionary += word.split('\n')


def find_anagrams(s):
    """
    :param s: str, the string to be searched for anagrams.
    """
    global total_list
    start = time.time()
    read_dictionary()
    string_lst = []
    # split the string by character and load into string_list
    for ch in s:
        string_lst.append(ch)
    # Call helper
    helper(string_lst, [])
    # print all anagrams found(loaded by total_list) when it got out of helper, then empty total_list
    print(len(total_list), 'anagrams:', total_list)
    total_list = []
    end = time.time()

    # print out the time consumed
    print('Time consumed:', end-start)


def helper(lst, current_lst):
    if len(lst) == len(current_lst):
        if ''.join(current_lst) in dictionary and ''.join(current_lst) not in total_list:
            # Base Case
            print('Found:', ''.join(current_lst))
            total_list.append(''.join(current_lst))
            print('Searching...')

    else:
        if has_prefix(current_lst):
            # Recursive calls
            for i in range(len(lst)):
                if lst.count(lst[i]) > current_lst.count(lst[i]):
                    # Choose
                    current_lst.append(lst[i])
                    # Explore
                    helper(lst, current_lst)
                    # Un-choose
                    current_lst.pop()


def has_prefix(sub_lst):
    """
    :param sub_lst:(list) a string list that is constructed by characters
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    sub_s = ''.join(sub_lst)
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
