import numpy as np
from PIL import Image

def loadImage(path):
    print("Image loaded")
    return np.array(Image.open(path))

def saveImageFromArray(image,path):
    convertedImg = Image.fromarray(image)
    convertedImg.save(path)
    print("Image was saved")

def enhanceColor(barva):
    threshold = 200
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

def invertColors():
    global image
    inverted_Image = abs(255 - image)
    image = inverted_Image
    
def toBlackAndWhite():
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            #Musí tam bejt ty [0:] ?
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
#toBlackAndWhite()
image = loadImage("C:\\Users\\Uživatel\\Desktop\\starladder.jpg")
#invertColors()
#toBlackAndWhite()
#mirrorHorizontally()
mirrorVertically()
saveImageFromArray(image,"C:\\Users\\Uživatel\\Desktop\\starladderedited.jpg")