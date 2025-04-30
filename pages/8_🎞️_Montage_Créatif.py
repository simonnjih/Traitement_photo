# import cv2
# import numpy as np
# import streamlit as st
# from PIL import Image
# import io

# # Fonction pour redimensionner les images à une taille donnée
# def resize_image(image, width, height):
#     return cv2.resize(image, (width, height))

# # Fonction pour créer un montage
# def create_collage(images, positions, rows, cols, img_width, img_height):
#     # Créer une image vide qui servira de fond pour le collage
#     collage = np.zeros((img_height * rows, img_width * cols, 3), dtype=np.uint8)
    
#     # Placer chaque image dans la grille en fonction des positions choisies
#     for i, img in enumerate(images):
#         row, col = positions[i]
#         collage[row * img_height: (row + 1) * img_height, col * img_width: (col + 1) * img_width] = img

#     return collage

# # Titre de l'application Streamlit
# st.title('Création de Montage Photo avec OpenCV')

# # Téléchargement des images
# uploaded_files = st.file_uploader("Téléchargez plusieurs images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# # Si des fichiers ont été téléchargés
# if uploaded_files:
#     images = []
#     positions = []
    
#     # Charger toutes les images téléchargées
#     for uploaded_file in uploaded_files:
#         # Charger l'image avec Pillow
#         image = Image.open(uploaded_file)
        
#         # Convertir l'image en RGB (conserver les couleurs d'origine)
#         image = image.convert("RGB")
        
#         # Convertir l'image en tableau NumPy pour OpenCV
#         image = np.array(image)
        
#         images.append(image)

#     # Demander à l'utilisateur combien de lignes et de colonnes pour le montage
#     rows = st.slider("Nombre de lignes", 1, 5, 2)
#     cols = st.slider("Nombre de colonnes", 1, 5, 2)
    
#     # S'assurer que nous avons suffisamment d'images
#     if len(images) < rows * cols:
#         st.warning(f"Veuillez télécharger au moins {rows * cols} images pour remplir la grille.")
#     else:
#         # Obtenir les dimensions de la première image pour définir la taille des cases dans la grille
#         img_height, img_width, _ = images[0].shape
        
#         # Redimensionner toutes les images à la taille de la grille
#         resized_images = [resize_image(img, img_width, img_height) for img in images]
        
#         # Demander à l'utilisateur de choisir la position de chaque image
#         for i in range(len(images)):
#             st.subheader(f"Choisir la position pour l'image {i + 1}")
#             row = st.number_input(f"Position de la ligne pour l'image {i + 1}", min_value=0, max_value=rows-1, value=i//cols)
#             col = st.number_input(f"Position de la colonne pour l'image {i + 1}", min_value=0, max_value=cols-1, value=i%cols)
#             positions.append((row, col))
        
#         # Créer le collage
#         collage = create_collage(resized_images, positions, rows, cols, img_width, img_height)
        
#         # Convertir l'image de collage en format PIL pour l'afficher
#         collage_pil = Image.fromarray(cv2.cvtColor(collage, cv2.COLOR_BGR2RGB))
#         st.image(collage_pil, caption="Montage final", use_column_width=True)

#         # Sauvegarder l'image finale
#         st.sidebar.subheader("Télécharger l'image modifiée")
#         save_button = st.sidebar.button("Télécharger l'image modifiée")
        
#         if save_button:
#             # Convertir l'image modifiée en fichier pour téléchargement
#             img_byte_arr = io.BytesIO()
#             collage_pil.save(img_byte_arr, format='PNG')
#             img_byte_arr = img_byte_arr.getvalue()

#             st.download_button(
#                 label="Télécharger l'image modifiée",
#                 data=img_byte_arr,
#                 file_name="montage_image.png",
#                 mime="image/png"
#             )

import cv2
import numpy as np
import streamlit as st
from PIL import Image
import io

# Configuration de page
st.set_page_config(page_title="🧠✨ Collage Creator", layout="wide")
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

# 🎨 Style HTML et CSS haut de gamme
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f9f9f9, #e0ecf3);
    }
    .header {
        font-size: 3.5em;
        color: #2c3e50;
        font-weight: 800;
        text-align: center;
        padding: 20px;
        margin-bottom: 0;
    }
    .subtext {
        text-align: center;
        font-size: 1.3em;
        color: #34495e;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-style: italic;
        color: #7f8c8d;
    }
    .highlight {
        background-color: #2c3e50;
        color: white;
        padding: 12px 25px;
        border-radius: 12px;
        font-size: 1.1em;
        margin-top: 20px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 💫 Titre émotionnel et inspirant
st.markdown('<div class="header">✨ Assemble tes souvenirs</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Chaque image est une mémoire. Chaque montage est une œuvre.</div>', unsafe_allow_html=True)

# 📤 Upload d'images
uploaded_files = st.file_uploader("Téléchargez plusieurs images pour créer votre montage visuel", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def create_collage(images, positions, rows, cols, img_width, img_height):
    collage = np.zeros((img_height * rows, img_width * cols, 3), dtype=np.uint8)
    for i, img in enumerate(images):
        row, col = positions[i]
        collage[row * img_height: (row + 1) * img_height, col * img_width: (col + 1) * img_width] = img
    return collage

if uploaded_files:
    images = []
    positions = []

    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file).convert("RGB")
        image = np.array(image)
        images.append(image)

    rows = st.slider("Nombre de lignes", 1, 5, 2)
    cols = st.slider("Nombre de colonnes", 1, 5, 2)

    if len(images) < rows * cols:
        st.warning(f"⚠️ Il faut au moins {rows * cols} images pour compléter le collage.")
    else:
        img_height, img_width, _ = images[0].shape
        resized_images = [resize_image(img, img_width, img_height) for img in images]

        st.markdown("### 📍 Choix des positions de chaque image")
        for i in range(rows * cols):
            with st.expander(f"📌 Image {i+1}"):
                row = st.number_input(f"Ligne pour l'image {i + 1}", min_value=0, max_value=rows - 1, value=i // cols, key=f"row_{i}")
                col = st.number_input(f"Colonne pour l'image {i + 1}", min_value=0, max_value=cols - 1, value=i % cols, key=f"col_{i}")
                positions.append((row, col))

        collage = create_collage(resized_images, positions, rows, cols, img_width, img_height)
        collage_pil = Image.fromarray(cv2.cvtColor(collage, cv2.COLOR_BGR2RGB))

        st.markdown("### 🖼️ Montage Final")
        st.image(collage_pil, use_column_width=True, caption="✨ Votre œuvre, votre héritage visuel.")

        st.markdown('<div class="highlight">Téléchargez votre création</div>', unsafe_allow_html=True)

        img_byte_arr = io.BytesIO()
        collage_pil.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        st.download_button(
            label="📥 Télécharger l'image finale",
            data=img_byte_arr,
            file_name="montage_image.png",
            mime="image/png"
        )

        st.markdown('<div class="footer">Fait avec ❤️ par un passionné de science, de vision et d’âme.</div>', unsafe_allow_html=True)
else:
    st.info("🎯 Pour commencer, veuillez télécharger quelques images.")
