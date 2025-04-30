# import streamlit as st
# import cv2
# import numpy as np
# from PIL import Image

# # Fonction pour changer la couleur des cheveux
# def changer_couleur_cheveux(image, couleur):
#     # Convertir l'image en format numpy array
#     img = np.array(image)
    
#     # Convertir en espace de couleur HSV
#     hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#     # Définir une plage de couleurs pour détecter les cheveux (valeurs approximatives)
#     # Cette plage peut être ajustée en fonction de la couleur des cheveux de l'image originale.
#     # Exemple: détecter une couleur brune ou noire pour les cheveux.
#     lower_hue = np.array([0, 0, 0])  # Plage basse de la couleur des cheveux
#     upper_hue = np.array([179, 255, 70])  # Plage haute de la couleur des cheveux
#     mask = cv2.inRange(hsv, lower_hue, upper_hue)

#     # Changer la couleur des pixels correspondant aux cheveux
#     img[mask > 0] = couleur

#     # Convertir l'image de retour au format RGB
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     return img

# # Interface Streamlit
# st.title("Changer la couleur des cheveux")

# # Télécharger l'image
# image_upload = st.file_uploader("Téléchargez une image", type=["jpg", "png"])

# if image_upload is not None:
#     # Charger l'image
#     image = Image.open(image_upload)

#     # Afficher l'image originale
#     st.image(image, caption="Image Originale", use_column_width=True)

#     # Choisir la nouvelle couleur de cheveux
#     couleur_choisie = st.color_picker("Choisissez une couleur pour les cheveux", "#ff0000")

#     # Convertir la couleur choisie en RGB
#     couleur_rgb = tuple(int(couleur_choisie[i:i+2], 16) for i in (1, 3, 5))

#     # Appliquer le changement de couleur
#     image_modifiee = changer_couleur_cheveux(image, couleur_rgb)

#     # Afficher l'image modifiée
#     st.image(image_modifiee, caption="Image avec Couleur de Cheveux Modifiée", use_column_width=True)
# import os
# import cv2
# import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt
# import streamlit as st
# from PIL import Image

# # Charger l'image
# def li(p):
#     img = cv2.imread(p)
#     img = img.astype(np.float32) / 127.5 - 1
#     img = np.expand_dims(img, 0)
#     img = tf.convert_to_tensor(img)
#     return img

# # Prétraiter l'image
# def pi(img, td=224):
#     shp = tf.cast(tf.shape(img)[1:-1], tf.float32)
#     sd = min(shp)
#     scl = td / sd
#     nhp = tf.cast(shp * scl, tf.int32)
#     img = tf.image.resize(img, nhp)
#     img = tf.image.resize_with_crop_or_pad(img, td, td)
#     return img

# # Fonction pour appliquer CartoonGAN sur l'image
# def cartoon(img_p):
#     # Charger l'image
#     si = li(img_p)
#     psi = pi(si, td=512)

#     # Modèle TFLite CartoonGAN
#     m = r'D:\DTI\1.tflite'  # Remplacez ce chemin par le chemin de votre modèle .tflite
#     i = tf.lite.Interpreter(model_path=m)
#     ind = i.get_input_details()
#     i.allocate_tensors()
#     i.set_tensor(ind[0]['index'], psi)
#     i.invoke()

#     r = i.tensor(i.get_output_details()[0]['index'])()

#     # Post-traitement de la sortie du modèle
#     o = (np.squeeze(r) + 1.0) * 127.5
#     o = np.clip(o, 0, 255).astype(np.uint8)
#     o = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)

#     return o

# # Interface utilisateur Streamlit
# st.title("Transformation d'image en style animé avec CartoonGAN")

# # Téléchargement d'image par l'utilisateur
# uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Sauvegarder l'image téléchargée pour traitement
#     img = Image.open(uploaded_file)
#     img_path = "uploaded_image.jpg"
#     img.save(img_path)

#     # Affichage de l'image originale
#     st.image(img, caption="Image originale", use_column_width=True)

#     # Appliquer CartoonGAN sur l'image
#     st.write("Transformation en cours...")
#     cartoon_image = cartoon(img_path)

#     # Afficher l'image transformée
#     st.image(cartoon_image, caption="Image transformée en style animé", use_column_width=True)

import os
import cv2
import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image
import io

# Page config
st.set_page_config(
    page_title="✨ CartoonGAN | Transforme ton monde en dessin animé ✨",
    layout="wide",
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

# 🌟 CSS personnalisé
st.markdown("""
    <style>
    html, body {
        background-color: #fefefe;
        font-family: 'Segoe UI', sans-serif;
        color: #2c3e50;
    }
    .main-title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.3em;
        color: #7f8c8d;
        margin-bottom: 40px;
    }
    .quote-box {
        background: #ecf0f1;
        padding: 20px;
        border-radius: 10px;
        margin-top: 50px;
        font-style: italic;
        text-align: center;
        color: #34495e;
    }
    .file-box {
        background-color: #f7f9fa;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 🌈 Titre principal
st.markdown('<div class="main-title">🎨 CartoonGAN : Dessine ton monde autrement</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Parce que chaque photo cache une histoire magique à révéler en style animé ✨</div>', unsafe_allow_html=True)

# 💾 Upload image
st.markdown('<div class="file-box">📤 Télécharge ton image ci-dessous pour la transformer en chef-d’œuvre animé :</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

# 🔧 CartoonGAN model (inchangé)
def li(p):
    img = cv2.imread(p)
    img = img.astype(np.float32) / 127.5 - 1
    img = np.expand_dims(img, 0)
    img = tf.convert_to_tensor(img)
    return img

def pi(img, td=224):
    shp = tf.cast(tf.shape(img)[1:-1], tf.float32)
    sd = min(shp)
    scl = td / sd
    nhp = tf.cast(shp * scl, tf.int32)
    img = tf.image.resize(img, nhp)
    img = tf.image.resize_with_crop_or_pad(img, td, td)
    return img

def cartoon(img_p):
    si = li(img_p)
    psi = pi(si, td=512)

    m = r'D:\DTI\1.tflite'  # 🔄 Change ce chemin selon ton modèle
    i = tf.lite.Interpreter(model_path=m)
    ind = i.get_input_details()
    i.allocate_tensors()
    i.set_tensor(ind[0]['index'], psi)
    i.invoke()

    r = i.tensor(i.get_output_details()[0]['index'])()
    o = (np.squeeze(r) + 1.0) * 127.5
    o = np.clip(o, 0, 255).astype(np.uint8)
    o = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)
    return o

# 🚀 Traitement
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = "uploaded_image.jpg"
    img.save(img_path)

    st.image(img, caption="📸 Image originale", use_column_width=True)

    st.markdown("## ✨ En train de révéler la magie…")
    cartoon_image = cartoon(img_path)

    # Affichage du résultat
    st.image(cartoon_image, caption="🖌️ Image transformée en style animé", use_column_width=True)

    # 🔽 Télécharger le résultat
    st.markdown("### 📥 Télécharger votre image animée")
    cartoon_pil = Image.fromarray(cartoon_image)
    img_bytes = io.BytesIO()
    cartoon_pil.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    st.download_button(
        label="🎉 Télécharger l'image stylisée",
        data=img_bytes,
        file_name="cartoon_image.png",
        mime="image/png"
    )

    # Citation inspirante
    st.markdown("""
        <div class="quote-box">
            "Les souvenirs sont des images gravées dans le cœur...<br>
            Offrez-leur des couleurs d’enfance et de rêve, avec CartoonGAN." 🌟
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("Commence par télécharger une image pour laisser la magie opérer 🎞️")

