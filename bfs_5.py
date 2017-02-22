from BintreeFile import Bintree
from linkedQ import LinkedQ

ordlista = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        ordlista.put(ordet)             # in i sökträdet


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


def main():
    '''
    Main menu q is a linked list that you add children and mother to
    used_words is a bintree that keeps track of the words we have already used
    swedish_alphabet is a string with all the characters in the swedish alphabet
    Each word is made into a ParentNode() that keeps track of its parent and the childs word
    ordlista keeps all the 3 syllable words in the swedish language
    path_found is used to indicate wether a path was found from the start_word to the end_word
    :return:
    '''

    q = LinkedQ()
    used_words2 = Bintree()
    swedish_alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

    start_word = input("Enter the starting word: ")
    end_word = input("Enter the ending word: ")

    first_parent = ParentNode(start_word)
    q.enqueue(first_parent)
    used_words2.put(start_word)

    path_found_node = None
    path_found = False

    while not q.isEmpty():
        #take the parent out of the queue and send it to make_children_q
        #if the end word is found we then print all the words before it using the parent pointer
        parent = q.dequeue()
        path_found_node = make_children_q(end_word, used_words2, swedish_alphabet, q, parent)
        if path_found_node:
            path_found = True
            break

    if path_found:
        writechain(path_found_node)
    else:
        print("No path has been found to %s."%end_word)


def writechain(child):
    if child.parent:
        writechain(child.parent)
    print(child.word)


def make_children_q(end_word, used_words2, swedish_alphabet, q, parent):
    '''
    Gets a parent node as parameter, then replaces each character in that parent nodes word
    linking each word that is a child to that parent via the parent pointer, if the end word is found we return that
    node, else we just return having not found a path
    :param used_words2: bintree that all words used are added to
    :param swedish_alphabet: a string containing the characters in the swedish alphabet
    ;:param q: the queue that we add the nodes to to keep track of them
    ;:param parent: the parent node for each level of the search
    :return: True or False
    '''

    start_word = parent.word
    for letter_number in range(0, len(start_word)):
        try_word = list(start_word)

        for symbol in swedish_alphabet:
            try_word[letter_number] = symbol
            temp_word = ''.join(try_word)

            if temp_word not in used_words2:
                if temp_word in ordlista:
                    current_node = ParentNode(temp_word, parent)
                    q.enqueue(current_node)
                    used_words2.put(temp_word)
                    if temp_word == end_word:
                        return current_node
    return





main()



