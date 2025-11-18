import cv2
import numpy as np

# Charger l'image
image = cv2.imread('$imagerouge.jpg')

if image is None:
    print("Image introuvable !")
    exit()

# Convertir en HSV pour détecter la couleur rouge plus facilement
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Définir une plage de rouge
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Créer un masque pour les pixels rouges
mask = cv2.inRange(hsv, lower_red, upper_red)

# Appliquer le remplacement : où c'est rouge → vert
image[mask > 0] = [0, 255, 0]

# Affichage
cv2.imshow("Image modifiée", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
