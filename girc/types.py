#!/usr/bin/env python3
# Written by Daniel Oaks <daniel@danieloaks.net>
# Released under the ISC license
from .utils import NickMask


class ServerConnected:
    """Something that's connected to an IRC server."""
    def __init__(self, server_connection):
        self.s = server_connection


class User(ServerConnected):
    """An IRC user."""
    def __init__(self, server_connection, nickmask):
        super().__init__(server_connection)

        user = NickMask(nickmask)
        self.nick = user.nick
        self.user = user.user
        self.host = user.host

        self.channels = []

    @property
    def channels(self):
        chanlist = []

        for channel in self._channels:
            chanlist.append(self.s.channels[channel])

        return chanlist

    @channels.setter
    def channels(self, chanlist):
        self._channels = self.s.ilist(chanlist)
    

class Channel(ServerConnected):
    """An IRC channel."""
    def __init__(self, server_connection, channel_name):
        super().__init__(server_connection)

        self.name = channel_name

        self.users = {}

    @property
    def users(self):
        userlist = {}

        for nick in self._users:
            userlist[nick] = self.s.users[nick]

        return userlist

    @users.setter
    def users(self, userlist):
        self._users = self.s.idict()