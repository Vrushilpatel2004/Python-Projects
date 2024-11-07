import time
from plyer import notification #Plyer is a platform-independent Python API for accessing hardware features of various platforms

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Reminder to Drink Water Now !!",
            message = "Drinking Water Helps Maintain the Balance of Body Fluids.The functions of these bodily fluids include digestion, absorption, circulation, creation of saliva, transportation of nutrients, and maintenance of body temperature.",
            #app_icon = "C:\Users\Vrushil\waterglass.ico",
            timeout =2
        )
        time.sleep(60*60)