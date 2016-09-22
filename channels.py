import pyaudio

pa = pyaudio.PyAudio()
for x in range(0,pa.get_device_count()):
    print("X :", str(x),pa.get_device_info_by_index(x))
