# Yuneec-camera


Project to make a raspberry ore small comoter work as camera for the Yuneec Drone


## Flow
Use ffmpeg to start a video stream and send to a rtsp-simple-server.
From the rtsp server the st16 controller and other should be able to see stream.
The rtsp server also can converts streams to lower qualty if need and lower framerate.

Api server that lisses on CGI calls from the controller. The Api server can then triggers command.
Phots and videos are saved from the rtsp stream.


### Support for multi camera
The rtsp server can stream many difrents stream. Only one stream can be sent back to the controller. But the api will we able to recors and take phots from all streams.
Have not yeat come up with the ide how you can swap cameras during flight
Possible to start the ffpmeg with python and then change the stream. Ore using the RTSP api and from there change the stream name.... Lets se 


### Test video
To test the video you can start ony the rtsp server and then test to stream for your raspberry ore rock against the rtsp server.
On Rock i hade to test my way to find the correct video device

'''
ffmpeg -f v4l2 -i /dev/video4 -pix_fmt yuv420p -preset ultrafast -b:v 600k -f rtsp rtsp://localhost:554/live
'''


To watch the stream then I use mplayer on ubuntu

'''
mplayer rtsp://IP/live
'''


This will also be the way to setup correct framerate and settings for you video.
Its possible to stream high video to the RTSP server on /high. Then using the rtsp server lower the video quality and stream it to /live for the st16 controller.
Photos can be alter using env to from what stream images should be taken from.




### Network hostspot with hostapd
Then started a docker container is started that set the IP address for wlan0 (Ore any other wlan config in docker-compose file)
And bring up a wifi AP to be connected.

You can with ENV in the docker file configure the settings


## Dev
As a dev you can use the docker compose to start up the dev enviroment.
It includes a ffmpeg that stream from you locak webcam. rtsp Server and the API.
You can test the aoi with the test curl from the test folder.

## Deploy
Then the deploy folder follow the instructions how the setup you devices to run on diffrent yuneec drones.


## Communicate


### Info
Info was found from the execelent repo github.com. Info from that repo made all the commanda and stream possible to setup.
So all credit to  

### API /CGI Commands
Commanda are using the following setup

http://192.168.42.1/cgi-bin/cgi?CMD=INDEX_PAGE

http://192.168.42.1/cgi-bin/cgi?CMD=SET_WIFI_SPEED&rate=9


Result starts with return value rval. This indicates if the command was successful or not.

In case the CGI command was received and accepted rval is 0 and message ID is > 0.
Example: {"rval":0, "msg_id":1, …}

rval < 0 are error codes, 
msg_id:0 means unknown message – check if all was proper written, no wrong spaces and so on. Not all commands will be accepted by your camera.




|  Commands |  Args  |   |   | Workinng  |
|---|---|---|---|---|
| INDEX_PAGE|||||
|GET_TIME|||||
|SET_TIME|||||
|QUERY_SD_FIRMWARE|||||
|DECOMPRESS_UPLOADED_FILE|||||
|GET_DECOMPRESS_PROGESS|||||
|SET_UPDATE_FILE_TYPE|||||
|UPGRADE_PKG|||||
|GET_UPGRADE_PROGESS|||||
|DEL_ALL_FIRMWARE|||||
|DEL_MEDIA_FILE|||||
|rtsp|||||
|GET_FW_VERSION|||||
|START_RECORD|||||
|STOP_RECORD|||||
|U|||||
|STOP_SHUTTER|||||
|GET_SHUTTER_STATE|||||
|SET_PHOTOMODE_BURST|||||
|GET_PHOTOMODE|||||
|SET_PHOTOMODE_TIMELAPSE|||||
|SET_PHOTOMODE_PANORAMA|||||
|SET_PHOTOMODE_SINGLE|||||
|GET_STATUS|||||
|DETECT_CARD|||||
|FORMAT_CARD|||||
|GET_REC_TIME|||||
|REST_VF|||||
|STOP_VF|||||
|SET_PHOTO_SIZE|||||
|GET_PHOTO_SIZE|||||
|GET_BATTERY_LEVEL|||||
|SET_SETTING|||||
|GET_SETTING|||||
|SET_VIDEO_STANDARD|||||
|GET_VIDEO_STANDARD|||||
|SET_FOV|||||
|GET_FOV|||||
|DETECT_CARD|||||
|GET_SPACE|||||
|GET_SPACE_FREE|||||
|GET_TOTAL_SPACE|||||
|GET_CARD_FORMAT|||||
|SET_PHOTO_MODE|||||
|GET_PHOTO_MODE|||||
|RESET_DEFAULT|||||
|SET_AUDIO_SW|||||
|GET_AUDIO_SW|||||
|SET_PHOTO_FORMAT|||||
|GET_PHOTO_FORMAT|||||
|SET_AE_ENABLE|||||
|GET_AE_ENABLE|||||
|SET_SH_TM_ISO|||||
|GET_SH_TM_ISO|||||
|SET_IQ_TYPE|||||
|GET_IQ_TYPE|||||
|SET_WHITEBLANCE_MODE|||||
|GET_WHITEBLANCE_MODE|||||
|SET_EXPOSURE_VALUE|||||
|GET_EXPOSURE_VALUE|||||
|SET_VIDEO_MODE|||||
|GET_VIDEO_MODE|||||
|SET_CAM_MODE|||||
|GET_CAM_MODE|||||
|GET_CAM_SCENE|||||
|SET_CAM_SCENE|||||
|RESET_STATUS|||||
|request_bind|||||
|get_bind_state|||||
|SET_RTSP_VID|||||
|GET_RTSP_VID|||||
|GET_METERING_MODE|||||
|SET_METERING_MODE|||||
|SET_SPOT_METER_COORDS|||||
|GET_PANORAMA_STATUS|||||
|GET_CAM_SCENE|||||
|GET_CAMERA_PKG_SOFT_VERSION|||||
|SET_FTP_INFO|||||
|GET_FTP_STATUS|||||
|SET_WIFI_SPEED|||||
|GET_WIFI_SPEED|||||
|SET_SHARPNESS|||||
|GET_SHARPNESS|||||
|   |   |   |   |   |
|   |   |   |   |   |





### Streams
There are diffrent streams that the drone send.

#### CGO2+/CGO3/CGO3+
Media files:		http://192.168.42.1/DCIM/100MEDIA/

Live stream:		rtsp://192.168.42.1/live   *Working*

#### CGO-ET
Natural live stream:	rtsp://192.168.42.1:554/live *working*

Thermal stream:	rtsp://192.168.42.1:8554/live

#### MK58/GoPro
Live stream:		rtsp://192.168.110.1/cam1/h264

### Lumix/GCO4
Live stream:	rtsp://192.168.73.254:8557/PSIA/Streaming/channels/2?videoCodecType=H.264
