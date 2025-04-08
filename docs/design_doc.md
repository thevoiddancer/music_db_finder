# Intention

The intention behind this repo is to create a combined search engine going through Spotify, YTMusic, Discogs and potentially other music services and databases.

## Requirements

Apart from dependency installation, this code will require login tokens. They are supplied via environmental variables. Additionally, some services will require a paid account, so for cases where I lack that account, the progress will be slower.

### Environmental variables

Required env variables use the following keys:

* SPOTIFY_CLIENT_ID
* SPOTIFY_CLIENT_SECRET
* DISCOGS_USER_TOKEN
* YTMUSIC_REFRESH_TOKEN
* YTMUSIC_ACCESS_TOKEN

Locations for setting up those values are:

* Spotify:
    * https://developer.spotify.com/dashboard
* Discogs:
    * https://www.discogs.com/settings/developers
* YT Music:
    * ....

In addition, python-dotenv (or equivalent) is required to store the variables. The suggestion is to place the variables in an _"env"_ file, to be stored in the folder with the project's git folder. Storing env variables then follows the following steps:

```python
import dotenv
env_file_name = '../../env'
dotenv.load_dotenv(env_file_name, override=True)
```

# Services

## Spotify

Spotify result is a dictionary with only one key that is the plural of the type used in search:

- artists for type='artist'
- albums for type='album'
- tracks for type='track'
- etc

The singular value in that dictionary is another dictionary with the following keys:

- 'href' - API endpoint for this search
- 'limit' - max number of results returned by that search
- 'next' - API endpoint for the next part of the search
- 'offset' - the current search offset
- 'previous' - API endpoint for the previous part of the search
- 'total' - total number of search results found
- 'items' - list of results

The actual results of the search is contained in the ['items'] list. It is a list of dictionaries with keys that vary depending on the type of search performed.

All result types have the following keys:
- external_urls - spotify link to the result item
- href - API endpoint for the result item
- id - spotify id for the result item
- name - name for the result item
- type - type of search result: track, album, artist
- uri - spotify uri for the result item

In addition, specific searches have additional keys:

TRACKS:
- album - album on which the track appears
- artists - list of artists who worked on the track
- available_markets - markets in which the track is vailable
- disc_number - the number of disc of the  album the track is on
- duration_ms - track duration in ms
- explicit - is the track explicit
- external_ids - dictionary with external id information
    - isrc - International Standard Recording Code
- is_local - is the track local (on the computer or phone)
- is_playable - is the track playable (available in market, etc)
- popularity - popularity rating of the track
- preview_url - link to the track preview
- track_number - the track number on the album

ALBUMS:
- album_type - type of the album: album, single ????
- total_tracks - number of tracks on the album
- available_markets - markets in which the album is vailable
- images - list with images for the album, as a dictionary:
    - height
    - width
    - url
- release_date - the release date of the album
- release_date_precision - precision of the releease date: day, year
- artists - list of artists on the album, as a dictionary

ARTISTS
- followers - dict with number of followers:
    - href
    - total
- genres - list of genres the artist is creating in
- images - list with images for the artist, as a dictionary:
    - height
    - width
    - url
- popularity - popularity rating of the artist




## YT Music

## Discogs