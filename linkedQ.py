class Node(object):
    def __init__(self):
        '''
        An Node object in a queue, _data contains user provided input and _next points toward the next object in the
        queue.
        '''
        self._data = None
        self._next = None


class LinkedQ(object):
    def __init__(self):
        '''
        An LinkedQ object for keeping track of the first and last objects in a queue.
        Attributes _first and _last points to Node objects in the queue.
        '''
        self._first = None
        self._last = None

    def enqueue(self, data):
        '''
        Queueing method, checks wether there is an existing queue or not
        if there it creates an Node object and adds it to the end of the list, moves next pointer of the object before
        to point to the new node object, and points the last pointer to the new object.
        If empty it creates an Node object and sets both last and first pointer to point towards that object.
        :param data provided by the call to this method:
        :return no return:
        '''
        if self.isEmpty():
            node = Node()
            node._data = data
            node._next = None
            self._first = node
            self._last = node
        else:
            node = Node()
            node._data = data
            node._next = None
            self._last._next = node
            self._last = node

    def dequeue(self):
        '''
        sets data to the data-segment of the first node.
        Sets the first-pointer to point to the second object in the list
        :return returns the data from the first node:
        '''
        data = self._first._data
        self._first = self._first._next
        return data

    def isEmpty(self):
        '''
        Checks wether the first node points to something or not, if not it returns False else True.
        :return False or True:
        '''
        if self._first == None:
            return True
        else:
            return False

