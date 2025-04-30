# import cv2
# import numpy as np
# import streamlit as st
# import matplotlib.pyplot as plt
# from PIL import Image
# import io

# # Fonction pour améliorer la netteté de l'image floue
# def restore_image(image_path):
#     # 1. Lire l'image
#     img = cv2.imread(image_path)
    
#     # Convertir l'image en niveaux de gris pour simplification
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # 2. Appliquer un filtre de défloutage
#     # Utilisation de la méthode de défloutage Wiener simple
#     kernel = np.ones((5, 5), np.float32) / 25  # Kernel simple pour appliquer un flou léger (peut être ajusté)
#     restored = cv2.filter2D(gray, -1, kernel)

#     # 3. Augmenter la netteté en utilisant un filtre de netteté (lissage puis enhancement)
#     # Appliquer un filtre unsharp (nettoyage)
#     sharp_kernel = np.array([[-1, -1, -1],
#                              [-1,  9, -1],
#                              [-1, -1, -1]])  # Un filtre de netteté simple
#     enhanced = cv2.filter2D(restored, -1, sharp_kernel)
    
#     return enhanced

# # Fonction pour afficher l'image de manière esthétique
# def display_image(image):
#     plt.figure(figsize=(8, 8))
#     plt.imshow(image, cmap="gray")
#     plt.axis('off')  # Enlever les axes pour une meilleure présentation
#     st.pyplot(plt)

# # Fonction pour télécharger l'image transformée
# def download_image(image):
#     # Convertir l'image numpy en format PIL pour la sauvegarder
#     image_pil = Image.fromarray(image)
    
#     # Sauvegarder l'image dans un buffer
#     img_byte_arr = io.BytesIO()
#     image_pil.save(img_byte_arr, format='PNG')
#     img_byte_arr = img_byte_arr.getvalue()
    
#     return img_byte_arr

# # Interface principale de Streamlit
# st.set_page_config(page_title="Restauration d'Image", page_icon="🔧", layout="centered")

# st.title("Restauration d'une Image Floue")
# st.markdown("Cette application vous permet de restaurer une image floue en améliorant sa netteté. Téléchargez simplement votre image floue et laissez-nous faire le reste!")

# # Téléchargement de l'image par l'utilisateur
# uploaded_file = st.file_uploader("Téléchargez une image floue", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Lire et afficher l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image Floue", use_column_width=True)

#     # Sauvegarder l'image téléchargée temporairement pour traitement
#     temp_image_path = "temp_image.jpg"
#     image.save(temp_image_path)

#     # Restaurer l'image pour améliorer la netteté
#     restored_image = restore_image(temp_image_path)

#     # Afficher l'image restaurée
#     st.subheader("Image Restaurée")
#     display_image(restored_image)

#     # Télécharger l'image restaurée
#     st.subheader("Téléchargez l'image restaurée")
#     img_byte_arr = download_image(restored_image)
#     st.download_button(label="Télécharger l'image restaurée", data=img_byte_arr, file_name="image_restaurée.png", mime="image/png")


import cv2
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import io

# Fonction pour améliorer la netteté d'une image ancienne et pixelisée
def restore_old_image(image_path):
    # 1. Lire l'image
    img = cv2.imread(image_path)

    # 2. Appliquer un filtre de réduction du bruit
    # On utilise un filtre bilateral pour réduire le bruit tout en préservant les bords
    img_bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 3. Appliquer un filtre de netteté (Unsharp Mask)
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])  # Un kernel pour améliorer la netteté
    img_sharp = cv2.filter2D(img_bilateral, -1, kernel)

    # 4. Améliorer la résolution de l'image (upsampling)
    # Utilisation d'une interpolation bicubique pour augmenter la taille de l'image
    height, width = img_sharp.shape[:2]
    new_dim = (width * 2, height * 2)
    img_upscaled = cv2.resize(img_sharp, new_dim, interpolation=cv2.INTER_CUBIC)

    return img_upscaled

# Fonction pour afficher l'image de manière esthétique
def display_image(image):
    plt.figure(figsize=(8, 8))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convertir BGR en RGB pour un affichage correct
    plt.axis('off')  # Enlever les axes pour une meilleure présentation
    st.pyplot(plt)

# Fonction pour télécharger l'image restaurée
def download_image(image):
    # Convertir l'image numpy en format PIL pour la sauvegarder
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # Sauvegarder l'image dans un buffer
    img_byte_arr = io.BytesIO()
    image_pil.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return img_byte_arr

# Interface principale de Streamlit
st.set_page_config(page_title="Restaurer une Image Ancienne", page_icon="🖼️", layout="centered")

st.title("Restaurer une Image Ancienne et Pixelisée")
st.markdown("""
Cette application permet de restaurer une image ancienne et de mauvaise qualité en l'améliorant. 
Téléchargez simplement votre image et laissez-nous la rendre plus nette et plus claire !""")

# Téléchargement de l'image par l'utilisateur
uploaded_file = st.file_uploader("Téléchargez une image ancienne et floue", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Lire et afficher l'image téléchargée
    image = Image.open(uploaded_file)
    st.image(image, caption="Image Originale", use_column_width=True)

    # Sauvegarder l'image téléchargée temporairement pour traitement
    temp_image_path = "temp_image.jpg"
    image.save(temp_image_path)

    # Restaurer l'image pour améliorer la netteté
    restored_image = restore_old_image(temp_image_path)

    # Afficher l'image restaurée
    st.subheader("Image Restaurée")
    display_image(restored_image)

    # Télécharger l'image restaurée
    st.subheader("Téléchargez l'image restaurée")
    img_byte_arr = download_image(restored_image)
    st.download_button(label="Télécharger l'image restaurée", data=img_byte_arr, file_name="image_restaurée.png", mime="image/png")
