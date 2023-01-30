#sh
v4l2-ctl --list-devices
v4l2-ctl --list-formats-ext


echo "Add the videocards into video file"
v4l2-ctl --list-devices | grep /dev/vide | awk {'print $1'} | xargs -i echo "{}" >> /tmp/video_card


echo "Lets start streams from the found video devices"
while read p; do
  echo "$p"
  ffmpeg -f v4l2 -i $p -pix_fmt yuv420p -preset ultrafast -b:v 600k -f rtsp rtsp://localhost:554/$p &
  sleep 5
done </tmp/video_card