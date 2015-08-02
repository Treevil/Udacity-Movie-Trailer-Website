import webbrowser

# Movie Class. Used for store information about movies
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_genre, 
                 movie_release, movie_main_actors, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.release = movie_release
        self.main_actors = movie_main_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url =  trailer_youtube

    def show_trailer(self):
        # Open the user's web browser for show the youtube movie trailer
        webbrowser.open(self.trailer_youtube_url)




