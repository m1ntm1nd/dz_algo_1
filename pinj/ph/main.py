#написать в стиле ооп, в мейне ноль деклараций
#ТЗ:
#считать картинку
#манипуляции
#ресайз
import sys
from photos import *

def main():
    photo = Photo("frog")
    photo.draw_lines()
    photo.show()


if __name__ == "__main__":
    sys.exit(main() or 0) #how does it work?

