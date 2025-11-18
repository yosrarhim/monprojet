#import numpy as np 
#import cv2
 # creer un image vide et noire 
#img= np.zeros((400,300,3), np.uint8)
# remplir toute l'image avec la couleur rouge 
#img[:,:]=(0,0,255)
#cv2.imshow('red image' , img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
import numpy as np
import cv2
# Crée une image noire de 100x100
img = np.zeros((100, 100, 3), dtype=np.uint8)

# Modifie le pixel à la position (10, 20) → pixel rouge
img[10, 20] = [0, 0, 255]

# Lire ce pixel
print(img[10, 20])  # Affiche [  0   0 255]
cv2.imshow('red image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()