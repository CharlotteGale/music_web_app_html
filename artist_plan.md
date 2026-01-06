# Music Web App Challenge

1. Test drive a route `GET /artists` to return a list of artists:
```py
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone
```

2. Test drive a route `POST /artists` to create a new artist in the database:
```py
# Request:
POST /artists

# With body parameters:
name=Rammstein
genre=Heavy Metal

# Expected response (200 OK)
(No content)
```

Your test should then assert that the new artist is present in the list of records returned by `GET /artists`:

```py
# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Rammstein
```

## Class Interface (High-Level)
```py
# Model Class
# in lib/models/artist.py
class Artist:
    pass
```

**Repository Class**
```py
# Repository class
# in lib/repositories/artist_repository.py
class ArtistRepository:
    pass
```

## Database Schema
**artists table**
```sql
-- artists table
-- in seeds/artists_table.sql
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);
```

### Seed the Database
```bash
psql -h 127.0.0.1 music_web_app < seeds/web_music_app.sql
```

## Route Signature
```py
POST /artists
    name: string
    genre: string

GET /artists
```

## Test Suite
**/artists**
```py
# POST /artists
#   name: Rammstein
#   genre: Heavy Metal
# Expected response (200 OK)
"""
(No content)
"""

# Get /artists
# Expected Response (200 OK)
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Rammstein
"""
```