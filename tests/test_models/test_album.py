from lib.models.album import Album

"""
Constructs with a id, title, release year, and artist id
"""
def test_constructs():
    album = Album(1, "Test Title", 2000, 3)

    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 3

"""
Albums with equal contents are equal
"""
def test_equal():
    album1 = Album(1, "Test Title", 2000, 3)
    album2 = Album(1, "Test Title", 2000, 3)

    assert album1 == album2

"""
Albums can be represented as strings
"""
def test_stringification():
    album = Album(1, "Test Title", 2000, 3)

    assert str(album) == "Album(1, Test Title, 2000, 3)"
