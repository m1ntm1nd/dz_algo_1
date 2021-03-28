import cv2

class Photo:
    def __init__(self, name):
        self._input_image = cv2.imread("imgs/{}.jpg".format(name))
        self._name = name
        print("imgs/{}.jpg".format(name))


    def show(self):
        cv2.imshow(self._name, self._input_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def draw_lines(self):
        width = self._input_image.shape[1]
        height = self._input_image.shape[0]
        self._input_image = cv2.line(self._input_image,(width//2,height),(width//2,0),(0,255,0),1)
        self._input_image = cv2.line(self._input_image,(0,height//3*2),(width,height//3*2),(0,255,0),1)
        self._input_image = cv2.line(self._input_image,(0,height//3),(width,height//3),(0,255,0),1)
        for x in range(width//2-1):
            for y in range(height-1,height//3*2-1,-1):
                r = self._input_image[y,x,0]  # узнаём значение красного цвета пикселя
                g = self._input_image[y,x,1]  # зелёного
                b = self._input_image[y,x,2]  # синего
                sr = (r + g + b) // 3  # среднее значение
                self._input_image[y,x] = (sr,sr,sr)
        

    