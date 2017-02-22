class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
        self.root=putta(self.root,newvalue)

    def __contains__(self, value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")


class Node(object):
    '''
    Class that keeps pointers to the object to the left of it and the right of it
    contains data that the user sets from functions outside the class.
    '''
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


def putta(root_object, value):
    '''
    Function that inserts and creates objects at their respective places
    uses a recursive while loop that checks if there is a node or not at the place we are currently at, then compares
    the input value against the value stored at that spot. Continues in different directions of the tree given that it
    is either greater than or less than.
    :param root_object: A root-pointer to keep track of the start of the tree
    :param value: The value we want to insert into the tree
    :return: returns a pointer to the root
    '''
    if root_object == None:
        # if there is no root object we create one
        new_node = Node()
        new_node.data = value
        root_object = new_node
    node = root_object
    # While there is a node we check wether we should put our value to the right or to the left.
    # If there is already an value stored with the same as the input we break the loop
    if value.lower() > node.data.lower():
        if node.right == None:
            new_node = Node()
            new_node.data = value
            node.right = new_node
        else:
            putta(node.right, value)

    #elif value.lower() == node.data.lower():
        #pass
    else:
        if node.left == None:
            new_node = Node()
            new_node.data = value
            node.left = new_node
        else:
            putta(node.left, value)
    return root_object


def finns(root_object, value):
    '''
    Function that steps through the tree looking for the value returns true or false
    :param root_object: Pointer to the root
    :param value: The value we are looking for
    :return: True or False
    '''
    if root_object == None:
        return False
    node = root_object
    result = comparison(value, node.data)
    if result == 1:
        if node.right == None:
            return False
        else:
            return finns(node.right, value)
    elif result == 0:
        return True
    #elif value.lower() < node.data.lower():
        #if node.left == None:
            #return False
        #else:
            #finns(node.left, value)
    else:
        if node.left == None:
            return False
        else:
            return finns(node.left, value)




def skriv(root_object):
    '''
    Function that prints the tree inorder.
    :param root_object: a root-pointer to keep track of where the tree starts
    :return: each objects data
    '''
    node = root_object
    if node.left:
        skriv(node.left)
    print(node.data)
    if node.right:
        skriv(node.right)


def comparison(value1, value2):
    '''
    Function for comparison of strings, converts to lowercase for equal comparison.
    :param value1: the first value to be compared
    :param value2: the second value to be compared
    :return: returns 1, -1 or 0
    '''
    if value1.lower() > value2.lower():
        return 1
    elif value1.lower() == value2.lower():
        return 0
    else:
        return -1

























