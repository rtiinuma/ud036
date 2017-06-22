import media
import fresh_tomatoes

# Instanciate movie objects
# Movie: Title, Plot summary, Poster image URL, Youtube trailer URL, and Release date
beauty_and_beast = media.Movie("Beauty and the Beast", "A girl falls in love with a beast", 
    "http://i.dailymail.co.uk/i/pix/2017/01/18/20/3C3FA2B500000578-4133768-image-a-44_1484772618253.jpg", "https://youtu.be/tRlzmyveDHE", 1991)
toy_story = media.Movie("Toy Story", "Toys come to life",
    "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", "https://youtu.be/KYz2wyBy3kc", 1995)
mulan = media.Movie("Mulan", "A girl cross-dresses and saves her country", 
                    "http://www.impawards.com/1998/posters/mulan_ver1_xlg.jpg", "https://youtu.be/MsAniqGowKE", 1998)
lilo_and_stitch = media.Movie("Lilo and Stitch","A girl becomes best friends with an alien",
    "http://www.my-sf.com/wp-content/uploads/2014/12/Lilo-and-Stitch-poster.jpg","https://youtu.be/5vMEOvZ1ODk", 2002)
princess_and_frog = media.Movie("Princess and the Frog", "A prince is turned into a frog",
    "http://www.impawards.com/2009/posters/princess_and_the_frog_xlg.jpg","https://youtu.be/ICFE0xiDii0", 2009)
frozen = media.Movie("Frozen","A girl goes on an adventure to save her sister",
    "http://www.impawards.com/2013/posters/frozen_xlg.jpg","https://youtu.be/TbQm5doF_Uc", 2013)
# Add movies to list to be displayed
movies = [beauty_and_beast,toy_story,mulan,lilo_and_stitch,princess_and_frog,frozen]
fresh_tomatoes.open_movies_page(movies)