# import streamlit as st
# import cv2
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt


# # Configuration de la page Streamlit
# st.set_page_config(
#     page_title="ImageMagic Pro",
#     page_icon="✨",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Fonction pour convertir une couleur hexadécimale en tuple BGR
# def hex_to_bgr(hex_color):
#     hex_color = hex_color.lstrip('#')
#     return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))  # Convertir en (B, G, R)

# # Titre de l'application avec un message de bienvenue
# st.title("✨ ImageMagic Pro")
# # st.markdown("""
# #     **Bienvenue sur ImageMagic Pro !**  
# #     Transformez vos images en œuvres d'art grâce à des outils de traitement d'image puissants et intuitifs.  
# #     Téléchargez une image, appliquez des transformations et téléchargez le résultat final.  
# #     *Faites passer vos images au niveau supérieur !*
# # """)

# # Téléchargement de l'image
# uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Convertir l'image téléchargée en un format utilisable par OpenCV
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

#     # Afficher l'image originale
#     st.subheader("Image Originale")
#     st.image(image, channels="BGR" , caption="Votre image originale")

#     # Options de traitement d'image dans la barre latérale
#     st.sidebar.header("🎨 Options de Traitement d'Image")

#     # 1. Redimensionnement
#     st.sidebar.subheader("📏 Redimensionnement")
#     resize_option = st.sidebar.checkbox("Redimensionner l'image")
#     if resize_option:
#         width = st.sidebar.slider("Largeur", 100, 2000, image.shape[1])
#         height = st.sidebar.slider("Hauteur", 100, 2000, image.shape[0])
#         image = cv2.resize(image, (width, height))

#     # 2. Conversion en niveaux de gris
#     gray_option = st.sidebar.checkbox("Convertir en niveaux de gris")
#     if gray_option:
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # 3. Flou
#     st.sidebar.subheader("🌫️ Flou")
#     blur_option = st.sidebar.checkbox("Appliquer un flou")
#     if blur_option:
#         blur_kernel = st.sidebar.slider("Taille du noyau de flou", 1, 25, 5)
#         if blur_kernel % 2 == 0:  # Le noyau doit être impair
#             blur_kernel += 1
#         image = cv2.GaussianBlur(image, (blur_kernel, blur_kernel), 0)

#     # 4. Amélioration du contraste
#     st.sidebar.subheader("🌈 Contraste et Luminosité")
#     contrast_option = st.sidebar.checkbox("Améliorer le contraste")
#     if contrast_option:
#         alpha = st.sidebar.slider("Alpha (contraste)", 0.0, 3.0, 1.5)
#         beta = st.sidebar.slider("Beta (luminosité)", -50, 50, 0)
#         image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

#     # 5. Seuillage (Thresholding)
#     st.sidebar.subheader("⚖️ Seuillage")
#     threshold_option = st.sidebar.checkbox("Appliquer un seuillage")
#     if threshold_option:
#         threshold_value = st.sidebar.slider("Valeur de seuil", 0, 255, 127)
#         _, image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

#     # 6. Détection de contours
#     st.sidebar.subheader("🖼️ Détection de Contours")
#     edges_option = st.sidebar.checkbox("Détecter les contours")
#     if edges_option:
#         image = cv2.Canny(image, 100, 200)

#     # 7. Rotation
#     st.sidebar.subheader("🔄 Rotation")
#     rotate_option = st.sidebar.checkbox("Faire pivoter l'image")
#     if rotate_option:
#         angle = st.sidebar.slider("Angle de rotation", -180, 180, 0)
#         h, w = image.shape[:2]
#         center = (w // 2, h // 2)
#         rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
#         image = cv2.warpAffine(image, rotation_matrix, (w, h))

#     # 8. Ajout de texte
#     st.sidebar.subheader("✍️ Ajouter du Texte")
#     text_option = st.sidebar.checkbox("Ajouter du texte à l'image")
#     if text_option:
#         text = st.sidebar.text_input("Texte à ajouter", "ImageMagic Pro")
#         position_x = st.sidebar.slider("Position X", 0, image.shape[1], 10)
#         position_y = st.sidebar.slider("Position Y", 0, image.shape[0], 50)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         font_scale = st.sidebar.slider("Taille de la police", 0.5, 3.0, 1.0)
#         font_color_hex = st.sidebar.color_picker("Couleur du texte", "#FFFFFF")
#         font_color = hex_to_bgr(font_color_hex)  # Convertir la couleur hexadécimale en BGR
#         thickness = st.sidebar.slider("Épaisseur du texte", 1, 10, 2)
#         image = cv2.putText(image, text, (position_x, position_y), font, font_scale, font_color, thickness)
    

#     # Afficher l'image transformée
#     st.subheader("🖼️ Image Transformée")
#     st.image(image, channels="BGR" if not gray_option else "GRAY", caption="Votre image transformée")

#     # Télécharger l'image transformée
#     st.subheader("📥 Télécharger l'Image Transformée")
#     if st.button("Télécharger l'image transformée"):
#         # Convertir l'image en format PIL pour le téléchargement
#         if gray_option:
#             pil_image = Image.fromarray(image)
#         else:
#             pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#         st.download_button(
#             label="Télécharger",
#             data=pil_image.tobytes(),
#             file_name="image_transformee.png",
#             mime="image/png"
#         )
#         st.success("✅ Votre image a été téléchargée avec succès !")

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# ⚠️ Toujours mettre set_page_config en premier
st.set_page_config(page_title="✨ ImageMagic Pro", page_icon="✨", layout="wide")

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

# 🎨 Style CSS personnalisé
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom right, #f4f7f6, #cfe0e8);
        }
        .main-title {
            text-align: center;
            font-size: 3em;
            color: #2a3d7c;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3em;
            color: #444;
            margin-bottom: 30px;
        }
        .feature-box {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }
        .download-button {
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 Fonctions
def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

# 🧾 Titre principal
st.markdown('<div class="main-title">✨ ImageMagic Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transformez vos images avec magie, mathématiques et AI !</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Téléchargez une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image, channels="BGR", caption="🖼️ Image originale")

    st.sidebar.title("🎨 Transformations d'image")

    with st.sidebar.expander("📏 Redimensionnement"):
        if st.checkbox("Activer le redimensionnement"):
            width = st.slider("Largeur", 100, 2000, image.shape[1])
            height = st.slider("Hauteur", 100, 2000, image.shape[0])
            image = cv2.resize(image, (width, height))

    if st.sidebar.checkbox("🔲 Niveaux de gris"):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    with st.sidebar.expander("🌫️ Flou Gaussien"):
        if st.checkbox("Appliquer un flou"):
            k = st.slider("Taille du noyau", 1, 25, 5)
            if k % 2 == 0:
                k += 1
            image = cv2.GaussianBlur(image, (k, k), 0)

    with st.sidebar.expander("🌈 Contraste & Luminosité"):
        if st.checkbox("Ajuster"):
            alpha = st.slider("Contraste (α)", 0.5, 3.0, 1.5)
            beta = st.slider("Luminosité (β)", -100, 100, 0)
            image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    with st.sidebar.expander("⚙️ Seuillage"):
        if st.checkbox("Appliquer un seuillage"):
            threshold = st.slider("Seuil", 0, 255, 127)
            _, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    with st.sidebar.expander("🧠 Détection de contours"):
        if st.checkbox("Appliquer Canny"):
            image = cv2.Canny(image, 100, 200)

    with st.sidebar.expander("🔄 Rotation"):
        if st.checkbox("Faire pivoter"):
            angle = st.slider("Angle", -180, 180, 0)
            h, w = image.shape[:2]
            M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
            image = cv2.warpAffine(image, M, (w, h))

    with st.sidebar.expander("✍️ Ajouter du texte"):
        if st.checkbox("Ajouter"):
            text = st.text_input("Texte", "ImageMagic Pro")
            x = st.slider("X", 0, image.shape[1], 50)
            y = st.slider("Y", 0, image.shape[0], 100)
            scale = st.slider("Taille police", 0.5, 3.0, 1.0)
            color = st.color_picker("Couleur", "#ffffff")
            thickness = st.slider("Épaisseur", 1, 10, 2)
            color_bgr = hex_to_bgr(color)
            font = cv2.FONT_HERSHEY_SIMPLEX
            image = cv2.putText(image, text, (x, y), font, scale, color_bgr, thickness)

    # 📸 Affichage image transformée
    st.markdown("## 🧙‍♀️ Résultat")
    st.image(image, channels="BGR" if len(image.shape) == 3 else "GRAY")

    # 🧾 Conversion PIL pour export
    if len(image.shape) == 2:
        pil_image = Image.fromarray(image)
    else:
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    img_bytes = io.BytesIO()
    pil_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # 📥 Téléchargement
    st.markdown('<div class="download-button">', unsafe_allow_html=True)
    st.download_button(
        label="📥 Télécharger l'image transformée",
        data=img_bytes,
        file_name="image_transformee.png",
        mime="image/png"
    )
    st.markdown('</div>', unsafe_allow_html=True)
