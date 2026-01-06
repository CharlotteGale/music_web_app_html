from lib.repositories.album_repository import AlbumRepository
from lib.models.album import Album
"""
When I call #all
I get all the albums in the album table
"""
def test_all(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = AlbumRepository(db_connection)

    assert repo.all() == [
        Album(1, "Waterloo", 1972, 2)
    ]
    
"""
When I call #create
I create an album in the database
And I cen see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 2000, 3)
    repo.create(album)

    assert repo.all() == [
        Album(1, "Waterloo", 1972, 2),
        Album(2, "Test Title", 2000, 3)
    ] 