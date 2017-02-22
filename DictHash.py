"""
DictHash class that uses pythons dict as it's data, then stores data under corresponding keys.
Also methods for searching and entering new values in the hash table.
"""

class DictHash:
    """
    Class that is made up out of pythons dict
    """
    def __init__(self):
        self.dict = {}

    def search(self, key):
        """
        search by returning a key, excepts key error and returns 404
        :param key:
        :return: the value at the key or error message
        """
        try:
            return self.dict[key]
        except KeyError:
            return 404

    def store(self, key, value):
        """
        Method for storing in the dictionary, creates lists under the key to be able to store multiple values
        :param key: the key we want store at
        :param value: the value we want to store under the key
        :return: no return
        """
        if key in self.dict:
            self.dict[key].append(value)
        else:
            self.dict[key] = []
            self.dict[key].append(value)

    def __getitem__(self, item):
        """
        search method that enables the use of dict[key] instead of search
        :param item: the key we are searching for
        :return: the value/values at the key or error message
        """
        try:
            return self.dict[item]
        except KeyError:
            return 404
