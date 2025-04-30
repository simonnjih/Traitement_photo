# import streamlit as st
# from PIL import Image

# # Fonctions d'amélioration des images
# def adjust_brightness(pixel, factor):
#     """Ajuste la luminosité d'un pixel."""
#     return tuple(min(int(c * factor), 255) for c in pixel)

# def adjust_contrast(pixel, factor):
#     """Ajuste le contraste d'un pixel."""
#     avg = sum(pixel) // 3
#     return tuple(min(max(int((c - avg) * factor + avg), 0), 255) for c in pixel)

# def adjust_saturation(pixel, factor):
#     """Ajuste la saturation d'un pixel."""
#     r, g, b = pixel
#     avg = (r + g + b) // 3
#     r = int(avg + (r - avg) * factor)
#     g = int(avg + (g - avg) * factor)
#     b = int(avg + (b - avg) * factor)
#     return (min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))

# def enhance_image(image, brightness_factor, contrast_factor, saturation_factor):
#     """Améliore l'image en ajustant la luminosité, le contraste et la saturation."""
#     pixels = image.load()  # Charger les pixels de l'image
#     width, height = image.size

#     # Parcourir tous les pixels
#     for x in range(width):
#         for y in range(height):
#             original_pixel = pixels[x, y]

#             # Ajuster la luminosité
#             bright_pixel = adjust_brightness(original_pixel, brightness_factor)

#             # Ajuster le contraste
#             contrast_pixel = adjust_contrast(bright_pixel, contrast_factor)

#             # Ajuster la saturation
#             enhanced_pixel = adjust_saturation(contrast_pixel, saturation_factor)

#             # Mettre à jour
#             pixels[x, y] = enhanced_pixel

#     return image

# # Créer l'interface Streamlit
# def main():
#     st.title("Amélioration d'Image")
#     st.write("Ajustez la luminosité, le contraste et la saturation de l'image.")

#     # Uploader une image
#     uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Image d'origine")

#         # Contrôles des paramètres
#         brightness_factor = st.slider("Luminosité", 0.5, 3.0, 1.5)
#         contrast_factor = st.slider("Contraste", 0.5, 3.0, 1.5)
#         saturation_factor = st.slider("Saturation", 0.5, 3.0, 1.5)

#         # Appliquer les ajustements
#         if st.button("Améliorer l'image"):
#             enhanced_image = enhance_image(image, brightness_factor, contrast_factor, saturation_factor)
#             st.image(enhanced_image, caption="Image Améliorée")
#             st.success("L'image a été améliorée avec succès!")

#         # Ajouter un bouton de téléchargement
#             st.download_button(
#                 label="Télécharger l'image améliorée",
#                 data=img_byte_arr,
#                 file_name="image_ameliorée.png",
#                 mime="image/png"
#             )

# # Lancer l'application
# if __name__ == "__main__":
#     main()
# # 
# import streamlit as st
# from PIL import Image
# import io

# # Fonctions d'amélioration des images
# def adjust_brightness(pixel, factor):
#     """Ajuste la luminosité d'un pixel."""
#     return tuple(min(int(c * factor), 255) for c in pixel)

# def adjust_contrast(pixel, factor):
#     """Ajuste le contraste d'un pixel."""
#     avg = sum(pixel) // 3
#     return tuple(min(max(int((c - avg) * factor + avg), 0), 255) for c in pixel)

# def adjust_saturation(pixel, factor):
#     """Ajuste la saturation d'un pixel."""
#     r, g, b = pixel
#     avg = (r + g + b) // 3
#     r = int(avg + (r - avg) * factor)
#     g = int(avg + (g - avg) * factor)
#     b = int(avg + (b - avg) * factor)
#     return (min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))

# def enhance_image(image, brightness_factor, contrast_factor, saturation_factor, progress_callback=None):
#     """Améliore l'image en ajustant la luminosité, le contraste et la saturation."""
#     pixels = image.load()  # Charger les pixels de l'image
#     width, height = image.size

#     total_pixels = width * height
#     processed_pixels = 0

#     # Parcourir tous les pixels
#     for x in range(width):
#         for y in range(height):
#             original_pixel = pixels[x, y]

#             # Ajuster la luminosité
#             bright_pixel = adjust_brightness(original_pixel, brightness_factor)

#             # Ajuster le contraste
#             contrast_pixel = adjust_contrast(bright_pixel, contrast_factor)

#             # Ajuster la saturation
#             enhanced_pixel = adjust_saturation(contrast_pixel, saturation_factor)

#             # Mettre à jour le pixel
#             pixels[x, y] = enhanced_pixel

#             processed_pixels += 1
#             if progress_callback:
#                 # Calculer le pourcentage de pixels traités
#                 progress_callback(int((processed_pixels / total_pixels) * 100))

#     return image

# def save_image_to_bytes(image):
#     """Convertit l'image en un flux d'octets pour le téléchargement."""
#     img_byte_arr = io.BytesIO()
#     image.save(img_byte_arr, format='PNG')
#     img_byte_arr.seek(0)
#     return img_byte_arr

# # Créer l'interface Streamlit
# def main():
#     st.title("Amélioration d'Image")
#     st.write("Ajustez la luminosité, le contraste et la saturation de l'image.")

#     # Uploader une image
#     uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Image d'origine")

#         # Contrôles des paramètres
#         brightness_factor = st.slider("Luminosité", 0.5, 3.0, 1.5)
#         contrast_factor = st.slider("Contraste", 0.5, 3.0, 1.5)
#         saturation_factor = st.slider("Saturation", 0.5, 3.0, 1.5)

#         # Initialiser la barre de progression
#         progress_bar = st.progress(0)
#         progress_text = st.empty()

#         # Appliquer les ajustements
#         if st.button("Améliorer l'image"):
#             progress_text.text("Traitement en cours... Veuillez patienter.")
            
#             # Appliquer les améliorations et afficher la progression
#             enhanced_image = enhance_image(image, brightness_factor, contrast_factor, saturation_factor, progress_callback=progress_bar.progress)

#             # Afficher l'image améliorée
#             st.image(enhanced_image, caption="Image Améliorée", use_column_width=True)
#             st.success("L'image a été améliorée avec succès!")

#             # Convertir l'image améliorée en octets pour le téléchargement
#             img_byte_arr = save_image_to_bytes(enhanced_image)

#             # Ajouter un bouton de téléchargement
#             st.download_button(
#                 label="Télécharger l'image améliorée",
#                 data=img_byte_arr,
#                 file_name="image_ameliorée.png",
#                 mime="image/png"
#             )

# # Lancer l'application
# if __name__ == "__main__":
#     main()

# import streamlit as st
# from PIL import Image
# import io
# import time

# # Fonctions d'amélioration des images
# def adjust_brightness(pixel, factor):
#     """Ajuste la luminosité d'un pixel."""
#     return tuple(min(int(c * factor), 255) for c in pixel)

# def adjust_contrast(pixel, factor):
#     """Ajuste le contraste d'un pixel."""
#     avg = sum(pixel) // 3
#     return tuple(min(max(int((c - avg) * factor + avg), 0), 255) for c in pixel)

# def adjust_saturation(pixel, factor):
#     """Ajuste la saturation d'un pixel."""
#     r, g, b = pixel
#     avg = (r + g + b) // 3
#     r = int(avg + (r - avg) * factor)
#     g = int(avg + (g - avg) * factor)
#     b = int(avg + (b - avg) * factor)
#     return (min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))

# def enhance_image(image, brightness_factor, contrast_factor, saturation_factor, progress_callback=None):
#     """Améliore l'image en ajustant la luminosité, le contraste et la saturation."""
#     pixels = image.load()  # Charger les pixels de l'image
#     width, height = image.size

#     total_pixels = width * height
#     processed_pixels = 0

#     # Parcourir tous les pixels
#     for x in range(width):
#         for y in range(height):
#             original_pixel = pixels[x, y]

#             # Ajuster la luminosité
#             bright_pixel = adjust_brightness(original_pixel, brightness_factor)

#             # Ajuster le contraste
#             contrast_pixel = adjust_contrast(bright_pixel, contrast_factor)

#             # Ajuster la saturation
#             enhanced_pixel = adjust_saturation(contrast_pixel, saturation_factor)

#             # Mettre à jour le pixel
#             pixels[x, y] = enhanced_pixel

#             processed_pixels += 1
#             if progress_callback:
#                 # Calculer le pourcentage de temps écoulé et mettre à jour la progression
#                 progress_callback(processed_pixels / total_pixels)

#     return image

# def save_image_to_bytes(image):
#     """Convertit l'image en un flux d'octets pour le téléchargement."""
#     img_byte_arr = io.BytesIO()
#     image.save(img_byte_arr, format='PNG')
#     img_byte_arr.seek(0)
#     return img_byte_arr

# # Créer l'interface Streamlit
# def main():
#     st.title("Amélioration d'Image")
#     st.write("Ajustez la luminosité, le contraste et la saturation de l'image.")

#     # Uploader une image
#     uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Image d'origine")

#         # Contrôles des paramètres
#         brightness_factor = st.slider("Luminosité", 0.5, 3.0, 1.5)
#         contrast_factor = st.slider("Contraste", 0.5, 3.0, 1.5)
#         saturation_factor = st.slider("Saturation", 0.5, 3.0, 1.5)

#         # Initialiser la barre de progression
#         progress_bar = st.progress(0)
#         progress_text = st.empty()

#         # Appliquer les ajustements
#         if st.button("Améliorer l'image"):
#             progress_text.text("Traitement en cours... Veuillez patienter.")
            
#             # Simuler le temps de calcul (par exemple, 5 secondes)
#             start_time = time.time()

#             # Appliquer les améliorations et afficher la progression
#             enhanced_image = enhance_image(image, brightness_factor, contrast_factor, saturation_factor, progress_callback=progress_bar.progress)

#             end_time = time.time()
#             processing_time = end_time - start_time

#             progress_text.text(f"Traitement terminé en {processing_time:.2f} secondes.")
            
#             # Afficher l'image améliorée
#             st.image(enhanced_image, caption="Image Améliorée", use_column_width=True)
#             st.success("L'image a été améliorée avec succès!")

#             # Convertir l'image améliorée en octets pour le téléchargement
#             img_byte_arr = save_image_to_bytes(enhanced_image)

#             # Ajouter un bouton de téléchargement
#             st.download_button(
#                 label="Télécharger l'image améliorée",
#                 data=img_byte_arr,
#                 file_name="image_ameliorée.png",
#                 mime="image/png"
#             )

# # Lancer l'application
# if __name__ == "__main__":
#     main()

# import streamlit as st
# from PIL import Image
# import io

# # Fonctions d'amélioration des images
# def adjust_brightness(pixel, factor):
#     """Ajuste la luminosité d'un pixel."""
#     return tuple(min(int(c * factor), 255) for c in pixel)

# def adjust_contrast(pixel, factor):
#     """Ajuste le contraste d'un pixel."""
#     avg = sum(pixel) // 3
#     return tuple(min(max(int((c - avg) * factor + avg), 0), 255) for c in pixel)

# def adjust_saturation(pixel, factor):
#     """Ajuste la saturation d'un pixel."""
#     r, g, b = pixel
#     avg = (r + g + b) // 3
#     r = int(avg + (r - avg) * factor)
#     g = int(avg + (g - avg) * factor)
#     b = int(avg + (b - avg) * factor)
#     return (min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))

# def enhance_image(image, brightness_factor, contrast_factor, saturation_factor):
#     """Améliore l'image en ajustant la luminosité, le contraste et la saturation."""
#     pixels = image.load()  # Charger les pixels de l'image
#     width, height = image.size

#     # Parcourir tous les pixels
#     for x in range(width):
#         for y in range(height):
#             original_pixel = pixels[x, y]

#             # Ajuster la luminosité
#             bright_pixel = adjust_brightness(original_pixel, brightness_factor)

#             # Ajuster le contraste
#             contrast_pixel = adjust_contrast(bright_pixel, contrast_factor)

#             # Ajuster la saturation
#             enhanced_pixel = adjust_saturation(contrast_pixel, saturation_factor)

#             # Mettre à jour
#             pixels[x, y] = enhanced_pixel

#     return image

# def save_image_to_bytes(image):
#     """Convertit l'image en un flux d'octets pour le téléchargement."""
#     img_byte_arr = io.BytesIO()
#     image.save(img_byte_arr, format='PNG')
#     img_byte_arr.seek(0)
#     return img_byte_arr

# # Créer l'interface Streamlit
# def main():
#     st.title("Amélioration d'Image")
#     st.write("Ajustez la luminosité, le contraste et la saturation de l'image.")

#     # Uploader une image
#     uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Image d'origine", use_column_width=True)

#         # Contrôles des paramètres
#         brightness_factor = st.slider("Luminosité", 0.5, 3.0, 1.5)
#         contrast_factor = st.slider("Contraste", 0.5, 3.0, 1.5)
#         saturation_factor = st.slider("Saturation", 0.5, 3.0, 1.5)

#         # Appliquer les ajustements
#         if st.button("Améliorer l'image"):
#             enhanced_image = enhance_image(image, brightness_factor, contrast_factor, saturation_factor)
#             st.image(enhanced_image, caption="Image Améliorée", use_column_width=True)
#             st.success("L'image a été améliorée avec succès!")

#             # Convertir l'image améliorée en octets pour le téléchargement
#             img_byte_arr = save_image_to_bytes(enhanced_image)

#             # Ajouter un bouton de téléchargement
#             st.download_button(
#                 label="Télécharger l'image améliorée",
#                 data=img_byte_arr,
#                 file_name="image_ameliorée.png",
#                 mime="image/png"
#             )

# # Lancer l'application
# if __name__ == "__main__":
#     main()

import streamlit as st
from PIL import Image
import io

# 🎨 Configuration et Style
st.set_page_config(page_title="🎨 L'Art du Pixel", page_icon="🖌️", layout="wide")
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
# CSS personnalisé
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #eef2f3, #d4e1ea);
        }
        .title {
            text-align: center;
            font-size: 3em;
            color: #2a3d7c;
            font-weight: bold;
            margin-top: 40px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.4em;
            color: #333;
            margin-bottom: 50px;
        }
        .card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .download-area {
            text-align: center;
            margin-top: 40px;
        }
        .highlight {
            color: #5c7aea;
            font-weight: bold;
        }
        .story {
            font-style: italic;
            color: #444;
            text-align: center;
            margin-bottom: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 Fonctions d’ajustement
def adjust_brightness(pixel, factor):
    return tuple(min(int(c * factor), 255) for c in pixel)

def adjust_contrast(pixel, factor):
    avg = sum(pixel) // 3
    return tuple(min(max(int((c - avg) * factor + avg), 0), 255) for c in pixel)

def adjust_saturation(pixel, factor):
    r, g, b = pixel
    avg = (r + g + b) // 3
    r = int(avg + (r - avg) * factor)
    g = int(avg + (g - avg) * factor)
    b = int(avg + (b - avg) * factor)
    return (min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255))

def enhance_image(image, brightness_factor, contrast_factor, saturation_factor):
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            p = pixels[x, y]
            p = adjust_brightness(p, brightness_factor)
            p = adjust_contrast(p, contrast_factor)
            p = adjust_saturation(p, saturation_factor)
            pixels[x, y] = p
    return image

def save_image_to_bytes(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

# 🖼️ Titre & Histoire
st.markdown('<div class="title">🖌️ L\'Art du Pixel</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Par un codeur qui transforme les pixels en poésie visuelle.</div>', unsafe_allow_html=True)

st.markdown('<div class="story">"Chaque pixel est une note, chaque image une symphonie. Le code est la baguette."</div>', unsafe_allow_html=True)

# 📤 Upload de l’image
uploaded_file = st.file_uploader("📤 Importez une image à transformer", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(image, caption="Image originale")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎛️ Réglages artistiques")
        brightness = st.slider("✨ Luminosité", 0.5, 3.0, 1.5)
        contrast = st.slider("🌗 Contraste", 0.5, 3.0, 1.5)
        saturation = st.slider("🌈 Saturation", 0.5, 3.0, 1.5)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🎨 Créer l'image magique"):
            enhanced_image = enhance_image(image.copy(), brightness, contrast, saturation)

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(enhanced_image, caption="Image transformée par l'art")
            st.markdown('</div>', unsafe_allow_html=True)

            img_byte_arr = save_image_to_bytes(enhanced_image)
            st.markdown('<div class="download-area">', unsafe_allow_html=True)
            st.download_button(
                label="📥 Télécharger cette œuvre",
                data=img_byte_arr,
                file_name="chef_doeuvre_pixel.png",
                mime="image/png"
            )
            st.markdown('</div>', unsafe_allow_html=True)
