from array import array
class ArrayQ(object):
    def __init__(self):
        '''
        Constructor that initializes an array type object that handles integers
        '''
        self._array = array('u')

    def enqueue(self, data):
        '''
        Method that appends an integer to the end of the arratý
        :param data an integer provided by user input:
        :return no return:
        '''
        self._array.append(data)

    def dequeue(self):
        '''
        Method that pops the first item in the array and returns it
        :return:
        '''
        data = self._array.pop(0)
        return data

    def isEmpty(self):
        '''
        Method that checks wether the list is empty or not, returns True if not empty, false otherwise
        :return:
        '''
        if len(self._array):
            return False
        else:
            return True










