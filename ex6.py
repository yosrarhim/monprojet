import numpy as np
import cv2
image = cv2.imread("classeg.jpg")
logo = cv2.imread("logo1.jpg")
image = cv2.resize(image, (800, 600))
max_logo_width = int(image.shape[1] * 0.1)
max_logo_height = int(image.shape[0] * 0.1)
logo = cv2.resize(logo, (max_logo_width, max_logo_height))
roi = image[0:max_logo_height, 0:max_logo_width]
if logo.shape[2] == 3:
    image[0:max_logo_height, 0:max_logo_width] = logo
else:
    b, g, r, a = cv2.split(logo)
    mask = cv2.merge((a, a, a))
    logo_rgb = cv2.merge((b, g, r))
    roi = cv2.bitwise_and(roi, 255 - mask)
    logo_masked = cv2.bitwise_and(logo_rgb, mask)
    image[0:max_logo_height, 0:max_logo_width] = cv2.add(roi, logo_masked)
cv2.imshow("Image avec logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
