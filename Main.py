import cv2
import faceDectection
import storeFaces
import faceReco
import time

yesIntent = ['yes','Yes','Y','y','YES','Hopefully','hopefully','YUP','yup','Yup']
noIntent = ['no','n','No','N','NO']
whyIntent = ['Why','why','WHY']
doubtIntent = ['maybe','Maybe','may be','May Be','May be','MAYBE','MAY BE',"I doubt","i doubt","I doubt",'I DOUBT']

print("Hello there")

while True:
    store = input("Have we met Earlier: ")

    if store in yesIntent:
        print("Welcome back! \nLets get started with Detection")
        print("I hope you remember that to exit you need to press that small key in the 'Top Left' corner")
        faceDectection.face_detect()
        break
    elif store in noIntent:
        print("""In that case I would be missing some of the important details
        which I hope you won't mind be collecting""")
        storeFaces.face_Store()
        print("Before we begin please make sure that for exiting the camera you may do anything but press 'ESCAPE' key")
        print("Thank you for all the deatils\n Lets get started with Detection")
        faceReco.face_reco()
        break
    elif store in whyIntent:
        print("So that I can show you a Magic Trick")
    elif store in doubtIntent:
        print("""In that case Let's collect all the details again""")
        storeFaces.face_Store()
        print("Before we begin please make sure that for exiting the camera you may do anything but press 'ESCAPE' key")
        print("Thank you for all the deatils\n Lets get started with Detection")
        faceReco.face_reco()
        break
    else:
        print("I too love jokes, but would you please let me about our earlier meeting so thaat we can enjoy the magic!")
print("Bye, See you later\nHave a nice day!")
time.sleep(1)

