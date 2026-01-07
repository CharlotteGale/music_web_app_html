from lib.repositories.album_repository import AlbumRepository
from lib.models.album import Album

def test_find_by_album_id(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = AlbumRepository(db_connection)

    album = repo.find_by_album_id_with_artist(1) 
    
    assert album.id == 1
    assert album.title == "Mutter"
    assert album.release_year == 2001
    assert album.artist_name == "Rammstein"