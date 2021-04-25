import numpy as np
from PIL import Image
from os import path as pth

def loadImage(path):
    print("Image loaded")
    return np.array(Image.open(path))

def saveImageFromArray(image,path):
    convertedImg = Image.fromarray(image)
    endIndex = path.index(".jpg")
    realPath = path[:endIndex] + "edited" + path[endIndex:]
    convertedImg.save(realPath)
    print("Image was saved")

def enhanceColor(barva):
    threshold = 150
    if(barva.lower() == "r"):
        tooHigh = image[:,:,0] > threshold
        image[tooHigh] = [255,0,0] 
        print("Red channel was enhanced")
    elif(barva.lower() == "g"):
        tooHigh = image[:,:,1] > threshold
        image[tooHigh] = [0,255,0] 
        print("Green channel was enhanced")
    elif(barva.lower() == "b"):
        tooHigh = image[:,:,2] > threshold
        image[tooHigh] = [0,255,0] 
        print("Blue channel was enhanced")
    else:
        print(barva + " is not a valit color")

def invertColors():
    global image
    inverted_Image = abs(255 - image)
    image = inverted_Image
   
def toBlackAndWhite():
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            #Musí tam bejt ty [0:] ?
            #TODO: Udělat to přes numpy místo nested for loopů
            prumer = (float(image[x][0:][y][0]) + float(image[x][0:][y][1]) + float(image[x][0:][y][2])) / 3
            image[x][0:][y][0] = prumer
            image[x][0:][y][1] = prumer
            image[x][0:][y][2] = prumer
    print("RGB converted to greyscale")

def mirrorHorizontally():
    #Jak by se to děalo bez .flip()????
    #bottom_halfInverted = image[int(image.shape[0]):-1:int(image.shape[0] / 2)-1,:,:]
    bottom_halfInverted = np.flip(image[int(image.shape[0] / 2):int(image.shape[0]),:,:],0)
    image[0:int((image.shape[0] / 2)),:,:] = bottom_halfInverted
    print("Mirroring was completed")

def mirrorVertically():
    left_halfInverted = np.flip(image[:,int(image.shape[1]/2):int(image.shape[1]),:],1)
    image[:,0:int(image.shape[1]/2),:] = left_halfInverted
    print("Mirroring was completed")

def sinDisortion():
    #TODO zachovat barvy = nesinovat třetí dimenzi
    waveHeight = image.shape[0] / 5
    waveMultiplier= 3/image.shape[1]
    for i in range(image.shape[1]):
        image[:,i] = np.roll(image[:,i],int(waveHeight * np.sin(2*np.pi*i * waveMultiplier)))
    print("Image was disorted")
def tanDisortion():
    waveHeight = image.shape[0] / 3
    waveMultiplier= 1/image.shape[1]
    for i in range(image.shape[1]):
        image[:,i] = np.roll(image[:,i],int(waveHeight * np.tan(2*np.pi*i * waveMultiplier)))

def chcekInputAction(action):
    print("Processing...")
    if(action[:-2].lower() == "enhcol"):
        if(action[-2:].lower().strip() == "r"):
            enhanceColor("r")
        elif(action[-2:].lower().strip() == "g"):
            enhanceColor("g")
        elif(action[-2:].lower().strip() == "b"):
            enhanceColor("b")
        else:
            print("Invalid color")
    elif(action.lower() == "invertcol"):
        invertColors()
    elif(action.lower() == "tobaw"):
        toBlackAndWhite()
    elif(action[:-4].lower() == "mirror"):
        if(action[-4:].lower().strip() == "ver"):
            mirrorVertically()
        elif(action[-4:].lower().strip() == "hor"):
            mirrorHorizontally()
        else:
            print("Invalid argument")
    elif(action[:-4].lower() == "disort"):
        if(action[-4:].lower().strip() == "sin"):
            sinDisortion()
        elif(action[-4:].lower().strip() == "tan"):
            tanDisortion()
        else:
            print("Invalid argument")
    else:
        print("Invalid action")


path = input("Image file path: ")
if pth.exists(path):
   image = loadImage(path)
   while(True):
       editAction = input("Enter edit action:\n ENHCOL R/G/B \n INVERTCOL \n TOBAW \n MIRROR ver/hor\n DISORT sin/tan \n")
       chcekInputAction(editAction)
       continueEdit = input("NEXT/END\n").lower()
       if(continueEdit.lower() == "end"):
            saveImageFromArray(image,path)
            break
