from lib.models.artist import Artist

"""
Artist constructs with an id, name, genre
"""
def test_artist_constructs():
    artist = Artist(1, "Pixies", "Rock")

    assert artist.id == 1
    assert artist.name == "Pixies"
    assert artist.genre == "Rock"

"""
Artist formats as string
"""
def test_stringification():
    artist = Artist(1, "Pixies", "Rock")

    assert str(artist) == "Artist(1, Pixies, Rock)"

"""
Artist objects are identical they are equal
"""
def test_equalisation():
    artist1 = Artist(1, "Pixies", "Rock")
    artist2 = Artist(1, "Pixies", "Rock")

    assert artist1 == artist2