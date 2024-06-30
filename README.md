```sh
~$ docker run --rm -it --network=host bluenviron/mediamtx:latest
2024/06/03 22:00:49 INF MediaMTX v1.8.2
2024/06/03 22:00:49 INF configuration loaded from /mediamtx.yml
2024/06/03 22:00:49 INF [RTSP] listener opened on :8554 (TCP), :8000 (UDP/RTP), :8001 (UDP/RTCP)
2024/06/03 22:00:49 INF [RTMP] listener opened on :1935
2024/06/03 22:00:49 INF [HLS] listener opened on :8888
2024/06/03 22:00:49 INF [WebRTC] listener opened on :8889 (HTTP), :8189 (ICE/UDP)
2024/06/03 22:00:49 INF [SRT] listener opened on :8890 (UDP)

// Check if port not available (conflict with default port of Jupyter Lab)
~$ sudo lsof -i -P -n | grep 8888
```

```sh
~$ sudo apt update
~$ sudo apt install ffmpeg
~$ ffmpeg -version
ffmpeg version 6.1.1-3ubuntu5 Copyright (c) 2000-2023 the FFmpeg developers
built with gcc 13 (Ubuntu 13.2.0-23ubuntu3)
configuration: --prefix=/usr --extra-version=3ubuntu5 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --disable-omx --enable-gnutls --enable-libaom --enable-libass --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgme --enable-libgsm --enable-libharfbuzz --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-openal --enable-opencl --enable-opengl --disable-sndio --enable-libvpl --disable-libmfx --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-ladspa --enable-libbluray --enable-libjack --enable-libpulse --enable-librabbitmq --enable-librist --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libx264 --enable-libzmq --enable-libzvbi --enable-lv2 --enable-sdl2 --enable-libplacebo --enable-librav1e --enable-pocketsphinx --enable-librsvg --enable-libjxl --enable-shared
libavutil      58. 29.100 / 58. 29.100
libavcodec     60. 31.102 / 60. 31.102
libavformat    60. 16.100 / 60. 16.100
libavdevice    60.  3.100 / 60.  3.100
libavfilter     9. 12.100 /  9. 12.100
libswscale      7.  5.100 /  7.  5.100
libswresample   4. 12.100 /  4. 12.100
libpostproc    57.  3.100 / 57.  3.100

// Publish a video file with FFmpeg
~$ ffmpeg -re -stream_loop -1 -i /home/yungshun317/workspace/py/cv-rtsp/videos/1080P_4000K_284922402.mp4  -c copy -f rtsp rtsp://localhost:8554/stream
```
