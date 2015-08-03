""" Module for manage and show infos about media content. """

import webbrowser


class Video(object):
    """ This class is used for store info about Video

    Attributes:
        - video_title(str):       The title of the video 
        - video_duration(str):    The duration of the video
        - video_description(str): Brief description of the video
        - video_genre(str):       Category of the video

    """
    def __init__(self, video_title, video_duration, video_description, 
                 video_genre):
        self.title = video_title
        self.duration = video_duration
        self.description = video_description
        self.genre = video_genre
        


class Movie(Video):
    """ This class is used for store info about movies.

    Attributes:
        - movie_release(str):     Release date
        - movie_main_actors(str): Main actors inside the movie
        - poster_image(str):      Urof the video poster image
        - trailer_youtube(str):   Url of the youtube trailer 

    """


    def __init__(self, movie_title, movie_duration,movie_description, 
                 movie_genre, movie_release, movie_main_actors, 
                 poster_image, trailer_youtube):
        super(Movie, self).__init__(movie_title, movie_duration, 
                                     movie_description, movie_genre)   
        self.release = movie_release
        self.main_actors = movie_main_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url =  trailer_youtube

    def show_trailer(self):
        """ Open the user's web browser for show the youtube movie trailer """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """ 
    This class is used for store info about TV Show
    
    Attributes:
        - tv_season: The number of season of the TV show
        - tv_episode: number of episode for season
        - tv_station: Where the TvShow is broadcasted 
    """

    def __init__(self, tv_title, tv_duration, tv_storyline, tv_genre, 
                 tv_season, tv_episode, tv_station):
        super(TvShow, self).__init__(tv_title, tv_duration, 
                                     tv_storyline, tv_genre)  
        self.season = tv_season
        self.episode = tv_episode
        self.station = tv_station
            




