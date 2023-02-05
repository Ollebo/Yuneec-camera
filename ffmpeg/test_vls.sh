 /usr/bin/vlc-wrapper -vvv v4l2c:///dev/video5:width=640:height=480:chroma=H264 --sout '#rtp{sdp=rtsp://:8554/live}' --demux h264
