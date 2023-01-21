#
#
# Answer the API call and trigegrs a CLI Commands using subcall 
# To take images from every stream configured

import asyncio
import cv2
import os
import cv2
import time
from datetime import datetime
import getpass

async def takePhotos(stream,id):
    '''
    Command to take the photos froms stream 
    '''
    RTSP_URL = 'rtsp://127.0.0.1/live'

    os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;tcp'
    cap = cv2.VideoCapture(RTSP_URL)
    fps = cap.get(cv2.CAP_PROP_FPS)

    frameRate = cap.get(5) #frame rate
    counter=0

    startImagesCount = int(str(datetime.now().strftime("%S")))
    while cap.isOpened():
        start_time = time.time()
        frameId = cap.get(1)  # current frame number
        ret, frame = cap.read()

        if (ret != True):
            break
        imagesCount = int(str(datetime.now().strftime("%S")))

        filename = "images/image_" + str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S"))  + ".jpg"

        cv2.imwrite(filename, frame)
        cv2.waitKey(1)
        #
        #
        # Deping on the frame rate we add images for 3 sec to be shoure we get any image with all frames.
        #
        if imagesCount > startImagesCount+2:
            cap.release()
            break





def TAKE_PHOTO(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    asyncio.run(takePhotos("stream",2))
    return {"rval":0, "msg_id":1} 