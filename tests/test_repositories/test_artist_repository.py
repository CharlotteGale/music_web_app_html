from lib.repositories.artist_repository import ArtistRepository
from lib.models.artist import Artist

def test_find_by_artist_id(db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    repo = ArtistRepository(db_connection)

    assert repo.find_by_artist_id(1) == (Artist(1, "Rammstein", "Heavy Metal"))