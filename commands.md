## Useful commands

#### Record

```bash
arecord --device=hw:1,0 --format S16_LE --rate 44100 -c 2 test.wav
```

#### Convert Wav to Flac

##### convert to flac using ffmpeg

```bash
ffmpeg -i test.wav -b:a 16000 -c:a flac test.flac

```

##### conver to mono channel flack

```bash
ffmpeg -i test.flac -ac 1 mono.flac

```

#### Play 

#### Using OmxPlayer

```bash
omxplayer -o local mono.flac

```

#### Debug commands

##### Check usb devices

```bash
dmesg | grep C-Media
lsusb
```

#### Playback devices

```bash
pi@raspberrypi ~ $ aplay -l

**** List of PLAYBACK Hardware Devices ****

```

#### Show sound card setting

```bash 
cat ~/.asoundrc

```

#### Misc

##### Kill process

```bash 
pkill -9 <pid>
```
```bash 
sudo ps aux | grep "python transcribe_streaming.py" | grep -v grep | awk '{print $2}' | xargs sudo kill -9

```


#### Resources

[raspberry pi with alsa](http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/)
[gstreamer tutorial](http://brettviren.github.io/pygst-tutorial-org/pygst-tutorial.pdf)
[gstreamer download](https://gstreamer.freedesktop.org/download/)
[gstreamer code snippets](https://github.com/rubenrua/GstreamerCodeSnippets)
[gstreamer blog](http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/)
[Daemon service](https://web.archive.org/web/20160305151936/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/)
[Daemon example](https://bitbucket.org/dnetman99/raspberrypiprojects)

##### Python packages
[pyAudio](http://people.csail.mit.edu/hubert/pyaudio/)
[Best practice Speech API](https://cloud.google.com/speech/docs/best-practices#language_support)

#### Raspberry pi 
[USB Audio](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/)
