class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        '''
        Initialize a Movie

        Keyword arguments:
        title -- movie title
        storyline -- movie storyline
        poster_image -- url link of the movie's poster image
        trailer_youtube -- url link of the movie trailer on youtube
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube