import cv2
import os
import cv2
import time
from datetime import datetime
import getpass
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




        

#cv2.destroyAllWindows()
#releasing camera immediately after capturing picture
