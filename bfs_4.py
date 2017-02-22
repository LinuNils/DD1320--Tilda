from BintreeFile import Bintree
from linkedQ import LinkedQ

ordlista = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        ordlista.put(ordet)             # in i sökträdet


def main():
    '''
    Main menu q is a linked list that you add children and mother to
    used_words is a bintree that keeps track of the words we have already used
    swedish_alphabet is a string with all the characters in the swedish alphabet
    chain  keeps track of the children
    ordlista keeps all the 3 syllable words in the swedish language
    path_found is used to indicate wether a path was found from the start_word to the end_word
    :return:
    '''

    q = LinkedQ()
    used_words1 = Bintree()
    used_words2 = Bintree()
    swedish_alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    chain = Bintree()

    start_word = input("Enter the starting word: ")
    end_word = input("Enter the ending word: ")

    q.enqueue(start_word)
    used_words1.put(start_word)
    used_words2.put(start_word)

    path_found = False
    while not q.isEmpty():
        nod = q.dequeue()
        if make_children_q(nod, end_word, used_words2, swedish_alphabet, q):
            path_found = True
            break
    if path_found:
        print("A path has been found to %s."%end_word)
    else:
        print("No path has been found to %s."%end_word)

    make_children(start_word, chain, used_words1, swedish_alphabet)
    chain.write()


def make_children(start_word, chain, used_words1, swedish_alphabet):
    '''
    First take the supplied starting word and make it into a list, then iterate over the number of characters in the
    word. Thereafter we change each character in the starting word one at a time, going throug all characters in
    the swedish alphabet also checking if the word is in the ordlista. Add used words to the used_words bintree.
    All possible words are added to the chain, if a word is the end_word we add it and break the loop.
    :param start_word: the starting word supplied from the user
    :param chain: bintree for adding the children to
    :param used_words: bintree that all words used are added to
    :param swedish_alphabet: a string containing the characters in the swedish alphabet
    :return: None
    '''
    for letter_number in range(0, len(start_word)):
        try_word = list(start_word)

        for symbol in swedish_alphabet:
            try_word[letter_number] = symbol
            temp_word = ''.join(try_word)

            if temp_word not in used_words1:
                if temp_word in ordlista:
                    chain.put(temp_word)
                    used_words1.put(temp_word)


def make_children_q(start_word, end_word, used_words2, swedish_alphabet, q):

    '''
    First take the supplied starting word and make it into a list, then iterate over the number of characters in the
    word. Thereafter we change each character in the starting word one at a time, going throug all characters in
    the swedish alphabet also checking if the word is in the ordlista. Add used words to the used_words bintree.
    If a word is the end_word we break the loop and return True.
    :param start_word: the starting word supplied from the user
    :param chain: bintree for adding the children to
    :param used_words: bintree that all words used are added to
    :param swedish_alphabet: a string containing the characters in the swedish alphabet
    :return: True or False
    '''

    for letter_number in range(0, len(start_word)):
        try_word = list(start_word)

        for symbol in swedish_alphabet:
            try_word[letter_number] = symbol
            temp_word = ''.join(try_word)

            if temp_word not in used_words2:
                if temp_word in ordlista:
                    q.enqueue(temp_word)
                    used_words2.put(temp_word)
                    if temp_word == end_word:
                        return True
    return False





main()



