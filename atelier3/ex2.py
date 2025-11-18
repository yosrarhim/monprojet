#5.4 :
import cv2
import numpy as np
import time

# Ouvre la caméra
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

# Démarrer un chrono pour calculer le FPS
prev_time = time.time()

while True:
    # Capture image par image
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la capture de l'image")
        break

    # Redimensionner l'image pour accélérer le traitement
    frame = cv2.resize(frame, (640, 480))

    # Conversion en HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Définir les plages pour la couleur rouge
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combiner les deux masques
    mask = mask1 + mask2

    # Nettoyage du masque
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Trouver les contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner les vrais contours détectés
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Ignorer les petits objets
            # Dessiner le contour directement
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

            # Optionnel : afficher du texte au centre du contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(frame, "Rouge detecte", (cx - 50, cy - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Calcul FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Afficher FPS sur l'image
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Afficher les résultats
    cv2.imshow('Detection Couleur Rouge', frame)
    cv2.imshow('Masque Rouge', mask)

    # Quitter en appuyant sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer toutes les fenêtres
cap.release()
cv2.destroyAllWindows()