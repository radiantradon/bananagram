from flask import Flask
app = Flask(__name__)

import bananagram.views

from node import Node
# Initialize the node, i.e. fill in the trie with our word list
# We do this in __init__.py so that the word list will only have to regenerate
# when the server restarts
trie = Node()
trie.fill(filename="sun_dictionary.txt")

