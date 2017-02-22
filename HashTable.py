"""
A HashTable class that is thought to be my interpretation of pythons dict. It works by storing several HashNodes in a
list. It has methods for searching the list for keys and hashing values to store nodes at the right places.
A lot slower than pythons dict.
"""
from HashNode import *


class HashTable:
    def __init__(self):
        self.size = 2340937
        self.slots = [None]*self.size

    def hash_string(self, key):
        """
        Method for hashing that splits the key into its characters, then adds their values*(pos+1) to avoid
        anagram collisions
        :param key: the key we want to hash
        :return:  returns the hash value of that key
        """
        temp_value = 0
        for pos in range(len(key)):
            temp_value += (ord(key[pos])*(pos+1))**2

        return temp_value % self.size

    def store(self, key, data):
        """
        Method for storing HashNodes in the right space within the hash table. Checks for collisions and avoids them
        using quadratic probing.
        :param key: the key we want to store under
        :param data: the data we want to store under that key
        :return: no return
        """
        hash_value = self.hash_string(key)
        i = 1
        nextslot = hash_value
        while self.slots[nextslot] is not None:
            if self.slots[nextslot] is not key:
                nextslot = self.rehash(nextslot+(i*i))
                i += 1
        if self.slots[nextslot] is None:
            node = HashNode(key)
            self.slots[nextslot] = node
            node.data.append(data)
        else:
            self.slots[nextslot].data.append(data)  #append to the list in the right place

    def rehash(self, pos):
        """
        Method that rehashes an existing hash value
        :param pos: the existing hash value
        :return: returns old hash value % size of the hash table
        """
        return pos % self.size

    def hash_search(self, key):
        """
        Method that searches the hash table for the supplied key, uses the same structure for searching if not found
        in the expected place as
        :param key:
        :return:
        """
        hash_index = self.hash_string(key)
        next_slot = hash_index
        i = 1
        while self.slots[next_slot] is not None:

            if self.slots[next_slot].key == key:
                return self.slots[next_slot].data
            next_slot = self.rehash(next_slot+(i*i))
            i += 1
        raise KeyError



