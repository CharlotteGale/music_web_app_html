DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    artist_id INTEGER
);

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);

INSERT INTO artists (name, genre) VALUES ('Rammstein', 'Heavy Metal');
INSERT INTO artists (name, genre) VALUES ('System of a Down', 'Alt Metal');
INSERT INTO artists (name, genre) VALUES ('Fleetwood Mac', 'Pop Rock');

INSERT INTO albums (title, release_year, artist_id) VALUES ('Du Hast', 1997, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Sonne', 2001, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('B.Y.O.B', 2005, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Chain', 1977, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Toxicity', 2001, 2);