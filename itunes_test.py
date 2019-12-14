import unittest
import itunes as itunes

class TestCases(unittest.TestCase):

    def testPopPartOne(self):
        m1 = itunes.Media()
        m2 = itunes.Media("1999", "Prince")
        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")

        s1 = itunes.Song()
        s2 = itunes.Song("song_title", "song_artist", 2019, 'song_album', 'song_genre', 5000)
        s3 = itunes.Song("album")
        self.assertEqual(s1.title, "No Title")
        self.assertEqual(s2.title, "song_title")
        self.assertEqual(s1.author, "No Author")
        self.assertEqual(s2.author, "song_artist")
        self.assertEqual(s1.release_year, "No Release Year")
        self.assertEqual(s2.release_year, 2019)
        self.assertEqual(s1.album, "No album")
        self.assertEqual(s2.album, "song_album")
        self.assertEqual(s1.genre, "No genre")
        self.assertEqual(s2.genre, "song_genre")
        self.assertEqual(s1.track_length, 0)
        self.assertEqual(s2.track_length, 5000)
        self.assertEqual(s3.title, "album")
        self.assertEqual(s3.album, "No album")

        f1 = itunes.Movie()
        f2 = itunes.Movie("Movie title", "Director", 2019, "Rating", 180000)
        f3 = itunes.Movie("Titanic")
        self.assertEqual(f1.title, "No Title")
        self.assertEqual(f2.title, "Movie title")
        self.assertEqual(f1.author, "No Author")
        self.assertEqual(f2.author, "Director")
        self.assertEqual(f1.release_year, "No Release Year")
        self.assertEqual(f2.release_year, 2019)
        self.assertEqual(f1.rating, "No rating given")
        self.assertEqual(f2.rating, "Rating")
        self.assertEqual(f1.movie_length, 0)
        self.assertEqual(f2.movie_length, 180000)
        self.assertEqual(f3.title, "Titanic")
        self.assertEqual(f3.rating, "No rating given")

    def testLenPartOne(self):
        m1 = itunes.Media()
        m2 = itunes.Media("1999", "Prince")
        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 0)

        s1 = itunes.Song()
        s2 = itunes.Song("song_title", "song_artist", 2019, 'song_album', 'song_genre', 5000)
        s3 = itunes.Song("album")
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 5)

        f1 = itunes.Movie()
        f2 = itunes.Movie("Movie title", "Director", 2019, "Rating", 180000)
        self.assertEqual(len(f1), 0)
        self.assertEqual(len(f2), 3)

    def testStrPartOne(self):
        m1 = itunes.Media()
        m2 = itunes.Media("1999", "Prince")
        self.assertEqual(str(m1), "No Title by No Author (No Release Year)")
        self.assertEqual(str(m2), "1999 by Prince (No Release Year)")

        s1 = itunes.Song()
        s2 = itunes.Song("song_title", "song_artist", 2019, 'song_album', 'song_genre', 5000)
        s3 = itunes.Song("album")
        self.assertEqual(str(s1), "No Title by No Author (No Release Year) [No genre]")
        self.assertEqual(str(s2), "song_title by song_artist (2019) [song_genre]")
        self.assertEqual(str(s3), "album by No Author (No Release Year) [No genre]")

        f1 = itunes.Movie()
        f2 = itunes.Movie("Movie title", "Director", 2019, "Rating", 180000)
        f3 = itunes.Movie("Titanic")
        self.assertEqual(str(f1), "No Title by No Author (No Release Year) [No rating given]")
        self.assertEqual(str(f2), "Movie title by Director (2019) [Rating]")
        self.assertEqual(str(f3), "Titanic by No Author (No Release Year) [No rating given]")

    def testInstanceVariablesPartOne(self):
        s1 = itunes.Song()
        m1 = itunes.Media()
        f1 = itunes.Movie()
        with self.assertRaises(AttributeError):
            s1.rating
        with self.assertRaises(AttributeError):
            s1.movie_length
        with self.assertRaises(AttributeError):
            m1.rating
        with self.assertRaises(AttributeError):
            m1.movie_length
        with self.assertRaises(AttributeError):
            m1.album
        with self.assertRaises(AttributeError):
            m1.genre
        with self.assertRaises(AttributeError):
            f1.genre
        with self.assertRaises(AttributeError):
            f1.album



    def testPartTwo(self):
        s1 = itunes.song
        self.assertEqual(s1.title, "Hey Jude")
        self.assertEqual(s1.author, "The Beatles")
        self.assertEqual(s1.release_year, "1968-08-26T07:00:00Z")
        self.assertEqual(s1.genre, "Rock")
        self.assertEqual(len(s1), 431)
        self.assertEqual(str(s1), "Hey Jude by The Beatles (1968-08-26T07:00:00Z) [Rock]")

        f1 = itunes.movie
        self.assertEqual(f1.title, "Jaws")
        self.assertEqual(f1.author, "Steven Spielberg")
        self.assertEqual(f1.release_year, "1975-06-20T07:00:00Z")
        self.assertEqual(f1.rating, "PG")
        self.assertEqual(len(f1), 124)
        self.assertEqual(str(f1), "Jaws by Steven Spielberg (1975-06-20T07:00:00Z) [PG]")

        m1 = itunes.media
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.release_year, "2012-04-03T07:00:00Z")
        self.assertEqual(str(m1), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012-04-03T07:00:00Z)")

    def testPartThree(self):

        itunes.get_info('love', 5)
        self.assertEqual(itunes.my_dict[0].title, itunes.itunes1[0]['trackName'])
        self.assertEqual(itunes.my_dict[1].title, itunes.itunes1[1]['trackName'])
        self.assertEqual(itunes.my_dict[2].title, itunes.itunes1[2]['trackName'])
        self.assertEqual(itunes.my_dict[3].title, itunes.itunes1[3]['trackName'])
        self.assertEqual(itunes.my_dict[4].title, itunes.itunes1[4]['trackName'])

        self.assertEqual(itunes.my_dict[0].album, itunes.itunes1[0]['collectionName'])
        self.assertEqual(itunes.my_dict[1].album, itunes.itunes1[1]['collectionName'])
        self.assertEqual(itunes.my_dict[2].album, itunes.itunes1[2]['collectionName'])
        self.assertEqual(itunes.my_dict[3].album, itunes.itunes1[3]['collectionName'])
        self.assertEqual(itunes.my_dict[4].album, itunes.itunes1[4]['collectionName'])

        self.assertEqual(itunes.my_dict[0].genre, itunes.itunes1[0]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[1].genre, itunes.itunes1[1]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[2].genre, itunes.itunes1[2]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[3].genre, itunes.itunes1[3]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[4].genre, itunes.itunes1[4]['primaryGenreName'])

        self.assertEqual(itunes.my_dict[0].track_length, itunes.itunes1[0]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[1].track_length, itunes.itunes1[1]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[2].track_length, itunes.itunes1[2]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[3].track_length, itunes.itunes1[3]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[4].track_length, itunes.itunes1[4]['trackTimeMillis'])

        itunes.get_info('baby', 5)
        self.assertEqual(itunes.my_dict[0].title, itunes.itunes1[0]['trackName'])
        self.assertEqual(itunes.my_dict[1].title, itunes.itunes1[1]['trackName'])
        self.assertEqual(itunes.my_dict[2].title, itunes.itunes1[2]['trackName'])
        self.assertEqual(itunes.my_dict[3].title, itunes.itunes1[3]['trackName'])
        self.assertEqual(itunes.my_dict[4].title, itunes.itunes1[4]['trackName'])

        self.assertEqual(itunes.my_dict[0].album, itunes.itunes1[0]['collectionName'])
        self.assertEqual(itunes.my_dict[1].album, itunes.itunes1[1]['collectionName'])
        self.assertEqual(itunes.my_dict[2].album, itunes.itunes1[2]['collectionName'])
        self.assertEqual(itunes.my_dict[3].album, itunes.itunes1[3]['collectionName'])
        self.assertEqual(itunes.my_dict[4].album, itunes.itunes1[4]['collectionName'])

        self.assertEqual(itunes.my_dict[0].genre, itunes.itunes1[0]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[1].genre, itunes.itunes1[1]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[2].genre, itunes.itunes1[2]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[3].genre, itunes.itunes1[3]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[4].genre, itunes.itunes1[4]['primaryGenreName'])

        self.assertEqual(itunes.my_dict[0].track_length, itunes.itunes1[0]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[1].track_length, itunes.itunes1[1]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[2].track_length, itunes.itunes1[2]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[3].track_length, itunes.itunes1[3]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[4].track_length, itunes.itunes1[4]['trackTimeMillis'])

        itunes.get_info('moana', 3)
        self.assertEqual(itunes.my_dict[0].title, itunes.itunes1[0]['trackName'])
        self.assertEqual(itunes.my_dict[1].title, itunes.itunes1[1]['trackName'])
        self.assertEqual(itunes.my_dict[2].title, itunes.itunes1[2]['trackName'])

        self.assertEqual(itunes.my_dict[0].album, itunes.itunes1[0]['collectionName'])
        self.assertEqual(itunes.my_dict[1].rating, itunes.itunes1[1]['contentAdvisoryRating'])
        self.assertEqual(itunes.my_dict[2].album, itunes.itunes1[2]['collectionName'])

        self.assertEqual(itunes.my_dict[0].genre, itunes.itunes1[0]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[2].genre, itunes.itunes1[2]['primaryGenreName'])

        self.assertEqual(itunes.my_dict[0].track_length, itunes.itunes1[0]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[1].movie_length, itunes.itunes1[1]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[2].track_length, itunes.itunes1[2]['trackTimeMillis'])

        itunes.get_info('helter skelter', 3)
        self.assertEqual(itunes.my_dict[0].title, itunes.itunes1[0]['trackName'])
        self.assertEqual(itunes.my_dict[1].title, itunes.itunes1[1]['trackName'])
        self.assertEqual(itunes.my_dict[2].title, itunes.itunes1[2]['trackName'])

        self.assertEqual(itunes.my_dict[0].album, itunes.itunes1[0]['collectionName'])
        self.assertEqual(itunes.my_dict[1].album, itunes.itunes1[1]['collectionName'])
        self.assertEqual(itunes.my_dict[2].album, itunes.itunes1[2]['collectionName'])

        self.assertEqual(itunes.my_dict[0].genre, itunes.itunes1[0]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[1].genre, itunes.itunes1[1]['primaryGenreName'])
        self.assertEqual(itunes.my_dict[2].genre, itunes.itunes1[2]['primaryGenreName'])

        self.assertEqual(itunes.my_dict[0].track_length, itunes.itunes1[0]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[1].track_length, itunes.itunes1[1]['trackTimeMillis'])
        self.assertEqual(itunes.my_dict[2].track_length, itunes.itunes1[2]['trackTimeMillis'])


        itunes.get_info('!@#$%^&*()hgsdfkhgrorgfowuergiwlbfv', 1)
        self.assertEqual(itunes.my_dict[0].title, itunes.itunes1[0].title)
        self.assertEqual(itunes.my_dict[0].author, itunes.itunes1[0].author)
        self.assertEqual(itunes.my_dict[0].release_year, itunes.itunes1[0].release_year)

        itunes.get_info('', 1)
        self.assertEqual(itunes.my_dict[0].title, itunes.itunes1[0].title)
        self.assertEqual(itunes.my_dict[0].author, itunes.itunes1[0].author)
        self.assertEqual(itunes.my_dict[0].release_year, itunes.itunes1[0].release_year)


unittest.main()
