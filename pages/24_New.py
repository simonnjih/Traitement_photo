import streamlit as st
from PIL import Image

def ajouter_accessoire(image_pil, accessoire_pil, position):
    """Ajoute un accessoire (chapeau ou lunettes) à une image PIL."""
    image_largeur, image_hauteur = image_pil.size
    accessoire_largeur, accessoire_hauteur = accessoire_pil.size

    # Redimensionner l'accessoire proportionnellement à la largeur de l'image
    nouvelle_largeur = int(image_largeur * 0.4)  # Ajuster le facteur selon la taille souhaitée
    ratio = nouvelle_largeur / accessoire_largeur
    nouvelle_hauteur = int(accessoire_hauteur * ratio)
    accessoire_redimensionne = accessoire_pil.resize((nouvelle_largeur, nouvelle_hauteur))

    acc_largeur_redim, acc_hauteur_redim = accessoire_redimensionne.size

    if position == "chapeau":
        # Positionner le chapeau en haut du visage (estimation)
        x = (image_largeur - acc_largeur_redim) // 2
        y = int(image_hauteur * 0.1) - acc_hauteur_redim // 2 # Ajuster la position verticale
    elif position == "lunettes":
        # Positionner les lunettes au centre du visage (estimation)
        x = (image_largeur - acc_largeur_redim) // 2
        y = int(image_hauteur * 0.4) # Ajuster la position verticale

    # Assurer que l'accessoire reste dans les limites de l'image
    x = max(0, min(x, image_largeur - acc_largeur_redim))
    y = max(0, min(y, image_hauteur - acc_hauteur_redim))

    # Créer une nouvelle image pour la fusion si l'image de base n'est pas en RGBA
    if image_pil.mode != 'RGBA':
        image_pil = image_pil.convert("RGBA")
    # Créer un masque pour gérer la transparence de l'accessoire
    masque = accessoire_redimensionne.split()[3] if accessoire_redimensionne.mode == 'RGBA' else None

    # Ajouter l'accessoire à l'image
    image_pil.paste(accessoire_redimensionne, (x, y), masque)
    return image_pil

def main():
    st.title("Ajouter un chapeau ou des lunettes de soleil")

    uploaded_file = st.file_uploader("Téléchargez une photo", type=["jpg", "jpeg", "png"])

    accessoire_choisi = st.selectbox("Choisissez un accessoire", ["Chapeau", "Lunettes de soleil"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Image téléchargée", use_column_width=True)

        if accessoire_choisi == "Chapeau":
            try:
                chapeau = Image.open("download.jpg").convert("RGBA")  # Assurez-vous que ce fichier existe
                image_avec_accessoire = ajouter_accessoire(image, chapeau, "chapeau")
                st.image(image_avec_accessoire, caption="Avec chapeau", use_column_width=True)
            except FileNotFoundError:
                st.error("Le fichier chapeau.png est introuvable. Veuillez le placer dans le même répertoire que le script.")
        elif accessoire_choisi == "Lunettes de soleil":
            try:
                lunettes = Image.open("lunettes_soleil.png").convert("RGBA")  # Assurez-vous que ce fichier existe
                image_avec_accessoire = ajouter_accessoire(image, lunettes, "lunettes")
                st.image(image_avec_accessoire, caption="Avec lunettes de soleil", use_column_width=True)
            except FileNotFoundError:
                st.error("Le fichier lunettes_soleil.png est introuvable. Veuillez le placer dans le même répertoire que le script.")

if __name__ == "__main__":
    main()
