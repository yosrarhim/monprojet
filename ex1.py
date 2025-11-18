from PIL import Image, ImageDraw

# Paramètres de la grille
rows, cols = 3, 2
cell_width = 200
cell_height = 150

# Taille de l’image finale
grid_width = cols * cell_width
grid_height = rows * cell_height
final_image = Image.new("RGB", (grid_width, grid_height), (255, 255, 255))

# Dessin des rectangles de la grille
draw = ImageDraw.Draw(final_image)
for row in range(rows):
    for col in range(cols):
        x0 = col * cell_width
        y0 = row * cell_height
        x1 = x0 + cell_width
        y1 = y0 + cell_height
        draw.rectangle([x0, y0, x1, y1], outline="black", width=2)

# Charger et redimensionner les images
images = []
for i in range(1, 6):
    img = Image.open(f"image{i}.jpg").resize((cell_width, cell_height))
    images.append(img)

# Coller les images dans les cellules
final_image.paste(images[0], (0, 0))                     
final_image.paste(images[1], (cell_width, 0))           
final_image.paste(images[2], (0, cell_height))              
final_image.paste(images[3], (cell_width, cell_height))     
final_image.paste(images[4], (cell_width // 2, 2 * cell_height)) 
# Affichage de l’image finale
final_image.show()
