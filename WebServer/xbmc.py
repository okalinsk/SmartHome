#!/bin/env/python

from xbmcjson import XBMC


class Xbmc:
    def __init__(self, user, password):
        self.xbmc = XBMC("http://localhost:8052/jsonrpc", user, password)

    def start_music(self):
        self.xbmc.Player.Stop({'playerid': 0})
        self.xbmc.Playlist.clear({"playlistid": 0})
        self.xbmc.Playlist.add({"playlistid": 0, "item": {"genreid": 2}})
        self.xbmc.Player.Open({'item': {'playlistid': 0}})
