from lib.repositories.artist_repository import ArtistRepository
from lib.models.artist import Artist

"""
When I call #all
I get all the artists in the artists table
"""
def test_all(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = ArtistRepository(db_connection)

    assert repo.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz")
    ]

"""
When I call #create
I create an artist in the database 
and I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = ArtistRepository(db_connection)
    artist = Artist(None, "Rammstein", "Heavy Metal")
    repo.create(artist)

    assert repo.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Rammstein", "Heavy Metal")
    ]