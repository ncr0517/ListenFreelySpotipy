#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:33:54 2020

@author: nithinravi
"""

import os
import sys

import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

os.environ["SPOTIPY_CLIENT_ID"] = "4ea0770420a94160955f4b372053c50f"
#sys.argv[1]
os.environ["SPOTIPY_CLIENT_SECRET"] = "d6336e14ce1a4c3681e1c5ae6ef60067"
#sys.argv[2]
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"

logger = logging.getLogger('examples.create_playlist')
logging.basicConfig(level='DEBUG')


#inputs to take: before a certain time. After a certain time. These are inputs to current user recently played
#username (done later)


def get_args():
    parser = argparse.ArgumentParser(description='Creates a playlist for user')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Name of Playlist')
    parser.add_argument('-d', '--description', required=False, default='',
                        help='Description of Playlist')
    return parser.parse_args()


def main():
    args = get_args()
    scope = "playlist-modify-public user-read-recently-played"
    uir = "http://localhost:8080"
    username = "ncr0517"
    token = util.prompt_for_user_token(username, scope, None, None, uir)
    
    print("SUCCESS")
    sp = spotipy.Spotify(auth=token)
    #sp = spotipy.Spotify(auth=token)
    #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = sp.me()['id']
    print("mark" + user_id)
    for item in sp.current_user_recently_played(limit=1):
        print(item + "\n")
    #sp.user_playlist_create(user_id, args.playlist)


if __name__ == '__main__':
    main()
    
# =============================================================================
# os.environ["SPOTIPY_CLIENT_ID"] = sys.argv[1]
# os.environ["SPOTIPY_CLIENT_SECRET"] = sys.argv[2]
# os.environ["SPOTIPY_REDIRECT_URI"] = sys.argv[3]
# =============================================================================]

# =============================================================================
# PORT_NUMBER = 8080
# SPOTIPY_CLIENT_ID = sys.argv[1]
# SPOTIPY_CLIENT_SECRET = sys.argv[2]
# SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
# SCOPE = 'user-library-read'
# CACHE = '.spotipyoauthcache'
# 
# token = oauth2.SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
# 
# cache_token = token.get_access_token()
# spotify = spotipy.Spotify(cache_token)
# 
# results1 = spotify.user_playlist_tracks(USER, PLAY_LIST, limit=100, offset=0)
# 
# print(results1)
# =============================================================================

# =============================================================================
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# 
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
# 
# for album in albums:
#     print(album['name'])
# =============================================================================
