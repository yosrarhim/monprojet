import cv2
import numpy as np

# Charger l'image
image_path = 'image1.jpg'  # Remplacer par le chemin de ton image
image = cv2.imread(image_path)

if image is None:
    print("Erreur : Impossible de charger l'image.")
    exit()

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

epsilon = 0.005
sigma_cible = 70  

# Calcul de la moyenne et de l'écart-type
mean = np.mean(gray)
std_dev = np.std(gray)

print(f"Moyenne originale : {mean:.2f}")
print(f"Écart-type original : {std_dev:.2f}")

# Application de la formule d'ajustement
adjusted = (gray - mean) / (std_dev + epsilon) * sigma_cible + mean
adjusted = np.clip(adjusted, 0, 255).astype(np.uint8)
cv2.imshow('Image Originale', gray)
cv2.imshow('Image Ajustée', adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
