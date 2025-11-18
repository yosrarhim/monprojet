import cv2
import numpy as np

def lectureImage():
    image01 = cv2.imread("mer01.jpg")
    image02 = cv2.imread("mer02.jpg")
    image03 = cv2.imread("mer03.jpg")
    image04 = cv2.imread("mer04.jpg")
    image05 = cv2.imread("mer05.jpg")
    return image01, image02, image03, image04, image05

def ajouter_bordure(img, taille_bordure=10):
    return cv2.copyMakeBorder(img, taille_bordure, taille_bordure, taille_bordure, taille_bordure, cv2.BORDER_CONSTANT, value=[255, 255, 255])

def rotation_image(img, angle):
    (h, w) = img.shape[:2]
    centre = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(centre, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), borderValue=(255, 255, 255))
    return rotated

def creer_collage(image01, image02, image03, image04, image05):
    # Redimensionner les images
    taille_image = (300, 300)
    images = [
        cv2.resize(image01, taille_image),
        cv2.resize(image02, taille_image),
        cv2.resize(image03, taille_image),
        cv2.resize(image04, taille_image),
        cv2.resize(image05, taille_image)
    ]

    # Appliquer bordure et rotation
    angles = [-5, 5, -10, 7, -3]
    images_modifiees = []
    for img, angle in zip(images, angles):
        img_bordure = ajouter_bordure(img)
        img_rotate = rotation_image(img_bordure, angle)
        images_modifiees.append(img_rotate)

    # Créer un fond blanc
    fond_largeur = 922
    fond_hauteur = 1220
    fond = np.ones((fond_hauteur, fond_largeur, 3), dtype=np.uint8) * 255

    # Positions dynamiques
    w, h = fond_largeur, fond_hauteur
    positionsI1 = [ (0, 0),(w // 2, 0),(0, h // 3),(w // 2, h // 3),(w // 4, 2 * h // 3)]
    positionsI2 = [(w // 3, 0),(w * 2 // 3, 0),(w // 3, h // 3),(w * 2 // 3, h // 3),(w // 2, 2 * h // 3)]
    positionsI3 = [(w // 4, 0),(w * 3 // 4, 0),(w // 4, h // 2),(w * 3 // 4, h // 2),(w // 2, h // 4)]
    # Coller les images
for img, (x, y) in zip(images_modifiees, positions):
        h_img, w_img = img.shape[:2]
        roi = fond[y:y+h_img, x:x+w_img]
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(img_gray, 250, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        fond_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        img_fg = cv2.bitwise_and(img, img, mask=mask)
        dst = cv2.add(fond_bg, img_fg)
        fond[y:y+h_img, x:x+w_img] = dst
# Main program
image01, image02, image03, image04, image05 = lectureImage()
resultat = creer_collage(image01, image02, image03, image04, image05)

cv2.imshow("Collage Final", resultat)
cv2.waitKey(0)
cv2.destroyAllWindows()
