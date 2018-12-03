class Movie():
    """ This particular class is used to create a movie object
    which then be used to display movie on the web page. """
    def __init__(self, movie_title, movie_poster_image, movie_trailer_youtube):
        # Title of the movie
        self.title = movie_title
        # The url to the thumbnail of the image to be displayed on the webpage.
        self.poster_image_url = movie_poster_image
        # The url of the youtube trailer to be played onClick.
        self.trailer_youtube_url = movie_trailer_youtube
