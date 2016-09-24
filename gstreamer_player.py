
#!/usr/bin/env python

import sys, os
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk


class GTK_Player(object):

    def __init__(self,stream_url):
        Gst.init(None)
        self.player = Gst.ElementFactory.make("playbin", "player")
        self.player.set_property("uri", stream_url)
        self.start = False
        
    def start_stop(self):
        if not self.start:
            self.player.set_state(Gst.State.PLAYING)
            self.start = True
        else:
            self.player.set_state(Gst.State.NULL)

    def on_message(self, bus, message):
        #implement later#
        pass
