import os
from flask import Flask, request, redirect, session, url_for
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id = '07929cf3a1014bca946866307d0f1f60'
client_secret = 'ab27740f650043eb9c602b2620e697ff'
redirect_uri = 'http://localhost:5000/callback'
scope = 'playlist-read-private'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True
)
sp = Spotify(auth_manager=sp_oauth)

@app.route('/')
def home():
    token_info = cache_handler.get_cached_token()
    if not sp_oauth.validate_token(token_info):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('get_playlists'))

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    cache_handler.save_token_to_cache(token_info)
    return redirect(url_for('get_playlists'))

@app.route('/get_playlists')
def get_playlists():
    token_info = cache_handler.get_cached_token()
    if not sp_oauth.validate_token(token_info):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

    try:
        playlists = sp.current_user_playlists()
        playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
        playlists_html = '<br>'.join([f'{name}: {url}' for name, url in playlists_info])
    except Exception as e:
        playlists_html = f"Error fetching playlists: {str(e)}"

    return playlists_html

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)