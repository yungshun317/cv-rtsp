import ffmpeg

stream = ffmpeg.input('rtsp://120.125.10.221:554/chID=2&streamType=main')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)