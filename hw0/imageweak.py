from PIL import Image
import sys
def image_wake(imagename):
    img = Image.open(imagename)
    img.show()
    w,h = img.size
    for i in range(w):
        for j in range(h):
            pixel = img.getpixel((i,j))
            img.putpixel((i,j),(pixel[0]/2,pixel[1]/2, pixel[2]/2))
    img.show()
    img.save("Q2.jpg")
if __name__== "__main__":
    image_wake(sys.argv[1])
    
    
