# Class Property & Property Decorator ############3


class MovieRating:
    def __init__(self, rating):
        self.set_rating(rating)

    def get_rating(self):
        return self.__rating

    def set_rating(self, value):
        if value < 0:
            raise ValueError("movie ratings cannot be zero")
        self.__rating = value

    rating = property(get_rating, set_rating)  # class property


# movie_rating = MovieRating(-8)
movie_rating = MovieRating(8)
print(movie_rating.rating)


# Property Decorator
class MovieRating:
    def __init__(self, rating):
        self.rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("movie rating cannot be zero")
        self.__rating = value


# movie_rating = MovieRating(-8)
movie_rating = MovieRating(8)
print(movie_rating.rating)
