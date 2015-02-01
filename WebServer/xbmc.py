#!/bin/env/python

from xbmcjson import XBMC
from credentials import USER, PASSWORD

xbmc = XBMC("http://localhost:8052/jsonrpc", USER, PASSWORD)


def start_music():
    xbmc.Player.Stop({'playerid': 0})
    xbmc.Playlist.clear({"playlistid": 0})
    xbmc.Playlist.add({"playlistid": 0, "item": {"genreid": 2}})
    xbmc.Player.Open({'item': {'playlistid': 0}})
    print('done')
