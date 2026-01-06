"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/web_music_app_html.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Waterloo, 1972, 2)"


"""
When I call POST /albums with album info
That album is now int he list in GET /albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/web_music_app_html.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Voyager',
        'release_year': '2022',
        'artist_id': '2'
    })

    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Waterloo, 1972, 2)\n" \
        "Album(2, Voyager, 2022, 2)"

def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/web_music_app_html.sql")
    post_response = web_client.post("/albums")

    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to submit a title, release_year, and artist_id"

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Waterloo, 1972, 2)"
    
"""
When I call GET /artists
I get a list of all artists back
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/web_music_app_html.sql")
    response = web_client.get("/artists")

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock), " \
        "Artist(2, ABBA, Pop), " \
        "Artist(3, Taylor Swift, Pop), " \
        "Artist(4, Nina Simone, Jazz)"
    
"""
When I call POST /artists with artist info
That artist is now in the list in GET /artists
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/web_music_app_html.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Rammstein',
        'genre': 'Heavy Metal'
    })

    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock), " \
        "Artist(2, ABBA, Pop), " \
        "Artist(3, Taylor Swift, Pop), " \
        "Artist(4, Nina Simone, Jazz), " \
        "Artist(5, Rammstein, Heavy Metal)"
