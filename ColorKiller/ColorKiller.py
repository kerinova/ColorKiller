import PIL
import Image
import _imaging

def main():
    inPath = raw_input("Enter the input image file path: ")
    image = Image.open(inPath)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    changeColor(image, outPath)

def changeColor(image, inPath):
    pixels = image.load()
    for row in range(image.size[0]):
        for col in range(image.size[1]):
            if pixels[row, col] != (255, 255, 255, 255): #if not total white
                pixels[row, col] = (0, 0, 0, 0) #change to transparent
    print "Hello"
    image.save(inPath + "trans.png")

if  __name__ =='__main__':
    main()