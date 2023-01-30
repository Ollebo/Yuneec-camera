#Import commands
from functions.photo import TAKE_PHOTO 
from functions.video import START_RECORD,STOP_RECORD





def commandSelect(CMD,data):
    #
    # This function will send the commands to the correct function
    if (CMD == "TAKE_PHOTO"):
        print("Taking phoyo")
        return TAKE_PHOTO(data)
    elif (CMD == "START_VIDEO"):
        print("Start Video")
    elif (CMD == "SET_PHOTO_SIZE"):
        return SET_PHOTO_SIZE(data)
    elif (CMD == "START_RECORD"):
        return START_RECORD(data)
    elif (CMD == "STOP_RECORD"):
        return STOP_RECORD(data)
    elif (CMD == "GET_FW_VERSION"):
        return GET_FW_VERSION(data)
    elif (CMD == "GET_STATUS"):
        return GET_STATUS(data)
    elif (CMD == "INIT_CAMERA"):
        return INIT_CAMERA(data)
    else:
        return default()


def SET_PHOTO_SIZE(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"rval":0, "msg_id":1} 

def GET_FW_VERSION(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    returnData={
        "rval":0,
        "msg_id":"11",
        "brand":"YUNEEC",
        "model":"CGO3",
        "YUNEEC_ver":"1.8.00(E)",
        "api_ver":"2.8.00",
        "fw_ver":"Jul 17 2015 14:02:17",
        "app_type":"sport",
        "logo":"/tmp/fuse_z/app_logo.jpg",
        "chip":"S2(A9)",
        "http":"disable" }
    return returnData   

def GET_STATUS(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    returnData={
        "rval":0, 
        "msg_id":1, 
        "cam_mode":"1",
        "status":"vf",
        "sdfree":"15191040",
        "sdtotal":"15549440",
        "record_time":"0",
        "white_balance":"0",
        "ae_enable":"1",
        "iq_type":"1",
        "exposure_value":"0.0",
        "video_mode":"3840x2160F30",
        "awb_lock":"0",
        "audio_sw":"1",
        "shutter_time":"60",
        "iso_value":"ISO_1600",
        "photo_format":"dng"}
    return returnData  



def INIT_CAMERA(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    returnData={
        "rval":0,
        "msg_id":"257",
        "param":1,
        "fw_ver":"1.8.00(E)",
        "cam_mode":"1",
        "status":"vf",
        "iq_type":"1",
        "white_balance":"0",
        "sdfree":"15191040",
        "sdtotal":"15549440",
        "exposure_value":"0.0",
        "video_mode":"3840x2160F30",
        "speed_rate":"6M",
        "sharpness":"6",
        "record_time":"0",
        "awb_lock":"0",
        "ae_enable":"1",
        "audio_sw":"1",
        "shutter_time":"60",
        "iso_value":"ISO_1600",
        "photo_format":"dng" }
    return returnData 



def default():
    # Defulat function if the command is not implemted then it end up here wirh response
    return  {"rval":0, "msg_id":1} 

