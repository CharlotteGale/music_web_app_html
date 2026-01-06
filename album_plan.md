# Music Web App Exercise

Test-drive a route `POST /albums` to create a new album:

```bash
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)
```

Your test should assert that the new album is present in the list of records returned by `GET /albums`.

## Class Interface
**Model Class**
```py
# Model Class
# in lib/models/album.py
class Album:
    pass
```

**Repository Class**
```py
# Repository class
# in lib/repositories/album_repository.py
class AlbumRepository:
    pass
```

## Database Schema
### albums table
```sql
-- albums table
-- in seeds/albums_table.sql
CREATE TABLE albums
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER(4),
    artist_id INTEGER;
```

### Seed the Database
```bash
psql -h 127.0.0.1 music_web_app < albums_table.sql
```

## Route Signature

```bash
POST /albums
    title: string
    release_year: number (str)
    artist_id: number (str)
```
```bash
GET /albums
```

## Test Suite
```py
# Scenario 1
# POST /albums
#   title: "Voyager"
#   release_year: 2022
#   artist_id: 2
# Expected response (200 OK)
"""
(No content)
"""

# Get /albums
# Expected Response (200 OK)
"""
Album(1, Waterloo, 1972, 2)
Album(2, Voyager, 2022, 2)
"""
```