"""
Test-scripts for testing the DictHash class and HashTable class, uses Pytest for testing.
"""

from DictHash import*
from HashTable import*
from SongClass import*
import pytest


test_dict = DictHash()



def test_hash_dict():
    """
    tests for the dict hash, asserts we have the right values
    :return: no returns
    """
    test_dict.store('5', 5)
    test_dict.store('7', 7)
    test_dict.store('5', 7)
    test_dict.store('8', 8)
    test_dict.store('9', 9)
    test_dict.store('9', 10)

    response1 = test_dict.search('7')
    assert 7 in response1

    response2 = test_dict.search('5')
    assert 5 and 7 in response2

    response3 = test_dict['8']
    assert 8 in response3

    response4 = test_dict['9']
    assert 9 and 10 in response4

    response5 = test_dict.search('10')
    assert response5 == 404

    response6 = test_dict['11']
    assert response6 == 404

    return "Test pass."


def test_hash_table():
    """
    Test for the HasTable class. Check that a search returns a list. Check that checking for a key not in the table
    raises KeyError. Check that search finds the object wanted.
    :return:
    """

    filename = 'unique_tracks.txt'
    file = open(filename, encoding="utf8")
    song_hash = HashTable()
    artist = None
    for line in file:
        info = line.split("<SEP>")
        song = SongClass(info[0], info[1], info[2], info[3])
        song_hash.store(song.artistname, song)

        artist = song

    response1 = song_hash.hash_search('Metallica')
    assert len(response1) >= 1

    with pytest.raises(KeyError):
        song_hash.hash_search('Den här artisten finns absolut inte')

    response3 = song_hash.hash_search(artist.artistname)
    assert response3[0].artistname == artist.artistname





