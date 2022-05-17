from . import db

# will contain movie and review models

class Movie:
    '''
    movie class that defines movie objects
    '''
    def __init__(self,id,title,overview,poster,vote_average, vote_count):
        self.id=id 
        self.title=title
        self.overview=overview
        self.poster= "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average=vote_average
        self.vote_count=vote_count

class Review:
    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title=title
        self.imageurl = imageurl
        self.review= review
    
    def save_review(self):
        Review.all_reviews.append(self)

    

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()


    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
                
        return response

class User(db.Model): #create user class which willc reate new users and pass dbmodel argument to connect the class to the database
    __tablename__ = 'users' #give the table in the database proper names otherwise sql alchemy will assume the tablename is the lowecase of the class name
    
    id = db.Column(db.Integer, primary_key = True) #dbcolumn to represent a single collumn. id column created and holds the primary key
    username = db.Column(db.String(255)) #datatype is a string with a maximum of 255 characters.
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  
    def __repr__(self): #used to debug applications
        return f'User {self.username}'

    
class Role(db.Model):
    __tablename__ = 'roles'

    id =db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref ='role', lazy = "dynamic")
    
    def __repr__(self):
        return f'User {self.name}'