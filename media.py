import webbrowser


class Movie():
    # documentation for class
    """ This class provides a way to store movie related information.
    It is used with the fresh_tomatoes.py program to create
    a movie trailer website."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image_url,
            trailer_youtube):

        self.title = movie_title

        self.storyline = movie_storyline

        self.poster_image_url = poster_image_url

        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
