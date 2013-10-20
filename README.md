bananagram
==========

Hosted app can be found at http://secure-mountain-8277.herokuapp.com/

When the Heroku dyno spins up, this app calculates a trie from a list of 230,000 words and stores it in memory. Then, given a string, it recursively searches the trie for any words that are substrings of that string.