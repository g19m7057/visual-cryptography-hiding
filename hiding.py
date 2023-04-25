import sys

def getColumns(cleanedImage):
    info = cleanedImage[1].split()
    width = info[0]
    return width
    
def getRows(cleanedImage):
    info = cleanedImage[1].split()
    height = info[1]
    return height


def createPpmFile(imageListData,width,height,maxColour,imgFormat):
    ppmList = []
    ppmList.append(imgFormat)
    ppmList.append(str(width) + ' ' + str(height))
    ppmList.append(maxColour)

    for n in imageListData:   #copy values of newly calculated image
        ppmList.append(n)


    f = open("newImage.ppm","w+")
    for n in ppmList:
        f.write(str(n))
        f.write("\n")

    f.close()


def createImage(format, width, height, max_value, data, name):
    newImage = []
    newImage.append(format)
    newImage.append(str(width)+" "+str(height))
    newImage.append(max_value)

    for n in data:
        newImage.append(n)

    save_File(newImage, name)

def save_File(file, name):
    with open(name, "w") as p:
        for n in file:
            p.write(str(n))
            p.write('\n')

def openFile(file):
    with open(file, 'r') as pbm:
        image = pbm.read()
    
    image = image.splitlines()

    for i in image:
        if i[0] == '#':
            image.remove(i)
    
    return image


def hideMessage(message, width, height):
    newImage = []
   
        
    
    messageLength = len(message)
    if (messageLength<10):
        newImage.append(0)
        newImage.append(0)
        newImage.append(messageLength)
    if (messageLength>10 and messageLength<100):
        newImage.append(0)
        for char in str(messageLength):
            newImage.append(int(char))

    for char in message:
        aValue = ord(char)
        if (aValue<100):
            newImage.append(0)
            for c in str(aValue):
                newImage.append(int(c))
        else:
            for c in str(aValue):
                newImage.append(int(c))

    format = 'P2'

    createImage(format,width,height, max(newImage),newImage, "hiding.pbm")


def revealMessage(cleanedImage):
    message = ""
    x = range(6,len(cleanedImage),3)
    for n in x:
        message = message + chr(int((cleanedImage[n])+(cleanedImage[n+1])+(cleanedImage[n+2])))
        
    print("Hidden message is: " + message)


def info(image):
    info = image[1].split()

    return image[0], info[0], info[1] , image[2]

def main():
    operation = input("Do you want to hide or reveal information? Type hide or reveal.")
    file = sys.argv[1]

    image = openFile(file)
    _, width, height, _ = info(image)

    if (operation == 'hide'):
        message = sys.argv[2]
        hideMessage(image, message, width, height)
    if (operation == 'reveal'):
        revealMessage(image)
              

if __name__ == "__main__":
    main()
