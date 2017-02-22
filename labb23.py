#from labb21 import *
from labb25 import*

def main():
    '''
    Main method uses input from user to create a list of integers
    calls for the magic_trick method and sends with it the array object
    :return:
    '''
    #q = ArrayQ()
    q = LinkedQ()
    cards = (input("Enter the card numbers from up to 13 that you wish to use: "))
    card_numbers = cards.split()

    for i in card_numbers:
        q.enqueue(int(i))

    magic_trick(q)


def magic_trick(q):
    '''
    Takes an array type object as parameter, while True it puts the first queue item last and prints the second one.
    Repeats until the queue is empty.
    :param q:
    :return:
    '''
    while True:
        if q.isEmpty() is False:
            top = q.dequeue()
            q.enqueue(top)
            to_table = q.dequeue()
            print(to_table)
        else:
            break

main()

