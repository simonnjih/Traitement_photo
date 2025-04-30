# from io import BytesIO

# import streamlit as st
# from PIL import Image
# from rembg import remove

# st.set_page_config(layout="wide", page_title="Image Background Remover")

# st.write("## Remove background from your image")
# st.write(
#     "Essayez de télécharger une image pour voir l'arrière-plan disparaître magiquement. Les images en pleine qualité peuvent être téléchargées depuis la barre latérale")
# st.sidebar.write("## Upload and download :gear:")

# # Create the columns
# col1, col2 = st.columns(2)

# # Download the fixed image
# def convert_image(img):
#     buf = BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im

# # Package the transform into a function
# def fix_image(upload):
#     image = Image.open(upload)
#     col1.write("Original Image :camera:")
#     col1.image(image)

#     fixed = remove(image)
#     col2.write("Fixed Image :wrench:")
#     col2.image(fixed)
#     st.sidebar.markdown("\\n")
#     st.sidebar.download_button(
#         "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
#     )

# # Create the file uploader
# my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# # Fix the image!
# if my_upload is not None:
#     fix_image(upload=my_upload)

import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO

# --- Configuration de la page (doit être la première commande) ---
st.set_page_config(layout="wide", page_title="Image Background Remover")
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
# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(135deg, #f4f7f6, #c1d3e0);
        padding: 0;
        margin: 0;
    }

    .header {
        text-align: center;
        color: #fff;
        font-size: 3em;
        font-weight: bold;
        background-color: #2a3d7c;
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.3);
        margin-top: 50px;
    }

    .subheader {
        font-size: 1.8em;
        color: #2a3d7c;
        text-align: center;
        margin-top: 20px;
    }

    .description {
        font-size: 1.2em;
        color: #555;
        text-align: center;
        margin-top: 30px;
        line-height: 1.6;
    }

    .upload-container {
        text-align: center;
        margin-top: 40px;
    }

    .upload-container input {
        font-size: 1.2em;
    }

    .download-button {
        background-color: #2a3d7c;
        color: white;
        padding: 12px 25px;
        font-size: 1.2em;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        transition: background-color 0.3s;
    }

    .download-button:hover {
        background-color: #1a2b55;
    }

    .image-column {
        padding: 20px;
    }

    .footer {
        text-align: center;
        font-size: 1em;
        color: #555;
        padding: 20px;
        background-color: #2a3d7c;
        color: white;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Titre et introduction ---
st.markdown('<div class="header">Remove Background from Your Image</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="subheader">Transformez vos images en toute simplicité</div>
    <div class="description">
    Essayez de télécharger une image et regardez l'arrière-plan disparaître magiquement !
    Cette application utilise l'IA pour détecter et retirer l'arrière-plan de vos photos.
    </div>
""", unsafe_allow_html=True)

# --- Section d'upload et de téléchargement ---
st.sidebar.write("## Upload your image :gear:")

col1, col2 = st.columns(2)

# Fonction pour convertir l'image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Fonction pour supprimer l'arrière-plan de l'image
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    # Appliquer la suppression de l'arrière-plan
    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)

    # Bouton de téléchargement
    st.sidebar.markdown("\\n")
    st.sidebar.download_button(
        "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
    )

# --- Télécharger une image ---
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Exécuter la fonction si une image est téléchargée
if my_upload is not None:
    fix_image(upload=my_upload)

# --- Footer ---
st.markdown("""
    <div class="footer">
    Créé avec ❤️ par Njitchoua
    </div>
""", unsafe_allow_html=True)
