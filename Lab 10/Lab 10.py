#Logan Passi
#11/27/2016
#CIS1400-003
class song:
    def __init__(self, artist, title, time, year):
        self.__artist = artist
        self.__title = title
        self.__time = time
        self.__year = year

    def getArtist(self):
        return self.__artist
    def getTitle(self):
        return self.__title
    def getTime(self):
        return self.__time
    def getYear(self):
        return self.__year    

def main():
    print("1st Song\n--------")
    artist = input("Enter in the artist's name:")
    title = input("Enter in the song name:")
    time = int(input("Enter in the song time in minutes:"))
    year = int(input("Enter in the release year:"))
    song1 = song(artist, title, time, year)

    print("\n2nd Song\n--------")
    artist = input("Enter in the artist's name:")
    title = input("Enter in the song name:")
    time = int(input("Enter in the song time in minutes:"))
    year = int(input("Enter in the release year:"))
    song2 = song(artist, title, time, year)
    print("The total song time is", song1.getTime() + song2.getTime(),"minutes.")
    myFile = open("song_inventory.dat", "w")
    myFile.write("%s,%s,%i,%i,\n" % (song1.getArtist(), song1.getTitle(),\
song1.getTime(), song1.getYear()))
    myFile.write("%s,%s,%i,%i,\n" % (song2.getArtist(), song2.getTitle(),\
song2.getTime(), song2.getYear()))
    myFile.close()
main()
##1st Song
##--------
##Enter in the artist's name:sake
##Enter in the song name:adrift
##Enter in the song time in minutes:3
##Enter in the release year:2016
##
##2nd Song
##--------
##Enter in the artist's name:spiegel eyes
##Enter in the song name:amphee
##Enter in the song time in minutes:2
##Enter in the release year:2016
##The total song time is 5 minutes.
