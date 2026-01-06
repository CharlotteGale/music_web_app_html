import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.repositories.album_repository import AlbumRepository
from lib.models.album import Album
from lib.repositories.artist_repository import ArtistRepository
from lib.models.artist import Artist

app = Flask(__name__)

@app.route('/albums', methods=['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release_year, and artist_id", 400
    
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id']
    )
    repo.create(album)
    return '', 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    albums = repo.all()
    return "\n".join(
        f"{album}" for album in albums
    )

def has_invalid_album_parameters(form):
    return 'title' not in form \
        or 'release_year' not in form \
        or 'artist_id' not in form

@app.route('/artists')
def get_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artists = repo.all()
    return ", ".join(
        f"{artist}" for artist in artists
    ), 200

"""
With all my mistakes, I didn't do my little change, which will fail all the tests, 
but in the return statement, I was going change the f string to f"{artist.name}" 
and show it on the browser as the list of artist names asked for in the challenge blurb
"""

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre']
    )
    repo.create(artist)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))