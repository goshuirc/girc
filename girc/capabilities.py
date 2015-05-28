#!/usr/bin/env python3
# Written by Daniel Oaks <daniel@danieloaks.net>
# Released under the ISC license


class Capabilities:
    """Ingests sets of client capabilities and provides access to them."""
    def __init__(self, wanted=[]):
        self.available = {}
        self.wanted = wanted
        self.enabled = []

    def ingest(self, cmd, parameters):
        cmd = cmd.casefold()

        if cmd == 'ls':
            caps = parameters[0].split(' ')

            for cap in caps:
                # strip first initial =/~
                if cap.startswith('='):
                    cap = cap[1:]

                if '=' in cap:
                    cap, value = cap.rsplit('=', 1)
                else:
                    value = True

                self.available[cap] = value

    def to_enable(self):
        l = []

        for cap in self.wanted:
            if cap in self.available:
                l.append(cap)

        return l

    def get(self, key, default=None):
        return self._dict.get(key, default)