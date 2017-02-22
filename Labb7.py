"""
Main program of labb7, reads from file and then creates DictHash, HashTable objects that are used for storing SongClass
objects. Times the different class methods to see which are the fastest.
"""


from SongClass import *
from DictHash import *
from HashTable import *
import timeit

file_name = "unique_tracks.txt"


def read_from_file(filename, dict_hash, hash_table):
    """
    Read from file creating objects and storing them in a HashDict and HashTable
    :param filename: the file we are reading from
    :param dict_hash: a hash made out of pythons dict
    :param hash_table: our own implemented hash table
    :return: return a song object that is used for searching
    """
    file = open(filename, encoding="utf8")
    song_dict = dict_hash
    song_hash = hash_table
    for line in file:
        info = line.split("<SEP>")
        song = SongClass(info[0], info[1], info[2], info[3])
        song_dict.store(info[2], song)
        song_hash.store(song.artistname, song)

    return song


def main(filename):

    dict_hash = DictHash()
    hash_table = HashTable()
    artist = read_from_file(filename, dict_hash, hash_table)

    response = timeit.timeit(stmt=lambda: dict_hash[artist.artistname], number=100000)
    print("The hash __getitem() took", round(response, 4), "seconds")

    response2 = timeit.timeit(stmt=lambda: dict_hash.search(artist.artistname), number=100000)
    print("The dict hash search took", round(response2, 4), "seconds")

    response3 = timeit.timeit(stmt=lambda: hash_table.hash_search(artist.artistname), number=100000)
    print("The hash table search took", round(response3, 4), "seconds")




main(file_name)


