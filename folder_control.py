import os
def check():
    try :
        if (os.path.exists("C:/Images/")) == True:
            os.chdir("C:/Images")
        else:
            os.mkdir("C:/Images")
            os.chdir("C:/Images")

    except :
        print("Directory Opening and Making Failure")
def check2():
    try :
        if (os.path.exists("C:/Cropped_Images/")) == True:
            os.chdir("C:/Cropped_Images/")
        else:
            os.mkdir("C:/Cropped_Images/")
            os.chdir("C:/Cropped_Images/")

    except :
        print("Directory Opening and Making Failure")