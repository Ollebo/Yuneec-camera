#
#

Diffrent ffmpeg test
ffmpeg  -f v4l2 -input_format mjpeg  -video_size 1920x1080 -i /dev/video5  -tune zerolatency   -f rtsp  rtsp://localhost:554/live


ffmpeg -f v4l2 -list_formats all -i /dev/video5


ffmpeg  -f v4l2 -input_format yuyv422  -video_size 1920x1080 -i /dev/video5 -vcodec libx264 -tune zerolatency   -f rtsp  rtsp://localhost:554/live
ffmpeg  -f v4l2 -input_format yuyv422  -video_size 1920x1080 -i /dev/video5    -f rtsp  rtsp://localhost:554/live
ffmpeg  -f v4l2 -input_format yuyv422  -video_size 1920x1080 -i /dev/video5 -vcodec libx264 -tune zerolatency   -f rtsp  rtsp://localhost:554/live
ffmpeg  -f v4l2 -input_format mjpeg  -video_size 1920x1080 -i /dev/video5 -vcodec libx264 -tune zerolatency   -f rtsp  rtsp://localhost:554/live
ffmpeg  -f v4l2 -input_format mjpeg  -video_size 1920x1080 -i /dev/video5  -tune zerolatency   -f rtsp  rtsp://localhost:554/live