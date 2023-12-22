def rotation(px, x0, y0, t):
   
 
    return(px)
 
# Programme principal


from PIL import Image # Sous Thonny : installer la biblio Pillow !

imageDebut = Image.open("maison.png")
imageDebut.show()

taille = imageDebut.size[0] # Récupération de la dimension de l'image (carrée ...)
print("Taille : ", taille)
matrice = imageDebut.load()# Récupération des pixels en codage rvb
print(matrice[7,4]) # Vérification pour un pixel.

rotation(matrice, 0, 0, taille)

imageDebut.save("maisonRota.png")