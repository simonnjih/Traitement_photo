# import cv2
# import numpy as np
# import streamlit as st
# import matplotlib.pyplot as plt
# from PIL import Image
# import io

# # Fonction pour transformer l'image en dessin animé avec effet 3D
# def cartoonize_image(image_path):
#     # 1. Lire l'image
#     img = cv2.imread(image_path)
    
#     # Convertir l'image en couleur RGB pour l'affichage
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     # 2. Lissage de l'image
#     img_bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    
#     # 3. Détection des bords avec Canny
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=9)

#     # 4. Fusionner les bords avec l'image lissée
#     cartoon = cv2.bitwise_and(img_bilateral, img_bilateral, mask=edges)

#     # 5. Créer un effet 3D basique (simuler la profondeur)
#     gradient = cv2.cvtColor(cartoon, cv2.COLOR_BGR2GRAY)
#     gradient = cv2.GaussianBlur(gradient, (5, 5), 0)
#     gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX)

#     # Ajouter le gradient pour donner un effet 3D
#     cartoon_3d = cv2.addWeighted(cartoon, 0.8, cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR), 0.2, 0)

#     return cartoon_3d

# # Fonction pour afficher l'image sous forme de galerie
# def display_image(image):
#     plt.figure(figsize=(8, 8))
#     plt.imshow(image)
#     plt.axis('off')  # Enlever les axes pour un affichage plus esthétique
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
# st.set_page_config(page_title="Transformation en Dessin Animé 3D", page_icon="🎨", layout="centered")

# st.title("Transformation d'une Photo en Dessin Animé 3D")
# st.markdown("Bienvenue dans l'application de transformation d'image en dessin animé avec un effet 3D. Téléchargez votre photo et découvrez l'effet magique !")

# # Téléchargement de l'image par l'utilisateur
# uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Lire et afficher l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image originale", use_column_width=True)

#     # Sauvegarder l'image téléchargée temporairement pour traitement
#     temp_image_path = "temp_image.jpg"
#     image.save(temp_image_path)

#     # Transformer l'image en dessin animé 3D
#     transformed_image = cartoonize_image(temp_image_path)

#     # Afficher l'image transformée
#     st.subheader("Image Transformée en Dessin Animé 3D")
#     display_image(transformed_image)

#     # Télécharger l'image transformée
#     st.subheader("Téléchargez l'image transformée")
#     img_byte_arr = download_image(transformed_image)
#     st.download_button(label="Télécharger l'image", data=img_byte_arr, file_name="dessin_animé_3d.png", mime="image/png")

import cv2
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import io

# 📐 CONFIGURATION PAGE (à mettre tout en haut)
st.set_page_config(
    page_title="Studio Émotionnel 3D 🎨",
    page_icon="🖼️",
    layout="centered",
)
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

# 💅 STYLE ÉMOTIONNEL EN CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f1f0;
        font-family: 'Segoe UI', sans-serif;
        color: #3b2e2e;
    }
    h1 {
        text-align: center;
        font-size: 3em;
        color: #7f4a88;
        margin-bottom: 0.3em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #5e4b5c;
        margin-bottom: 2em;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        background-color: #7f4a88;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.6em 1.2em;
    }
    .stButton>button:hover {
        background-color: #a65fc1;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# 🎨 HEADER
st.markdown("<h1>✨ Studio Émotionnel 3D</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transformez vos photos en œuvres d’art dessin animé avec profondeur et poésie. 🎭🖌️</div>', unsafe_allow_html=True)

# 🔄 FONCTIONS DE TRAITEMENT

def cartoonize_image(image):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    cartoon = cv2.bitwise_and(img_bilateral, img_bilateral, mask=edges)

    # 🌌 Effet 3D simulé par dégradé
    gradient = cv2.cvtColor(cartoon, cv2.COLOR_BGR2GRAY)
    gradient = cv2.GaussianBlur(gradient, (5, 5), 0)
    gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX)
    cartoon_3d = cv2.addWeighted(cartoon, 0.85, cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR), 0.15, 0)

    cartoon_3d = cv2.cvtColor(cartoon_3d, cv2.COLOR_BGR2RGB)
    return cartoon_3d

def download_image(image):
    image_pil = Image.fromarray(image)
    buf = io.BytesIO()
    image_pil.save(buf, format="PNG")
    return buf.getvalue()

# 📥 UPLOADER
uploaded_file = st.file_uploader("📸 Choisissez une image (JPEG ou PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Votre photo originale", use_column_width=True)

    # 🚀 Traitement
    with st.spinner("✨ Transformation magique en cours..."):
        cartoon_img = cartoonize_image(image)

    st.subheader("🎆 Résultat : Dessin Animé Émotionnel 3D")
    st.image(cartoon_img, use_column_width=True)

    # 📥 Téléchargement
    img_data = download_image(cartoon_img)
    st.download_button(
        label="📥 Télécharger votre œuvre",
        data=img_data,
        file_name="emotion_cartoon_3d.png",
        mime="image/png"
    )

    st.markdown("> *Chaque cliché cache une âme. Laissez-la s’exprimer en couleurs et relief.* 🌌")
else:
    st.info("🖼️ Importez une image pour commencer l'expérience artistique.")
