import media 
import fresh_tomatoes


toy_story = media.Movie("Toy story", 
                        "A story of a boy and his toys that came to life", 
                        "Animation, Adventure, Comedy",
                        "22 November 1995",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "http://bit.ly/1LYSb5Z", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "Action, Adventure, Fantasy",
                     "18 December 2009",
                     "Sam Worthington, Zoe Saldana, S. Weaver",
                     "http://ecx.images-amazon.com/images/I/41vuODnDSuL.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


school_of_rock = media.Movie("School of Rock", 
                             "Using rock music to learn", 
                             "Comedy, Music",
                             "3 October 2003",
                             "Jack Black, Mike White, Joan Cusack ",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", 
                          "A rat is a chef in Paris", 
                          "Animation, Comedy, Family",  
                          "29 June 2007",
                          "Brad Garrett, Lou Romano, Patton Oswalt",
                          "https://s4.mzstatic.com/us/r30/Video/v4/b7/6d/97/b76d974a-bd47-f511-3154-99ff04138a29/poster212x312.jpeg", 
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", 
                                "Going back in time to meet authors",
                                "Comedy, Romance",
                                "10 June 2011",
                                "Owen Wilson, Rachel McAdams, Kathy Bates",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", 
                           "A really real reality show",
                           " Adventure, Sci-Fi, Thriller",
                           "23 March 2012",
                           "Josh Hutcherson, Liam Hemsworth, J. Lawrence",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)



