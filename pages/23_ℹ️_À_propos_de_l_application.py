#import streamlit as st

import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

st.balloons()
st.title("Appliquez un filtre à votre image")

# Télécharger une image
uploaded_image = st.file_uploader("Téléchargez une image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Ouvrir l'image téléchargée
    image = Image.open(uploaded_image)

    # Afficher l'image originale
    st.image(image, caption="Image originale")

    # Choisir un filtre
    filter_option = st.selectbox("Choisissez un filtre", ["Aucun", "Noir et blanc", "Augmenter la couleur", "Flou"])
    progress_bar = st.sidebar.progress(10)
    if filter_option == "Noir et blanc":
        image = image.convert("L")
    elif filter_option == "Augmenter la couleur":
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(2.0)  # Augmenter la couleur
    elif filter_option == "Flou":
        image = image.filter(ImageFilter.GaussianBlur(5))

    # Afficher l'image modifiée
    st.image(image, caption="Image avec filtre appliqué")
