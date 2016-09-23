#!/bin/bash

set -e

echo "Recording .. Press Ctrl+C to stop"
#arecord -D “plughw:1,0” -q -f cd -t wav | ffmpeg -loglevel panic -y -i – -ar 16000 -acodec flac file.flac > /dev/null 2>&1
arecord --device=hw:1,0 --format S16_LE --rate 44100 -c1 test.wav

# add a way to send request to google speech api server
#ffmpeg -i test2.wav -b:a 16000 -c:a flac test2.flac
#ffmpeg -i test2.flac -ac 1 mono.flac
