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
    elif (CMD == "INDEX_PAGE"):
        return INDEX_PAGE(data)
    elif (CMD == "SET_TIME"):
        return SET_TIME(data)
    elif (CMD == "get_bind_state"):
        return get_bind_state(data)
    elif (CMD == "request_bind"):
        return request_bind(data)
    elif (CMD == "GET_PANORAMA_STATUS"):
        return GET_PANORAMA_STATUS(data)
    elif (CMD == "GET_FW_VERSION"):
        return GET_FW_VERSION(data)
    elif (CMD == "SET_RTSP_VID"):
        return SET_RTSP_VID(data)
    else:
        return default()


def SET_RTSP_VID(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"rval":0,"msg_id":"373"}



def GET_FW_VERSION(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"rval":0,"msg_id":"11","brand":"YUNEEC","model":"CGO3+","YUNEEC_ver":"3.2.34(A)","api_ver":"2.8.00","fw_ver":"Jan 11 2017 11:47:55","app_type":"sport","logo":"/tmp/fuse_z/app_logo.jpg",
"chip":"S2E(A9S)","http":"disable","Lens":"LianChuang2","soft_ver":"30234"}



def GET_PANORAMA_STATUS(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"rval":0, "msg_id":"397","all_pic":"8","taken_pic":"0","take_action":"0" }



def request_bind(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"result":"ok", "server_mac_address":"b8:13:32:4a:46:0e"}



def get_bind_state(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"isbinded":"yes", "binded_client_address":"e0:b6:f5:80:2e:99"} 



def SET_TIME(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"rval":0,"msg_id":"336", "type":"camera_clock" } 


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

def INDEX_PAGE(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    returnData={
        "rval": 0,
        "msg_id": "257",
        "param": "1",
        "fw_ver": "3.2.34(E)",
        "cam_mode": "1",
        "status": "vf",
        "iq_type": "1",
        "white_balance": "0",
        "sdfree": "26250240",
        "sdtotal": "31154176",
        "exposure_value": "0.0",
        "video_mode": "1920x1080F30",
        "speed_rate": "54M auto",
        "record_time": "0",
        "awb_lock": "0",
        "ae_enable": "1",
        "audio_sw": "1",
        "shutter_time": "30",
        "iso_value": "ISO_600",
        "photo_format": "jpg",
        "audio_enable": "1",
        "rtsp_res": "720P",
        "photo_mode": "1",
        "photo_num": "1",
        "photo_times": "1",
        "ev_step": "0.000000",
        "interval_ms": "333",
        "soft_ver": "30234",
        "cam_scene": "0",
        "left_time": "0",
        "metering_mode": "2",
        "x_ratio": "0.00",
        "y_ratio": "0.00",
        "layers": "1",
        "pitch": "0",
        "yaw": "60",
        "timer_photo_sta": "0"

    }

    return returnData 

def GET_STATUS(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    returnData={"rval":0, "msg_id":1, "cam_mode":"1", "status":"vf","sdfree":"0","sdtotal":"0","record_time":"0","white_balance":"0","ae_enable":"1","iq_type":"0","exposure_value":"0.0","video_mode":"3840x2160F30","awb_lock":"0","audio_sw":"1","shutter_time":"30","iso_value":"ISO_3200","photo_format":"jpg", "rtsp_res":"720P", "photo_mode":"3", "photo_num":"0", "photo_times":"1", "ev_step":"0.000000", "interval_ms":"1000", "cam_scene":"0", "audio_enable":"1","left_time": "0","metering_mode":"2","x_ratio":"0.00","y_ratio":"0.00", "layers":"0", "pitch":"0", "yaw":"0", "timer_photo_sta":"0" }
    returnData2={
        "rval": 0,
        "msg_id": 1,
        "cam_mode": "1",
        "status": "vf",
        "sdfree": "26250240",
        "sdtotal": "31154176",
        "record_time": "0",
        "white_balance": "0",
        "ae_enable": "1",
        "iq_type": "1",
        "exposure_value": "0.0",
        "video_mode": "1920x1080F30",
        "awb_lock": "0",
        "audio_sw": "1",
        "shutter_time": "30",
        "iso_value": "ISO_600",
        "photo_format": "jpg",
        "rtsp_res": "720P",
        "photo_mode": "1",
        "photo_num": "1",
        "photo_times": "1",
        "ev_step": "0.000000",
        "interval_ms": "333",
        "cam_scene": "0",
        "audio_enable": "1",
        "left_time": "0",
        "metering_mode": "2",
        "x_ratio": "0.00",
        "y_ratio": "0.00",
        "layers": "1",
        "pitch": "0",
        "yaw": "60",
        "timer_photo_sta": "0"
    }
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

