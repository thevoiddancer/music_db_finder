from music_db_finder.fuzz_helpers import get_discogs_name, get_name_as_str, obj_ratio

import discogs_client as DiscogsClient
from discogs_client.models import Artist
import os

DISCOGS_USER_TOKEN = os.getenv("DISCOGS_USER_TOKEN")
discogs_client = DiscogsClient.Client(
    "ExampleApplication/0.1", user_token=DISCOGS_USER_TOKEN
)
data = {
    "id": 20055,
    "type": "artist",
    "user_data": {"in_wantlist": False, "in_collection": False},
    "master_id": None,
    "master_url": None,
    "uri": "/artist/20055-Grendel",
    "title": "Grendel",
    "thumb": "https://i.discogs.com/NOtmovOr-b4_dUzWxTw4F0xH6APaiZPcyz3zgaA56eI/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTIwMDU1/LTExMDg1ODQ2NjAu/Z2lm.jpeg",
    "cover_image": "https://i.discogs.com/Efy4HlVUzYTnyncLHk9piMZryZ1KeKwsgoUXevdXkqk/rs:fit/g:sm/q:90/h:193/w:258/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTIwMDU1/LTExMDg1ODQ2NjAu/Z2lm.jpeg",
    "resource_url": "https://api.discogs.com/artists/20055",
    "name": "Grendel",
}

artist_discogs = Artist(discogs_client, data)

# Spotify
artist_spotify = {
    "external_urls": {
        "spotify": "https://open.spotify.com/artist/28D0LIS1y01QS8fbh9dXVk"
    },
    "followers": {"href": None, "total": 49522},
    "genres": ["aggrotech", "cyberpunk", "ebm", "futurepop", "industrial metal"],
    "href": "https://api.spotify.com/v1/artists/28D0LIS1y01QS8fbh9dXVk",
    "id": "28D0LIS1y01QS8fbh9dXVk",
    "images": [
        {
            "height": 640,
            "url": "https://i.scdn.co/image/ab6761610000e5ebc76c7a2e21ef46bc86c02bf8",
            "width": 640,
        },
        {
            "height": 320,
            "url": "https://i.scdn.co/image/ab67616100005174c76c7a2e21ef46bc86c02bf8",
            "width": 320,
        },
        {
            "height": 160,
            "url": "https://i.scdn.co/image/ab6761610000f178c76c7a2e21ef46bc86c02bf8",
            "width": 160,
        },
    ],
    "name": "Grendel",
    "popularity": 30,
    "type": "artist",
    "uri": "spotify:artist:28D0LIS1y01QS8fbh9dXVk",
}

# ytmusic
artist_ytmusic = {
    "category": "Artists",
    "resultType": "artist",
    "artist": "Grendel",
    "shuffleId": "RDAOX3Dp7AWJM1nNlHmtHf9DVg",
    "radioId": "RDEMX3Dp7AWJM1nNlHmtHf9DVg",
    "browseId": "UCFeXJhNBcNWydmK_PRRSB-A",
    "thumbnails": [
        {
            "url": "https://lh3.googleusercontent.com/ALMN78i7pf_vX6CqT_DOAdTDEIhwicr9LMiUPIAPkno0Lwt6sP8HU4vNy79wLquCwFBdoidE8Z8vFeq93Q=w60-h60-l90-rj",
            "width": 60,
            "height": 60,
        },
        {
            "url": "https://lh3.googleusercontent.com/ALMN78i7pf_vX6CqT_DOAdTDEIhwicr9LMiUPIAPkno0Lwt6sP8HU4vNy79wLquCwFBdoidE8Z8vFeq93Q=w120-h120-l90-rj",
            "width": 120,
            "height": 120,
        },
    ],
}
