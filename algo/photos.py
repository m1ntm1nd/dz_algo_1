import cv2
import random

class Photo():
    def __init__(self, name):
        self._input_image = cv2.imread("imgs/{}.jpg".format(name))
        self._name = name
        print("imgs/{}.jpg".format(name))


    def show(self):
        cv2.imshow(self._name, self._input_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def draw_lines(self):
        factor = int(input('factor:')) 
        height = self._input_image.shape[0]
        width = self._input_image.shape[1] 
        for x in range(width):
            #for y in range(height-1,height//3*2-1,-1):
            for y in range(height):
                b = self._input_image[y,x,0]
                g = self._input_image[y,x,1]
                r = self._input_image[y,x,2]
                middle = (r + g + b) // 3
                if x < width//2 and y < height//3:
                    self._input_image[y,x] = (middle,middle,middle) #greyscale
                elif x > width//2 and y < height//3:
                    k = 20
                    self._input_image[y,x] = (middle,middle+k,middle+2*k) #sepia
                elif x < width//2 and (y > height//3 and y < height//3*2):
                    self._input_image[y,x] = (255-b,255-g,255-r) #negative
                elif x > width//2 and (y > height//3 and y < height//3*2):
                    rand = random.randint(-factor, factor)
                    self._input_image[y,x] = (b+rand,g+rand,r+rand) #noises
                elif x < width//2 and (y > height//3*2):
                    self._input_image[y,x] = (b+factor,g+factor,r+factor) #brightness
                elif x > width//2 and (y > height//3*2):
                    summ = b+g+r
                    if (summ) > 100:  #black/white
                        self._input_image[y,x] = (255-middle,255-middle,255-middle)
                    else:
                        self._input_image[y,x] = (middle,middle,middle)
        self._input_image = cv2.line(self._input_image,(width//2,height),(width//2,0),(0,255,0),1)
        self._input_image = cv2.line(self._input_image,(0,height//3*2),(width,height//3*2),(0,255,0),1)
        self._input_image = cv2.line(self._input_image,(0,height//3),(width,height//3),(0,255,0),1)
        cv2.imwrite('imgs/{}_out.jpg'.format(self._name),self._input_image)
    