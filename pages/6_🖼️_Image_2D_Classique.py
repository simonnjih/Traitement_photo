# import cv2
# import numpy as np
# import streamlit as st
# import matplotlib.pyplot as plt
# from PIL import Image
# import io

# # Fonction pour transformer l'image en un dessin 2D
# def sketch_image(image_path):
#     # 1. Lire l'image
#     img = cv2.imread(image_path)
    
#     # Convertir en niveaux de gris
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # 2. Inverser l'image en niveaux de gris
#     inverted_gray = 255 - gray

#     # 3. Appliquer un flou gaussien
#     blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

#     # 4. Inverser l'image floutée
#     inverted_blurred = 255 - blurred

#     # 5. Créer le croquis final
#     sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

#     return sketch

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
# st.set_page_config(page_title="Transformation en Dessin 2D", page_icon="🖼️", layout="centered")

# st.title("Transformation de Photo en Dessin 2D")
# st.markdown("Découvrez la magie de la transformation d'une photo en un dessin à main levée ! Téléchargez votre image et laissez la magie opérer.")

# # Téléchargement de l'image par l'utilisateur
# uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Lire et afficher l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image originale", use_column_width=True)

#     # Sauvegarder l'image téléchargée temporairement pour traitement
#     temp_image_path = "temp_image.jpg"
#     image.save(temp_image_path)

#     # Transformer l'image en dessin 2D
#     transformed_image = sketch_image(temp_image_path)

#     # Afficher l'image transformée
#     st.subheader("Votre Image Transformée en Dessin 2D")
#     display_image(transformed_image)

#     # Télécharger l'image transformée
#     st.subheader("Téléchargez votre dessin 2D")
#     img_byte_arr = download_image(transformed_image)
#     st.download_button(label="Télécharger le dessin", data=img_byte_arr, file_name="dessin_2d.png", mime="image/png")

import cv2
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import io

# --- Configuration de la page Streamlit ---
st.set_page_config(page_title="Transformation en Dessin 2D", page_icon="🖼️", layout="centered")



st.markdown("""
    <style>
    /* Personnalisation de la barre latérale */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f3e5f5, #e1f5fe);
        color: #333;
        padding: 2rem 1rem;
        font-family: 'Segoe UI', sans-serif;
    }

    [data-testid="stSidebar"]::before {
        content: "🌌 Naviguez dans l’univers visuel";
        display: block;
        font-size: 1.3em;
        font-weight: bold;
        color: #4a148c;
        margin-bottom: 1em;
        text-align: center;
    }

    [data-testid="stSidebarNav"] ul {
        padding-left: 0;
    }

    [data-testid="stSidebarNav"] li {
        font-size: 1.1em;
        margin-bottom: 10px;
    }

    [data-testid="stSidebarNav"] li:hover {
        background-color: #f8bbd0;
        border-radius: 10px;
        transition: 0.3s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# Fonction pour transformer l'image en un dessin 2D
def sketch_image(image_path):
    # 1. Lire l'image
    img = cv2.imread(image_path)
    
    # Convertir en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Inverser l'image en niveaux de gris
    inverted_gray = 255 - gray

    # 3. Appliquer un flou gaussien
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

    # 4. Inverser l'image floutée
    inverted_blurred = 255 - blurred

    # 5. Créer le croquis final
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

    return sketch

# Fonction pour afficher l'image de manière esthétique
def display_image(image):
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap="gray")
    plt.axis('off')  # Enlever les axes pour une meilleure présentation
    st.pyplot(plt)

# Fonction pour télécharger l'image transformée
def download_image(image):
    # Convertir l'image numpy en format PIL pour la sauvegarder
    image_pil = Image.fromarray(image)
    
    # Sauvegarder l'image dans un buffer
    img_byte_arr = io.BytesIO()
    image_pil.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return img_byte_arr

# --- CSS et style de la page ---
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;  /* Couleur de fond douce et apaisante */
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }

        h1 {
            color: #3B82F6;  /* Bleu vibrant pour le titre */
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            margin-top: 50px;
        }

        h2 {
            color: #1F2937;  /* Gris foncé pour les sous-titres */
            font-size: 28px;
            text-align: center;
            font-weight: 600;
            margin-top: 30px;
        }

        p {
            font-size: 18px;
            text-align: center;
            color: #4B5563;
            margin-top: 10px;
            line-height: 1.6;
        }

        .button {
            display: block;
            width: 200px;
            margin: 40px auto;
            padding: 12px 0;
            text-align: center;
            background-color: #3B82F6;
            color: white;
            font-size: 18px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s;
        }

        .button:hover {
            background-color: #2563EB;
            transform: scale(1.05);
        }

        .uploaded-image {
            display: block;
            margin: 20px auto;
            width: 80%;
            max-width: 600px;
        }

        .img-container {
            text-align: center;
            margin-top: 30px;
        }

        /* Animation de fade-in pour l'apparition de l'image transformée */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .fade-in {
            animation: fadeIn 1s ease-in;
        }

    </style>
""", unsafe_allow_html=True)

# Interface principale de Streamlit
st.title("✨ Transformation de Photo en Dessin 2D ✨")
st.markdown("Découvrez la magie de transformer une photo en un dessin à main levée. Téléchargez votre image et laissez la magie opérer!")

# Téléchargement de l'image par l'utilisateur
uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Lire et afficher l'image téléchargée
    image = Image.open(uploaded_file)
    st.image(image, caption="Image originale")

    # Sauvegarder l'image téléchargée temporairement pour traitement
    temp_image_path = "temp_image.jpg"
    image.save(temp_image_path)

    # Transformer l'image en dessin 2D
    transformed_image = sketch_image(temp_image_path)

    # Afficher l'image transformée avec une animation fade-in
    st.subheader("🎨 Votre Image Transformée en Dessin 2D")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    display_image(transformed_image)
    st.markdown('</div>', unsafe_allow_html=True)

    # Télécharger l'image transformée
    st.subheader("💾 Téléchargez votre dessin 2D")
    img_byte_arr = download_image(transformed_image)
    st.download_button(label="Télécharger le dessin", data=img_byte_arr, file_name="dessin_2d.png", mime="image/png", key="download_button", use_container_width=True)
    
    # Bouton de retour
    st.markdown('<a href="javascript:window.history.back()" class="button">Retour</a>', unsafe_allow_html=True)

