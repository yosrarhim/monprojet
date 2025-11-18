import numpy as np
import cv2

def rvb_to_gris(img):
    h, l, c = img.shape
    gris = np.zeros((h, l), np.uint8)
    for i in range(h):
        for j in range(l):
            b, v, r = img[i, j]
            val = 0.3 * r + 0.59 * v + 0.11 * b
            gris[i, j] = val
    return gris

m = cv2.imread("image4.jpg")
print(m.shape)

cv2.imshow('image originale', m)
cv2.waitKey(0)

gris = rvb_to_gris(m)
cv2.imshow('image gris (fonction personnalisée)', gris)
cv2.waitKey(0)

gris2 = cv2.cvtColor(m, cv2.COLOR_BGR2GRAY)
cv2.imshow('image gris (cv2.cvtColor)', gris2)
cv2.waitKey(0)

cv2.destroyAllWindows()
