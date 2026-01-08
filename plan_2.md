# Music Web App: HTML
## HTML Links & Forms

Test-drive and implement the following change:

The page returned by `GET /albums` should contain a link for each album listed. 
It should link to `/albums/<id>`, where `<id>` is the corresponding album's id. 
That page should then show information about the specific album.

```html
<!-- GET /albums 'home page' -->
<!DOCTYPE html>
<html>
    <head>
        <title>Albums Home</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Choose an Album</h1>

        <div>
            <p><a href="/albums/1">Mutter</a></p>
            <p><a href="/albums/2">Rammstein</a></p>
            <p><a href="/albums/3">Hypnotize</a></p>
            <p><a href="/albums/5">Rumors</a></p>
            <p><a href="/albums/4">Toxicity</a></p>
        </div>
    </body>
</html>
```

Test-drive and implement the following changes:

Add a route `GET /artists/<id>` which returns an HTML page showing details for a single artist.
Add a route `GET /artists` which returns an HTML page with the list of artists. This page should contain a link for each artist listed, linking to `/artists/<id>` where `<id>` needs to be the corresponding artist id.

```html
<!-- GET /artists 'home page' -->
 <!DOCTYPE html>
<html>
    <head>
        <title>Artists Home</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Artists</h1>

        <div>
            <p>Rammstein</p>
            <p>System of a Down</p>
            <p>Fleetwood Mac</p>
        </div>
    </body>
</html>
```

```html
<!-- GET /artists/1 -->
 <!DOCTYPE html>
<html>
    <head>
        <title>Rammstein</title>
        <meta charset="utf-8">
    </head>
    <body>
        <div>
            Artist: Rammstein
            Genre: Heavy Metal
        </div>
    </body>
</html>

<!-- GET /artists/2 -->
 <!DOCTYPE html>
<html>
    <head>
        <title>System of a Down</title>
        <meta charset="utf-8">
    </head>
    <body>
        <div>
            Artist: System of a Down
            Genre: Alt Metal
        </div>
    </body>
</html>

<!-- GET /artists/3 -->
 <!DOCTYPE html>
<html>
    <head>
        <title>Fleetwood Mac</title>
        <meta charset="utf-8">
    </head>
    <body>
       <div>
            Artist: Fleetwood Mac
            Genre: Pop Rock
        </div>
    </body>
</html>
```

Test-drive and implement a form page to add a new album.

You should then be able to use the form in your web browser to add a new album, and see this new album in the albums list page.

```html
<!-- GET /albums 'home page' -->
<!DOCTYPE html>
<html>
    <head>
        <title>Albums Home</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Choose an Album</h1>

        <div>
            <p><a href="/albums/1">Mutter</a></p>
            <p><a href="/albums/2">Rammstein</a></p>
            <p><a href="/albums/3">Hypnotize</a></p>
            <p><a href="/albums/5">Rumors</a></p>
            <p><a href="/albums/4">Toxicity</a></p>
        </div>
        <div>
            <p><a href="/albums/new">Add New Album</a></p>
        </div>
    </body>
</html>
```

```html
<!-- GET /albums/new 'home page' -->
<!DOCTYPE html>
<html>
    <head>
        <title>Albums Home</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Add an Album</h1>

        <div>
            <p>
                <label for="title">Title: </label>
                <input type="text" name="title" id="title">
            </p>
            <p>
                <label for="release_year">Release Year: </label>
                <input type="number" name="release_year" id="release_year">
            </p>
            <p>
                <input type="submit" value="Add Album">
            </p>
        </div>
    </body>
</html>
```