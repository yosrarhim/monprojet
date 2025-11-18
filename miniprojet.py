import cv2

# 1. Initialiser la capture vidéo (0 = première caméra détectée)
cap = cv2.VideoCapture(0)

# 2. Vérifier si la caméra est bien ouverte
if not cap.isOpened():
    print("Erreur : Impossible d'accéder à la caméra.")
    exit()

# 3. Boucle de capture
while True:
    # Lire une image depuis la caméra
    ret, frame = cap.read()

    # Vérifier que la capture a réussi
    if not ret:
        print("Erreur : Impossible de lire l'image.")
        break

    # Afficher l’image capturée dans une fenêtre
    cv2.imshow("Flux vidéo - Appuyez sur 'q' pour quitter", frame)

    # Sortir de la boucle si 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. Libérer les ressources
cap.release()
cv2.destroyAllWindows()
