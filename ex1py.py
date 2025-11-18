import cv2
import numpy as np

def lectureImage():
    image01=cv2.imread("image1.jpg")
    image02=cv2.imread("image2.jpg")
    image03=cv2.imread("image3.jpg")
    image04=cv2.imread("image4.jpg")
    image05=cv2.imread("image5.jpg")
    return image01,image02, image03, image04, image05


def afficheImage(image01, image02, image03, image04,image05):
    cv2.imshow ("image image 01", image01)
    cv2.imshow ("image image 02", image02)
    cv2.imshow ("image image 02", image03)
    cv2.imshow ("image image 04", image04)
    cv2.imshow ("image image 05", image05)
    cv2.waitKey (0)
    cv2.destroyAllWindows ()


image01,image02, image03, image04, image05 =lectureImage()
afficheImage(image01, image02, image03, image04,image05)