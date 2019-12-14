import sys
import time
import json
import requests
import webbrowser

class Media:

    def __init__(self, title = "No Title", author = "No Author", release_year = "No Release Year", link = None, json = None):
        if json == None:
            self.title = title
        else:
            if 'trackName' in json:
                self.title = json['trackName']

            if 'collectionName' in json:
                self.title = json['collectionName']
            else:
                self.title = title
        if json == None:
            self.author = author
        else:
            if 'artistName' in json:
                self.author = json['artistName']
            else:
                self.author = author
        if json == None:
            self.release_year = release_year
        else:
            if 'releaseDate' in json:
                self.release_year = json['releaseDate']
            else:
                self.release_year = release_year
        if json == None:
            self.link = None
        else:
            if 'trackViewUrl' in json:
                self.link = json['trackViewUrl']

            else:
                self.link = None

    def __str__(self):
        say = self.title + " by " + self.author + " (" + str(self.release_year) + ")"
        return say

    def __len__(self):
        return 0

class Song(Media):

    def __init__(self, title = "No Title", author = "No Author", release_year = "No Release Year", album = "No album", genre = "No genre", track_length = 0, link = None, json = None):
        super().__init__(title, author, release_year, link, json)
        if json == None:
            self.title = title
        else:
            if 'trackName' in json:
                self.title = json['trackName']
            else:
                self.title = title
        if json == None:
            self.album = album
        else:
            if 'collectionName' in json:
                self.album = json['collectionName']
            else:
                self.album = title
        if json == None:
            self.genre = genre
        else:
            if 'primaryGenreName' in json:
                self.genre = json['primaryGenreName']
            else:
                self.genre = genre
        if json == None:
            self.track_length = track_length
        else:
            if 'trackTimeMillis' in json:
                self.track_length = json['trackTimeMillis']
            else:
                self.track_length = track_length

    def __str__(self):
        say = self.title + " by " + self.author + " (" + str(self.release_year) + ")" + " [" + self.genre + "]"
        return say

    def __len__(self):
        x = self.track_length
        x = x // 1000
        return x

class Movie(Media):

    def __init__(self, title = "No Title", author = "No Author", release_year = "No Release Year", rating = "No rating given", movie_length = 0, link = None, json = None):
        super().__init__(title,author, release_year, link, json)
        if json == None:
            self.title = title
        else:
            if 'trackName' in json:
                self.title = json['trackName']
            else:
                self.title = title
        if json == None:
            self.rating = rating
        else:
            if 'contentAdvisoryRating' in json:
                self.rating = json['contentAdvisoryRating']
            else:
                self.rating = rating
        if json == None:
            self.movie_length = movie_length
        else:
            if 'trackTimeMillis' in json:
                self.movie_length = json['trackTimeMillis']
            else:
                self.movie_length = movie_length

    def __str__(self):
        say = self.title + " by " + self.author + " (" + str(self.release_year) + ")" + " [" + str(self.rating) + "]"
        return say

    def __len__(self):
        time = self.movie_length
        time = time // 60000
        return time

with open('sample_json.json') as x:
    data = json.load(x)

for x in data:
    if x['wrapperType'] == 'track':
        if x['kind'] == 'song':
            song = Song(json = x)
        if x['kind'] == 'feature-movie':
            movie = Movie(json = x)
    else:
        media = Media(json = x)

def get_info(x, y):
    baseurl = "https://itunes.apple.com/search?"
    params_dict = {}
    params_dict["term"] = x
    params_dict['limit'] = y
    response = requests.get(baseurl, params_dict)
    result = response.json()
    global itunes1
    itunes1 = result['results']
    i = 0
    global my_dict
    my_dict = {}
    for x in itunes1:
        if x['wrapperType'] == 'track':
            if x['kind'] == 'song':
                song = Song(json = x)
                my_dict[i] = song
                i += 1
            if x['kind'] == 'feature-movie':
                movie = Movie(json = x)
                my_dict[i] = movie
                i+=1
        else:
            media = Media(json = x)
            my_dict[i] = media1
            i+=1
    if not itunes1:
        empty = Media()
        my_dict[i] = empty
        itunes1.append(my_dict[i])

def api_call(x, y):
    baseurl = "https://itunes.apple.com/search?"
    params_dict = {}
    params_dict["term"] = x
    params_dict['limit'] = y
    response = requests.get(baseurl, params_dict)
    result = response.json()
    global itunes
    itunes = result['results']
    return itunes

def assignment():
    music = []
    film = []
    other = []
    for x in itunes:
        if x['wrapperType'] == 'track':
            if x['kind'] == 'song':
                song = Song(json = x)
                music.append(song)
            if x['kind'] == 'feature-movie':
                movie = Movie(json = x)
                film.append(movie)
        else:
            media = Media(json = x)
            other.append(media)

    i = 1
    print('\n')
    print('Top songs for your search: ')
    global final
    final = []
    list0 = []
    if not music:
        print("\t" + "--- No music results for your search")
    for x in music:
        final.append(x)
        print("\t" + str(i) + ": " + str(x))
        list0.append(str(i) +': ' + str(x))
        if len(list0) == 25:
            i  = i+1
            break
        else:
            i  = i+1

    print('\n')
    print('Top movies for your search: ')
    global final1
    final1 = []
    list1 = []
    if not film:
        print("\t" + "--- No movie results for your search")
    for x in film:
        final1.append(x)
        print("\t" + str(i)+ ": " + str(x))
        list1.append(str(i) +': '+ str(x))
        if len(list1) == 125:
            i  = i+1
            break
        else:
            i  = i+1

    print('\n')
    print('Top other forms of media for your search: ')
    global final2
    final2 = []
    list2 = []
    if not other:
        print("\t" + "--- No other media results for your search")
        print('\n')
    for x in other:
        final2.append(x)
        print("\t" + str(i) + ": " + str(x))
        list2.append(str(i) +': '+ str(x))
        if len(list2) == 25:
            i = i+1
            break
        else:
            i  = i+1


if __name__ == "__main__":

    print('\n')
    text = input('Enter search term for the iTunes store or "quit" to exit: ')
    if text.lower() =='quit':
        print('\n')
        print("Bye!")
        print('\n')
        sys.exit()
    api_call(text, 250)
    assignment()
    num = 1
    while num == 1:
        print('\n')
        text = input('Enter a number for more info, or another search term, or "quit" to exit: ')
        if text.lower() == 'quit':
            print('\n')
            print("Bye!")
            print('\n')
            break
        if text.isdigit():
            text = int(text)
            print('\n')
            options = final + final1 + final2
            if options[text - 1].link == None:
                print("Unable to get more info, sorry")
            else:
                print("Launching " + str(options[text - 1].link) + " for you to learn some more! ")
                time.sleep(1.5)
                webbrowser.open(options[text - 1].link, new = 2)
        else:
            api_call(text, 250)
            assignment()
