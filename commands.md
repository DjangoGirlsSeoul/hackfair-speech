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

