def commandSelect(CMD,data):
    #
    # This function will send the commands to the correct function
    if (CMD == "TAKE_PHOTO"):
        print("Taking phoyo")
    elif (CMD == "START_VIDEO"):
        print("Start Video")
    elif (CMD == "SET_PHOTO_SIZE"):
        return SET_PHOTO_SIZE(data)    
    else:
        return default()


def SET_PHOTO_SIZE(data):
    #Set the phoyo size
    MODE = data.get('MODE')
    print(MODE)
    return {"rval":0, "msg_id":1} 



def default():
    # Defulat function if the command is not implemted then it end up here wirh response
    return  {"rval":0, "msg_id":1} 

