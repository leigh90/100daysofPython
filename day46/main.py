from bs4 import BeautifulSoup
import requests
from decouple import config
# 2000-08-12
user_date = input("What year would you like to go to?")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
print(response)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
all_artists = soup.find_all(name="span",class_="chart-element__information__artist text--truncate color--secondary")
song_list = []
artist_list = []

for song in all_songs:
    # print(song.getText())
    song_list.append(song.getText())


# for artist in all_artists:
#     # print(artist.getText())
#     artist_list.append(artist.getText())

# print(len(song_list))
# print(len(artist_list))

# billboard_hottest = {artist_list[i] : song_list[i] for i in range(len(song_list))}
# print(billboard_hottest)

# SPOTIFY

SPOTIFY_CLIENT_ID = config("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = config("CLIENT_SECRET")
SPOTIFY_REDIRECT_URI=config("REDIRECT_URI")
# scope = "user-library-read"
scope="playlist-modify-private" 

# SPOTIFY API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# # WITHOUT AUTHENTICATION
# # sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))
# # results = sp.search(q='jordan davis', limit=20)
# # for idx, track in enumerate(results['tracks']['items']):
# #     print(idx, track['name'])

# OAUTH
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI,scope="user-library-read"))
results = sp.search(q='jordan davis', limit=20)

user_id = spotipy.client.Spotify.current_user(sp)
print(user_id)
# {'display_name': 'Leigh', 'external_urls': {'spotify': 'https://open.spotify.com/user/31pancwlwjcojay6bllzpnqxl67i'}, 'followers': {'href': None, 'total': 0}, 'href': 'https://api.spotify.com/v1/users/31pancwlwjcojay6bllzpnqxl67i', 'id': '31pancwlwjcojay6bllzpnqxl67i', 'images': [], 'type': 'user', 'uri': 'spotify:user:31pancwlwjcojay6bllzpnqxl67i'}
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# for artist, song in billboard_hottest.items():
#     results = sp.search(q=artist, limit=1)
#     for idx, track in enumerate(results['tracks']['items']):
#         print(idx, track['name'])



# CREATE SPOTIFY PLAYLIST FROM BILLBOARD SONGS
song_uris = []
year  = user_date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesnt exist in spotify, Skipped")


playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)