#5.3 :
import cv2
import numpy as np

# Charger l'image
image = cv2.imread('image.jpg')  
if image is None:
    print("Erreur : image non trouvée.")
    exit()

# Convertir l'image de BGR à HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Définir les plages de couleur bleue
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])

# Créer un masque pour la couleur bleue
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Trouver les contours
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner les contours trouvés sur l'image
cv2.drawContours(image, contours, -1, (255, 0, 0), 2)  # Couleur bleue, épaisseur 2

# Afficher l'image finale
cv2.imshow('Contours Bleus', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
