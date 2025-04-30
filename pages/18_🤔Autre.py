# import streamlit as st
# from PIL import Image, ImageDraw, ImageFont
# import random
# import emoji
# import numpy as np

# st.title("Appliquez des autocollants et des émojis sur votre image")

# # Télécharger l'image
# uploaded_image = st.file_uploader("Téléchargez une image", type=["png", "jpg", "jpeg"])

# if uploaded_image is not None:
#     image = Image.open(uploaded_image)
    
#     # Afficher l'image téléchargée
#     st.image(image, caption="Image originale")
    
#     # Ajouter un émoji
#     emoji_list = ["😀", "😍", "😂", "🤔", "😎"]
#     selected_emoji = st.selectbox("Choisissez un émoji", emoji_list)

#     # Définir la taille de l'émoji
#     emoji_size = st.slider("Taille de l'émoji", min_value=30, max_value=200, value=50)
    
#     # Convertir l'émoji en image avec Pillow
#     emoji_img = Image.new("RGBA", (emoji_size, emoji_size), (255, 255, 255, 0))
#     draw = ImageDraw.Draw(emoji_img)
#     font = ImageFont.load_default()
#     draw.text((10, 10), selected_emoji, font=font, fill="black")

#     # Placer l'émoji sur l'image
#     emoji_pos = (random.randint(50, image.width - emoji_size), random.randint(50, image.height - emoji_size))
#     image.paste(emoji_img, emoji_pos, emoji_img)

#     # Afficher l'image avec émoji
#     st.image(image, caption="Image avec émoji ajouté")

    # # Ajouter des autocollants (ici un exemple simple)
    # st.sidebar.subheader("Choisir un autocollant")
    # sticker_options = ["Sticker 1", "Sticker 2", "Sticker 3"]
    # selected_sticker = st.sidebar.selectbox("Sélectionnez un autocollant", sticker_options)
    
    # if selected_sticker == "Sticker 1":
    #     sticker = Image.open("stickers/sticker1.png")
    # elif selected_sticker == "Sticker 2":
    #     sticker = Image.open("stickers/sticker2.png")
    # elif selected_sticker == "Sticker 3":
    #     sticker = Image.open("stickers/sticker3.png")
    
    # # Ajuster la taille de l'autocollant
    # sticker_size = st.sidebar.slider("Taille de l'autocollant", min_value=30, max_value=150, value=100)
    # sticker = sticker.resize((sticker_size, sticker_size))

    # # Placer l'autocollant sur l'image
    # sticker_pos = (random.randint(50, image.width - sticker_size), random.randint(50, image.height - sticker_size))
    # image.paste(sticker, sticker_pos, sticker)

    # # Afficher l'image avec autocollant
    # st.image(image, caption="Image avec autocollant ajouté", use_column_width=True)
    
    # # Ajouter un texte à l'image
    # text_input = st.text_input("Ajoutez du texte à l'image", "Snapchat Style!")
    # if text_input:
    #     draw = ImageDraw.Draw(image)
    #     font = ImageFont.load_default()
    #     text_size = draw.textsize(text_input, font=font)
    #     text_pos = (random.randint(10, image.width - text_size[0] - 10), random.randint(10, image.height - text_size[1] - 10))
    #     draw.text(text_pos, text_input, font=font, fill="white")
    
    # # Afficher l'image avec texte ajouté
    # st.image(image, caption="Image modifiée avec texte, autocollant et émoji", use_column_width=True)

# import streamlit as st
# from rembg import remove
# from PIL import Image
# import io
# import tempfile

# # Fonction pour enlever l'arrière-plan
# def remove_background(input_image):
#     # Convertir l'image téléchargée en bytes
#     input_bytes = input_image.read()  # Convertir directement en bytes
#     # Utiliser rembg pour supprimer l'arrière-plan sans 'progressbar'
#     output_bytes = remove(input_bytes, force_return_bytes=True)  # Pas de progressbar ici
#     return output_bytes

# # Fonction pour sauvegarder l'image en fichier temporaire
# def save_image(output_bytes):
#     # Créer un fichier temporaire pour sauvegarder l'image
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
#         temp_file.write(output_bytes)
#         return temp_file.name

# # Interface utilisateur Streamlit
# def main():
#     st.title("Suppression d'Arrière-plan d'Image")
#     st.write("Téléchargez une image et l'arrière-plan sera automatiquement supprimé.")

#     # Uploader une image
#     uploaded_file = st.file_uploader("Choisir une image", type=["png", "jpg", "jpeg"])

#     if uploaded_file is not None:
#         # Afficher l'image téléchargée
#         st.image(uploaded_file, caption="Image téléchargée", use_column_width=True)

#         # Appeler la fonction pour enlever l'arrière-plan
#         if st.button("Supprimer l'arrière-plan"):
#             # Supprimer l'arrière-plan de l'image
#             output_bytes = remove_background(uploaded_file)

#             # Convertir les octets en image
#             output_image = Image.open(io.BytesIO(output_bytes))
#             st.image(output_image, caption="Image sans arrière-plan", use_column_width=True)

#             # Sauvegarder l'image dans un fichier temporaire
#             saved_image_path = save_image(output_bytes)

#             # Ajouter un bouton pour télécharger l'image sans arrière-plan
#             st.download_button(
#                 label="Télécharger l'image sans arrière-plan",
#                 data=open(saved_image_path, "rb").read(),
#                 file_name="image_sans_arriere_plan.png",
#                 mime="image/png"
#             )

# # Lancer l'application
# if __name__ == "__main__":
#     main()

import streamlit as st

from streamlit_image_comparison import exif_transpose
from streamlit_image_comparison import read_image_as_pil
from streamlit_image_comparison import pillow_to_base64
from streamlit_image_comparison import local_file_to_base64
from streamlit_image_comparison import local_file_to_base64
from streamlit_image_comparison import pillow_local_file_to_base64
from streamlit_image_comparison import image_comparison

IMAGE_TO_URL = {
    "sample_image_1": "https://user-images.githubusercontent.com/34196005/143309873-c0c1f31c-c42e-4a36-834e-da0a2336bb19.jpg",
    "sample_image_2": "https://user-images.githubusercontent.com/34196005/143309867-42841f5a-9181-4d22-b570-65f90f2da231.jpg",
}


st.set_page_config(
    page_title="Streamlit Image Comparison",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="auto",
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

st.markdown(
    """
    <h2 style='text-align: center'>
    Streamlit Image Comparison Demo
    </h2>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <p style='text-align: center'>
    <br />
    Follow me for more! <a href='https://twitter.com/fcakyon' target='_blank'> <img src="https://img.icons8.com/color/48/000000/twitter--v1.png" height="30"></a><a href='https://github.com/fcakyon' target='_blank'><img src="https://img.icons8.com/fluency/48/000000/github.png" height="27"></a><a href='https://www.linkedin.com/in/fcakyon/' target='_blank'><img src="https://img.icons8.com/fluency/48/000000/linkedin.png" height="30"></a> <a href='https://fcakyon.medium.com/' target='_blank'><img src="https://img.icons8.com/ios-filled/48/000000/medium-monogram.png" height="26"></a>
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("##")

with st.form(key="Streamlit Image Comparison"):
    # image one inputs
    col1, col2 = st.columns([3, 1])
    with col1:
        img1_url = st.text_input("Image one URL:", value=IMAGE_TO_URL["sample_image_1"])
    with col2:
        img1_text = st.text_input("Image one text:", value="YOLOX")

    # image two inputs
    col1, col2 = st.columns([3, 1])
    with col1:
        img2_url = st.text_input("Image two URL:", value=IMAGE_TO_URL["sample_image_2"])
    with col2:
        img2_text = st.text_input("Image two text:", value="SAHI+YOLOX")

    # continious parameters
    col1, col2 = st.columns([1, 1])
    with col1:
        starting_position = st.slider(
            "Starting position of the slider:", min_value=0, max_value=100, value=50
        )
    with col2:
        width = st.slider(
            "Component width:", min_value=400, max_value=1000, value=700, step=100
        )

    # boolean parameters
    col1, col2, col3, col4 = st.columns([1, 3, 3, 3])
    with col2:
        show_labels = st.checkbox("Show labels", value=True)
    with col3:
        make_responsive = st.checkbox("Make responsive", value=True)
    with col4:
        in_memory = st.checkbox("In memory", value=True)

    # centered submit button
    col1, col2, col3 = st.columns([6, 4, 6])
    with col2:
        submit = st.form_submit_button("Update Render 🔥")

static_component = image_comparison(
    img1=img1_url,
    img2=img2_url,
    label1=img1_text,
    label2=img2_text,
    width=width,
    starting_position=starting_position,
    show_labels=show_labels,
    make_responsive=make_responsive,
    in_memory=in_memory,
)