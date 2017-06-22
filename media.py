import webbrowser

class Movie():
    '''Movie class with information on movie title, storyline, release date (year), 
        youtube trailer URL, and poster iamge URL'''
    def __init__(self, title, storyline, poster_image, trailer, release_date):
        '''Movie class constructor initializing instance variables: title, storyline, poster_image, trailer, release_date'''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.release_date = release_date

    def print(self):
        '''Movie class print function to debug instance variable values'''
        print("Title: " + self.title)
        print("Storyline: " + self.storyline)
        print("Poster image URL: " + self.poster_image_url)
        print("Youtube trailer URL: " + self.trailer_youtube_url)
        print("Release date (year): " + self.release_date)