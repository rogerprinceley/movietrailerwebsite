"""Class docstring

=class=============
     Movie
-------------------
Methods:
(none)

Properties:
* title - Official title of the movie
* storyline (unused) - A brief description of the plot of the movie
* poster_image_url - URL to an image of the official movie poster
* trailer_youtube_url - URL to a trailer of the movie hosted on youtube.com
* year - Year of release of the movie
* actors (unused) - A list of the actors playing key characters in the movie
"""


class Movie:
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url,
                 year, actors):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
        self.actors = actors
