# import streamlit as st
# import cv2
# import numpy as np
# from PIL import Image
# import io

# def process_image(image_bytes, x1, y1, x2, y2):
#     """Modifie une image en remplissant un rectangle de blanc"""
#     if image_bytes is None:
#         return None

#     # Décoder l'image
#     img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
#     if img is None:
#         return None

#     # Dessiner un rectangle blanc
#     cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)

#     # Reconvertir en bytes
#     return cv2.imencode(".png", img)[1].tobytes()

# st.title("🧽 Supprimer une zone d'une image")

# uploaded_file = st.file_uploader("📤 Téléversez une image", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Lire l'image une seule fois
#     image_bytes = uploaded_file.read()
#     image = Image.open(io.BytesIO(image_bytes))

#     st.image(image, caption="🖼️ Image originale", use_column_width=True)

#     st.markdown("### ✏️ Entrez les coordonnées de la zone à supprimer")

#     # Coordonnées à saisir
#     col1, col2 = st.columns(2)
#     with col1:
#         x1 = st.number_input("x1 (gauche)", min_value=0, value=10)
#         y1 = st.number_input("y1 (haut)", min_value=0, value=10)
#     with col2:
#         x2 = st.number_input("x2 (droite)", min_value=0, value=100)
#         y2 = st.number_input("y2 (bas)", min_value=0, value=100)

#     if st.button("🧼 Supprimer la zone sélectionnée"):
#         modified_image_bytes = process_image(image_bytes, int(x1), int(y1), int(x2), int(y2))
#         if modified_image_bytes:
#             st.image(modified_image_bytes, caption="✅ Image modifiée", use_column_width=True)
#             st.download_button(
#                 label="📥 Télécharger l'image modifiée",
#                 data=modified_image_bytes,
#                 file_name="image_modifiee.png",
#                 mime="image/png"
#             )
#         else:
#             st.error("Une erreur est survenue lors du traitement de l'image.")

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# Ajouter des styles CSS pour personnaliser l'apparence
def add_background_color():

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
    
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 0 25px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #FF6F61;
            font-size: 3em;
            text-align: center;
        }
        .stButton > button {
            background-color: #FF6F61;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #ff4040;
        }
        .stDownloadButton > button {
            background-color: #28a745;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stDownloadButton > button:hover {
            background-color: #218838;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def process_image(image_bytes, x1, y1, x2, y2):
    """Modifie une image en remplissant un rectangle de blanc"""
    if image_bytes is None:
        return None

    # Décoder l'image
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        return None

    # Dessiner un rectangle blanc
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)

    # Reconvertir en bytes
    return cv2.imencode(".png", img)[1].tobytes()

# Personnaliser l'apparence
add_background_color()

# Titre et message
st.markdown("<h1>🧽 Supprimer une zone d'une image 💖</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size: 18px; color: #6c757d; text-align: center;'>Donnez une nouvelle vie à vos images. 🎨✨ Supprimez des objets ou des zones indésirables et créez quelque chose d'unique !</p>",
    unsafe_allow_html=True
)

# Téléchargement de l'image
uploaded_file = st.file_uploader("📤 Téléversez une image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Lire l'image une seule fois
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Afficher l'image originale
    st.image(image, caption="🖼️ Image originale")

    st.markdown("### ✏️ Entrez les coordonnées de la zone à supprimer")

    # Coordonnées à saisir
    col1, col2 = st.columns(2)
    with col1:
        x1 = st.number_input("x1 (gauche)", min_value=0, value=10)
        y1 = st.number_input("y1 (haut)", min_value=0, value=10)
    with col2:
        x2 = st.number_input("x2 (droite)", min_value=0, value=100)
        y2 = st.number_input("y2 (bas)", min_value=0, value=100)

    if st.button("🧼 Supprimer la zone sélectionnée"):
        modified_image_bytes = process_image(image_bytes, int(x1), int(y1), int(x2), int(y2))
        if modified_image_bytes:
            st.image(modified_image_bytes, caption="✅ Image modifiée", use_column_width=True)
            st.download_button(
                label="📥 Télécharger l'image modifiée",
                data=modified_image_bytes,
                file_name="image_modifiee.png",
                mime="image/png"
            )
        else:
            st.error("Une erreur est survenue lors du traitement de l'image.")

st.markdown(
    "<p style='font-size: 12px; color: #6c757d; text-align: center;'>Fait avec amour 💖 pour vous par Streamlit. ✨</p>",
    unsafe_allow_html=True
)
