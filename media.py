import webbrowser
""" Module for manage and show infos about media content. """


class Video(object):
    """docstring for Video"""
    def __init__(self, video_title, video_duration, video_description, 
                 video_genre):
        self.title = video_title
        self.duration = video_duration
        self.description = video_description
        self.genre = video_genre
        


class Movie(Video):
    """ Class is used for store info about the movies.

    This class is 

    Attributes:
        movie_title(str):
        movie_storyline(str):

    """


    def __init__(self, movie_title, movie_duration,movie_storyline, 
                 movie_genre, movie_release, movie_main_actors, 
                 poster_image, trailer_youtube):
        """Inits Movie class with blah."""
        super(Movie, self).__init__(movie_title, movie_duration, 
                                     movie_storyline, movie_genre)   
        self.release = movie_release
        self.main_actors = movie_main_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url =  trailer_youtube

    def show_trailer(self):
        """ Open the user's web browser for show the youtube movie trailer """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """docstring for TvShow"""
    def __init__(self, tv_title, tv_duration, tv_storyline, tv_genre, 
                 tv_season, tv_episode, tv_station):
        super(TvShow, self).__init__(tv_title, tv_duration, 
                                     tv_storyline, tv_genre)  
        self.season = tv_season
        self.episode = tv_episode
        self.station = tv_station
            




