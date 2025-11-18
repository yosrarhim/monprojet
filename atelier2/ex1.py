import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger l'image
image_path = 'figure03_02.jpg'  
image = cv2.imread(image_path)

if image is None:
    print("Erreur : Impossible de charger l'image.")
    exit()

# Convertir en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#  Filtre Moyenneur 
mean_filter = cv2.blur(gray, (5, 5))  

# Filtre Médian 
median_filter = cv2.medianBlur(gray, 5)

# Filtre Pondéré (filtre Gaussien)

weighted_filter = cv2.GaussianBlur(gray, (5, 5), sigmaX=1)
#seuil
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# --- Affichage ---
titles = ['Originale', 'Filtre Moyenneur', 'Filtre Médian', 'Filtre Pondéré (Gaussien)', 'Seuil']
images = [gray, mean_filter, median_filter, weighted_filter, thresholded]

plt.figure(figsize=(15, 8))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
