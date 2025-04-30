# import streamlit as st
# from PIL import Image
# import io

# def compress_image(image_file, quality=80):
#     """Compresse une image en utilisant PIL."""
#     img = Image.open(image_file)
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format='JPEG', quality=quality, optimize=True)
#     compressed_image = img_byte_arr.getvalue()
#     return compressed_image

# def main():
#     st.title("Compresseur d'Images Streamlit")

#     uploaded_file = st.file_uploader("Téléchargez une image", type=["png", "jpg", "jpeg"])

#     if uploaded_file is not None:
#         st.image(uploaded_file, caption="Image originale", use_column_width=True)

#         compression_quality = st.slider("Qualité de compression (0-100)", 0, 100, 80)

#         if st.button("Compresser l'image"):
#             compressed_data = compress_image(uploaded_file, quality=compression_quality)

#             st.subheader("Image compressée")
#             st.image(compressed_data, caption="Image compressée", use_column_width=True)

#             st.download_button(
#                 label="Télécharger l'image compressée",
#                 data=compressed_data,
#                 file_name="compressed_image.jpg",
#                 mime="image/jpeg"
#             )

# if __name__ == "__main__":
#     main()

import streamlit as st
from PIL import Image
import io

# 🎨 Arrière-plan doux (optionnel)
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
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ✂️ Compression d'image avec conversion RGBA → RGB
def compress_image(image_file, quality=80):
    img = Image.open(image_file)

    # Convertir en RGB si l'image a de la transparence
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG', quality=quality, optimize=True)
    return img_byte_arr.getvalue()

# 📏 Taille du fichier (en Ko)
def get_file_size(file_bytes):
    return round(len(file_bytes) / 1024, 2)

# 💖 Application principale
def main():
    add_background_color()

    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📷 Compresseur d'Images Émotionnel 💖</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Transformez vos souvenirs en œuvres légères mais inoubliables ✨</p>", unsafe_allow_html=True)
    st.markdown("---")

    uploaded_file = st.file_uploader("📤 Téléversez une image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.markdown("### 🖼️ Image originale")
        st.image(uploaded_file, caption="Voici votre image, telle qu'elle est 🧡")

        original_bytes = uploaded_file.getvalue()
        original_size = get_file_size(original_bytes)

        compression_quality = st.slider("🔧 Choisissez le niveau de compression :", 0, 100, 80)

        if st.button("✨ Compresser avec amour ✂️"):
            compressed_data = compress_image(uploaded_file, quality=compression_quality)
            compressed_size = get_file_size(compressed_data)

            st.markdown("### 💡 Résultat de la compression")
            st.image(compressed_data, caption="Une version allégée mais toujours pleine d’émotion 💫")

            st.success(f"📏 Taille originale : {original_size} Ko")
            st.success(f"📉 Taille compressée : {compressed_size} Ko")
            st.info(f"🎯 Gain : {original_size - compressed_size:.2f} Ko")

            st.download_button(
                label="📥 Télécharger l'image compressée",
                data=compressed_data,
                file_name="compressed_image.jpg",
                mime="image/jpeg"
            )

    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 0.9em;'>Fait avec ❤️ grâce à Streamlit & PIL</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
