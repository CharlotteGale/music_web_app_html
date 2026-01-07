# Music Web App: HTML

Test-drive a `GET /albums` route that connects with an `AlbumRepository` and the database to return a result like this:

```html
<!-- GET /albums -->

<html>
  <head></head>
  <body>
    <h1>Albums</h1>

    <div>
      Title: Doolittle
      Released: 1989
    </div>

    <div>
      Title: Surfer Rosa
      Released: 1988
    </div>

    <!-- ... -->
  </body>
</html>
```

Test-drive and implement a route that returns the HTML content for a single album.
It should work like this:
```html
<!-- Example for GET /albums/1 -->

<html>
  <head></head>
  <body>
    <h1>Doolittle</h1>
    <p>
      Release year: 1989
      Artist: Pixies
    </p>
  </body>
</html>

<!-- Example for GET /albums/2 -->

<html>
  <head></head>
  <body>
    <h1>Surfer Rosa</h1>
    <p>
      Release year: 1988
      Artist: Pixies
    </p>
  </body>
</html>
```