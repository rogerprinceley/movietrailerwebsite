"""Module docstring

This code acts as the entertainment center for the movie database project.
The application reads in movie data from the movies.xml file.
This data is a list of movies that is used to generate an HTML page using
fresh_tomatoes code.
"""

# Builtin modules
import xml.etree.ElementTree as ElementTree
# Local Files
from media import Movie
import fresh_tomatoes


def main():
    # Import data from XML file
    tree = ElementTree.parse('movies.xml')
    root = tree.getroot()

    # Empty List
    movies = []

    # Extract Movies from XML data
    for child in root:
        movies.append(Movie(child.get('name'), child.find('storyline').text,
                            child.find('poster').text,
                            child.find('trailer').text,
                            child.find('year').text, None))

    # Create Movies Page
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()
