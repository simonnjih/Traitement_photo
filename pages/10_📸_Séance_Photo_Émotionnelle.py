# import streamlit as st
# from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFilter
# import io

# def main():
#     st.title("Advanced Image Editor")

#     st.sidebar.write("## Upload Image")
#     uploaded_file = st.sidebar.file_uploader("", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.sidebar.image(image, caption="Uploaded Image", use_column_width=True)
        
#         st.write("## Edited Image")

#         # Rotation
#         rotate = st.sidebar.slider("Rotate", 0, 360, step=10)
#         rotated_image = image.rotate(rotate)
        
#         # Brightness
#         brightness = st.sidebar.slider("Brightness", 1.0, 3.0, step=0.1)
#         enhancer = ImageEnhance.Brightness(rotated_image)
#         brightened_image = enhancer.enhance(brightness)
        
#         # Contrast
#         contrast = st.sidebar.slider("Contrast", 1.0, 3.0, step=0.1)
#         enhancer = ImageEnhance.Contrast(brightened_image)
#         contrasted_image = enhancer.enhance(contrast)

#         # Sharpness
#         sharpness = st.sidebar.slider("Sharpness", 1.0, 3.0, step=0.1)
#         enhancer = ImageEnhance.Sharpness(contrasted_image)
#         sharpened_image = enhancer.enhance(sharpness)

#         # Grayscale
#         grayscale = st.sidebar.checkbox("Grayscale")
#         edited_image = ImageOps.grayscale(sharpened_image) if grayscale else sharpened_image

#         # Flip
#         flip_option = st.sidebar.selectbox("Flip Image", ["None", "Horizontal", "Vertical"])
#         if flip_option == "Horizontal":
#             edited_image = ImageOps.mirror(edited_image)
#         elif flip_option == "Vertical":
#             edited_image = ImageOps.flip(edited_image)

#         # Crop
#         crop = st.sidebar.checkbox("Crop Image")
#         if crop:
#             left = st.sidebar.number_input("Left", 0, edited_image.width, 0)
#             top = st.sidebar.number_input("Top", 0, edited_image.height, 0)
#             right = st.sidebar.number_input("Right", 0, edited_image.width, edited_image.width)
#             bottom = st.sidebar.number_input("Bottom", 0, edited_image.height, edited_image.height)
#             edited_image = edited_image.crop((left, top, right, bottom))

#         st.image(edited_image, caption="Edited Image", use_column_width=True)

#         # Download Button
#         buffered = io.BytesIO()
#         edited_image.save(buffered, format="JPEG")
#         img_str = buffered.getvalue()
#         st.download_button(
#             "Download Edited Image",
#             img_str,
#             file_name="edited_image.jpg",
#             mime="image/jpeg",
#         )

# if __name__ == "__main__":
#     main()

import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io

# 🌌 Configuration de la page
st.set_page_config(page_title="🎨 Lumière sur l'image", layout="wide")

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
# 🌟 Style HTML
st.markdown("""
    <style>
        html, body {
            background: linear-gradient(to right, #fdfcfb, #e2d1c3);
            color: #2c3e50;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 3.2em;
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
        .highlight-box {
            background-color: #2c3e50;
            color: white;
            padding: 1em;
            border-radius: 12px;
            text-align: center;
            font-size: 1.1em;
            margin-top: 40px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-style: italic;
            color: #95a5a6;
        }
    </style>
""", unsafe_allow_html=True)

# 🖼️ Titre poétique
st.markdown('<div class="main-title">🎨 Lumière sur l\'Image</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Chaque cliché est une émotion figée. Chaque retouche est une seconde chance de la faire vibrer.</div>', unsafe_allow_html=True)

# 📤 Upload
uploaded_file = st.sidebar.file_uploader("📂 Télécharge ton image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Image originale", use_column_width=True)

    # 🎛️ Édition
    st.sidebar.subheader("✨ Paramètres artistiques")

    rotate = st.sidebar.slider("🔄 Rotation", 0, 360, step=10)
    rotated_image = image.rotate(rotate)

    brightness = st.sidebar.slider("☀️ Luminosité", 1.0, 3.0, 1.2, step=0.1)
    enhancer = ImageEnhance.Brightness(rotated_image)
    bright_image = enhancer.enhance(brightness)

    contrast = st.sidebar.slider("🌗 Contraste", 1.0, 3.0, 1.5, step=0.1)
    enhancer = ImageEnhance.Contrast(bright_image)
    contrast_image = enhancer.enhance(contrast)

    sharpness = st.sidebar.slider("🔬 Netteté", 1.0, 3.0, 1.5, step=0.1)
    enhancer = ImageEnhance.Sharpness(contrast_image)
    final_image = enhancer.enhance(sharpness)

    if st.sidebar.checkbox("⚫ Mode N&B"):
        final_image = ImageOps.grayscale(final_image)

    flip_option = st.sidebar.selectbox("🪞 Miroir", ["Aucun", "Horizontal", "Vertical"])
    if flip_option == "Horizontal":
        final_image = ImageOps.mirror(final_image)
    elif flip_option == "Vertical":
        final_image = ImageOps.flip(final_image)

    # 📐 Recadrage
    if st.sidebar.checkbox("✂️ Recadrer l'image"):
        left = st.sidebar.number_input("Gauche", 0, final_image.width, 0)
        top = st.sidebar.number_input("Haut", 0, final_image.height, 0)
        right = st.sidebar.number_input("Droite", 0, final_image.width, final_image.width)
        bottom = st.sidebar.number_input("Bas", 0, final_image.height, final_image.height)
        final_image = final_image.crop((left, top, right, bottom))

    # 🖼️ Affichage final
    st.markdown("### 🌟 Résultat : Ton chef-d'œuvre")
    st.image(final_image, caption="Image transformée", use_column_width=True)

    # 💾 Téléchargement
    st.markdown('<div class="highlight-box">📥 Enregistre ton émotion figée dans le temps</div>', unsafe_allow_html=True)
    buffered = io.BytesIO()
    final_image.save(buffered, format="JPEG")
    img_str = buffered.getvalue()

    st.download_button(
        label="Télécharger l'image retouchée",
        data=img_str,
        file_name="chef_doeuvre.jpg",
        mime="image/jpeg"
    )

    st.markdown('<div class="footer">Fait avec 🧠 et ❤️ pour sublimer tes souvenirs.</div>', unsafe_allow_html=True)
else:
    st.info("Commence par importer une image 📷 pour la transformer en poésie visuelle.")
