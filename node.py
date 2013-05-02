class Node(object):
    def __init__(self, value='', valid_word=False, depth=0):
        #empty dict to store child nodes
        self.children = {}
        # What is the value of this node? One letter
        self.value = value
        # Store whether or not this is a leaf node
        self.valid_word = valid_word
        self.depth = depth

    def add_word(self, word):
        """Add a word to the trie"""
        current_node = self
        for index, letter in enumerate(word, start=1):
            if letter not in current_node.children.keys():
                current_node.children[letter] = Node(value=letter,
                                                     depth=index)
            current_node = current_node.children[letter]
            if len(word) == index:
                current_node.valid_word = True

    def is_word(self, word):
        current_node = self
        for letter in word:
            try:
                current_node = current_node.children[letter]
            except KeyError:
                return False
        return current_node.valid_word

    def fill(self, filename='dictionary.txt'):
        with open(filename, 'r') as f:
            for line in f:
                self.add_word(line.strip())

    def find_substrings(self, string):
        """Recursively find all valid words that can be spelled by picking out
        letters of a given string"""
        self.word_list = []
        beginning_node = self
        self._anagram_finder(beginning_node,
                             prefix_string="",
                             remainder_letters=sorted(string))
        return self.word_list

    def _anagram_finder(self, node, prefix_string="", remainder_letters=""):
        current_node = node
        for index, letter in enumerate(remainder_letters):
            if index > 0 and letter == remainder_letters[index-1]:
                # If this letter is the same as the previous letter, then
                # skip because we've already checked this letter
                continue
            # Try each one of the "remainder letters" against the prefix string
            # to see if any of the remainder letters are children of the
            # node that represents your prefix string
            if letter in current_node.children.keys():
                next_node = current_node.children[letter]
                if next_node.valid_word:
                    word = prefix_string + letter
                    if word not in self.word_list:
                        self.word_list.append(word)
                # pop letter out of "remainder letters"
                # add letter to the end of prefix string
                # recursively call _anagram_finder
                new_prefix_string = prefix_string + letter
                new_remainder_letters = (remainder_letters[:index] +
                                         remainder_letters[index+1:])
                if new_remainder_letters:
                    self._anagram_finder(next_node,
                                         prefix_string=new_prefix_string,
                                         remainder_letters=new_remainder_letters)
                else:
                    return
