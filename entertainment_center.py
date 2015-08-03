import media 
import fresh_tomatoes

# Initialize 

toy_story = media.Movie("Toy story", 
                        "0:00",
                        "A story of a boy and his toys that came to life", 
                        "Animation, Adventure, Comedy",
                        "22 November 1995",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "http://bit.ly/1LYSb5Z", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "0:00",
                     "A marine on an alien planet",
                     "Action, Adventure, Fantasy",
                     "18 December 2009",
                     "Sam Worthington, Zoe Saldana, S. Weaver",
                     "http://ecx.images-amazon.com/images/I/41vuODnDSuL.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

'''
school_of_rock = media.Movie("School of Rock", 
                             "Using rock music to learn", 
                             "Comedy, Music",
                             "3 October 2003",
                             "Jack Black, Mike White, Joan Cusack ",
                             "http://bit.ly/1E376FU",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", 
                          "A rat is a chef in Paris", 
                          "Animation, Comedy, Family",  
                          "29 June 2007",
                          "Brad Garrett, Lou Romano, Patton Oswalt",
                          "http://bit.ly/1SxnIS1", 
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", 
                                "Going back in time to meet authors",
                                "Comedy, Romance",
                                "10 June 2011",
                                "Owen Wilson, Rachel McAdams, Kathy Bates",
                                "http://bit.ly/1MG5PfN",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", 
                           "A really real reality show",
                           "Adventure, Sci-Fi, Thriller",
                           "23 March 2012",
                           "Josh Hutcherson, Liam Hemsworth, J. Lawrence",
                           "http://bit.ly/1KKnRuk",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")
'''

movies = [toy_story, avatar]#, school_of_rock, ratatouille, 
        #  midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)



