#!/usr/bin/python
import gi
gi.require_version("Gst",'1.0')
from gi.repository import Gst, GObject,Gtk

client_id = 'enter_cliend_id'
stream_url = 'https://soundcloud.com/girlsgeneration_smtown/girls-generation-everyday-love'
mp3_stream_url = 'http://www.richardfarrar.com/audio/right.mp3'
track_stream_url = 'https://api.soundcloud.com/tracks/134204364/stream?client_id=' + client_id

def play_stream(music_stream_uri):
    music_stream_uri = "/home/pi/Documents/google-hackfair/hackfair-speech/resources/test_dj.mp3"
    #creates a playbin (plays media form an uri) 
    player = Gst.ElementFactory.make("playbin","player")
    print("player: ",player, " track_url: " + track_stream_url)    
    #set the uri
    #player.set_property('uri',"file://" +  music_stream_uri)
    player.set_property('uri',track_stream_url)

    #start playing
    player.set_state(Gst.State.PLAYING)


if __name__ == '__main__':
    Gst.init(None)
    play_stream(stream_url)

#wait and let the music play
raw_input('Press enter to stop playing...')
