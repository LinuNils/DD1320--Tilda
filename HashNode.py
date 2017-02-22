"""
The HashNode class used in HashTable class, it has 2 data fields. One that holds the key and the other a list that
is used for storing data associated with that key. Also has a string representation method for it's key.
"""


class HashNode:
    """
    Class that has 2 data fields, one named key that stores the key
    the other is a list called data that stores all objects associated with that key
    """
    def __init__(self, key):
        self.key = key
        self.data = []

    def __str__(self):
        """
        method that returns the key associated with the node
        :return: self.key
        """
        return self.key
