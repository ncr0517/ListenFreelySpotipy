#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

os.environ["SPOTIPY_CLIENT_ID"] = "4ea0770420a94160955f4b372053c50f"
os.environ["SPOTIPY_CLIENT_SECRET"] = "d6336e14ce1a4c3681e1c5ae6ef60067"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"

#logger = logging.getLogger('examples.create_playlist')
#logging.basicConfig(level='DEBUG')

#collects user information
def get_args():
    playlistName = input('Enter a playlist name --> ')
    playlistDescription = input('Enter a playlist description --> ')
    username = input('Enter your spotify username --> ')
    numSong = int(input('How many recent songs in your playlist? --> '))
    return playlistName, playlistDescription, username, numSong


def main():
    playlistName, playlistDescription, username, numSong = get_args()
    scope = "playlist-modify-public user-read-recently-played playlist-modify-public"
    token = util.prompt_for_user_token(username, scope)
    print("SUCCESS")
    sp = spotipy.Spotify(auth=token)
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user_id, playlistName, True, playlistDescription)
    playlist_id = playlist["id"]
    tracks = []
    for item in sp.current_user_recently_played(limit=numSong)["items"]:
        tracks.append(item["track"]["id"])
    sp.user_playlist_add_tracks(user_id, playlist_id, tracks, position=None)


if __name__ == '__main__':
    main()

