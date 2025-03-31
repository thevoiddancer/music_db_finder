import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import dotenv
import os
import discogs_client as DiscogsClient

env_file_name = '.env'
dotenv.load_dotenv(env_file_name, override=True)

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
DISCOGS_USER_TOKEN = os.getenv('DISCOGS_USER_TOKEN')
YTMUSIC_REFRESH_TOKEN = os.getenv('YTMUSIC_REFRESH_TOKEN')
YTMUSIC_ACCESS_TOKEN = os.getenv('YTMUSIC_ACCESS_TOKEN')

def test_stored_env():
    assert SPOTIPY_CLIENT_ID
    assert SPOTIPY_CLIENT_SECRET
    assert DISCOGS_USER_TOKEN
    assert YTMUSIC_REFRESH_TOKEN
    assert YTMUSIC_ACCESS_TOKEN

def test_connection_ytmusic():
    from ytmusicapi import YTMusic as YTMusicClient
    import json

    with open('oauth.json__') as file:
        oauth = json.load(file)
    oauth['access_token'] = YTMUSIC_ACCESS_TOKEN
    oauth['refresh_token'] = YTMUSIC_REFRESH_TOKEN
    ytmusic = YTMusicClient()
    results = ytmusic.search('Hellraiser', filter='songs', limit=10)
    assert results
    assert 'Suicide Commando' in [artist['name'] for res in results for artist in res['artists']]


def test_connection_discogs():
    discogs_client = DiscogsClient.Client('ExampleApplication/0.1', user_token=DISCOGS_USER_TOKEN)
    result = discogs_client.search('Bind, Torture, Kill', type='release')
    assert result
    release = result._pages[1][0]
    assert release.title == 'Suicide Commando - Bind, Torture, Kill'
    assert release.master.title == 'Bind, Torture, Kill'
    artist = release.artists[0]
    assert artist.name == 'Suicide Commando'


def test_connection_spotify():
    spotify_auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
    spotify_client = spotipy.Spotify(client_credentials_manager=spotify_auth_manager)
    results = spotify_client.search('Bind, Torture, Kill', type='album', limit=50)
    album = results['albums']['items'][0]
    assert album['name'] == 'Bind, Torture, Kill'
    artist = album['artists'][0]
    assert artist['name'] == 'Suicide Commando'

