#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:33:54 2020

@author: nithinravi
"""

import os
import sys
import json

import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

os.environ["SPOTIPY_CLIENT_ID"] = "CLIENT_ID_HERE"
#sys.argv[1]
os.environ["SPOTIPY_CLIENT_SECRET"] = "CLIENT_SECRET_HERE"
#sys.argv[2]
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"

logger = logging.getLogger('examples.create_playlist')
logging.basicConfig(level='DEBUG')


#inputs to take: before a certain time. After a certain time. These are inputs to current user recently played
#username (done later)


def get_args():
    #parser = argparse.ArgumentParser(description='Creates a playlist for user')
    #parser.add_argument('-p', '--playlist', required=True,
    #                    help='Name of Playlist')
    #parser.add_argument('-d', '--description', required=False, default='',
    #                    help='Description of Playlist')
    playlistName = input('Enter a playlist name --> ')
    playlistDescription = input('Enter a playlist description --> ')
    username = input('Enter a spotify username --> ')
    numSong = int(input('How many recent songs in your playlist? --> '))
    return playlistName, playlistDescription, username, numSong


def main():
    #args = get_args()
    playlistName, playlistDescription, username, numSong = get_args()
    scope = "playlist-modify-public user-read-recently-played playlist-modify-public"
    uir = "http://localhost:8080"
    token = util.prompt_for_user_token(username, scope, None, None, uir)
    print("SUCCESS")
    sp = spotipy.Spotify(auth=token)
    user_id = sp.me()['id']
    print("mark" + user_id)
    playlist = sp.user_playlist_create(user_id, playlistName, True, playlistDescription)
    playlist_id = playlist["id"]
    tracks = []
    for item in sp.current_user_recently_played(limit=numSong)["items"]:
        tracks.append(item["track"]["id"])
    sp.user_playlist_add_tracks(user_id, playlist_id, tracks, position=None)


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
