import media
import fresh_tomatoes

# Instantiate movie objects
# Title, Plot summary, Poster image URL, Youtube trailer URL, and Release date
beauty_and_beast = media.Movie("Beauty and the Beast",
                               "A girl falls in love with a beast",
                               "http://i.imgur.com/QNCojML.jpg",
                               "https://youtu.be/tRlzmyveDHE",
                               1991)
toy_story = media.Movie("Toy Story",
                        "Toys come to life",
                        "http://i.imgur.com/3KNAUJ9.jpg",
                        "https://youtu.be/KYz2wyBy3kc",
                        1995)
mulan = media.Movie("Mulan",
                    "A girl cross-dresses and saves her country",
                    "http://i.imgur.com/RCf0TSH.jpg",
                    "https://youtu.be/MsAniqGowKE",
                    1998)
lilo_and_stitch = media.Movie("Lilo and Stitch",
                              "A girl becomes best friends with an alien",
                              "http://i.imgur.com/FVwPrWE.jpg",
                              "https://youtu.be/5vMEOvZ1ODk",
                              2002)
princess_and_frog = media.Movie("Princess and the Frog",
                                "A prince is turned into a frog",
                                "http://i.imgur.com/x7og9U9.jpg",
                                "https://youtu.be/ICFE0xiDii0",
                                2009)
frozen = media.Movie("Frozen",
                     "A girl goes on an adventure to save her sister",
                     "http://i.imgur.com/bWkr4Z5.jpg",
                     "https://youtu.be/TbQm5doF_Uc",
                     2013)
# Add movies to list to be displayed
movies = [beauty_and_beast, toy_story, mulan,
          lilo_and_stitch, princess_and_frog, frozen]
# Call function to dynamically generate html page
fresh_tomatoes.open_movies_page(movies)
