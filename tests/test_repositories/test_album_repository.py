from lib.repositories.album_repository import AlbumRepository
from lib.models.album import Album

"""
When I call AlbumRepository#all
I get a list of Album objects reflecting the seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = AlbumRepository(db_connection)
    
    assert repo.all() == [
        Album(1, "Mutter", 2001, 1),
        Album(2, "Rammstein", 2019, 1),
        Album(3, "Hypnotize", 2005, 2),
        Album(4, "Rumors", 1977, 3),
        Album(5, "Toxicity", 2001, 2)
    ]

"""
When I call AlbumRepository#find_by_album_id
I get a single Album object reflecting seed data
Filtered by album_id
"""
def test_find_by_album_id(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = AlbumRepository(db_connection)

    assert repo.find_by_album_id(1) == Album(1, "Mutter", 2001, 1)

"""
When I call AlbumRepository#find_by_album_id_with_artist
I get a single Album object reflecting seed data
Filtered by album_id
And joined to artists on artist.id
"""
def test_find_by_album_id_with_artist(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = AlbumRepository(db_connection)

    album = repo.find_by_album_id_with_artist(1) 
    
    assert album.id == 1
    assert album.title == "Mutter"
    assert album.release_year == 2001
    assert album.artist_name == "Rammstein"