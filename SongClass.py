class SongClass:
    def __init__(self, trackid=None, songid=None, artistname=None, trackname=None):
        self.trackid = trackid
        self.songid = songid
        self.artistname = artistname
        self.trackname = trackname

    def __lt__(self, other):
        name1 = self.artistname.lower()
        name2 = other.artistname.lower()
        return name1 < name2

    def __str__(self):
        '''
        method for representing each object as a string
        :return: a string representation of the object
        '''
        str_repr = "\n%s"%self.trackid+"\n%s"%self.songid+"\n%s"%self.artistname+"\n%s"%self.trackname
        return str_repr
