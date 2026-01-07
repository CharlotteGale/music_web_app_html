import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.repositories.album_repository import AlbumRepository
from lib.repositories.artist_repository import ArtistRepository


app = Flask(__name__)

@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    albums = repo.all()
    return render_template("albums/index.html", albums=albums)

@app.route("/albums/<id>")
def get_album_by_id_with_artist(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    album = repo.find_by_album_id_with_artist(id)
    return render_template("albums/album_id.html", album=album)

@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artists = repo.all()

    return render_template("artists/index.html", artists=artists)

@app.route("/artists/<id>")
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artist = repo.find_by_artist_id(id)
    return render_template("artists/artist_id.html", artist=artist)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))