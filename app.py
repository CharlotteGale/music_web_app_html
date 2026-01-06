import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.repositories.album_repository import AlbumRepository


app = Flask(__name__)

@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    albums = repo.all()
    return render_template("albums/index.html", albums=albums)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))