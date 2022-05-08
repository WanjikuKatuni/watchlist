import unittest  #import unittiest module
from models import movie  #import the movie module
Movie= movie.Movie #get movie class

class MovieTest (unittest.TestCase): #movie testcalss
    '''
    test class that tests the movie class
    '''
    def setUp(self):#instantiate movie clas to make the self.newmovie
        '''
        method whcih will run before every step
        '''
        self.new_movie = Movie(1234,'Python Must be Crazy', 'A thrilling new python series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993) #instance of movie calss

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))


if __name__ == '__main__':
    unittest.main()