# import streamlit as st
# import openai
# from PIL import Image
# import io
# from dotenv import load_dotenv
# import os

# # Charger les variables d'environnement
# load_dotenv()

# # Configuration de l'API OpenAI
# openai.api_key = os.getenv('OPENAI_API_KEY')

# # Fonction pour générer une image à partir du texte
# def generate_image_from_text(text_prompt):
#     response = openai.Image.create(
#         prompt=text_prompt,
#         n=1,
#         size="1024x1024"  # Vous pouvez ajuster la taille
#     )
#     image_url = response['data'][0]['url']
#     return image_url

# # Fonction pour interpréter une image (par exemple, reconnaissance de texte)
# def interpret_image(image):
#     # Pour cette démo, nous allons simplement afficher l'image.
#     # Vous pouvez intégrer une API de reconnaissance d'image ici (par exemple, OpenAI CLIP, Google Vision, etc.).
#     st.image(image, caption='Image interprétée')

# # Application Streamlit
# st.title('Générateur d\'image à partir de texte')

# # Entrée utilisateur
# text_input = st.text_input('Entrez une description pour générer une image', '')

# if text_input:
#     # Générer l'image à partir du texte
#     with st.spinner('Génération de l\'image...'):
#         image_url = generate_image_from_text(text_input)
    
#     st.image(image_url, caption='Image générée', use_column_width=True)

# # Section d'analyse d'image
# st.subheader('Interprétez une image')

# uploaded_file = st.file_uploader("Téléchargez une image pour l'interprétation", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Affichage de l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image téléchargée", use_column_width=True)

#     # Interprétation de l'image
#     with st.spinner('Interprétation de l\'image...'):
#         interpret_image(image)


# import streamlit as st
# import openai
# from PIL import Image
# import io
# from dotenv import load_dotenv
# import os

# # Charger les variables d'environnement
# load_dotenv()

# # Configuration de l'API OpenAI
# openai.api_key = os.getenv('OPENAI_API_KEY')

# # Fonction pour générer une image à partir du texte
# def generate_image_from_text(text_prompt):
#     try:
#         # Utilisation du modèle DALL·E pour générer l'image à partir du texte
#         response = openai.Image.create(
#             prompt=text_prompt,  # Description textuelle
#             n=1,  # Nombre d'images à générer
#             size="1024x1024"  # Taille de l'image générée
#         )
#         # Récupérer l'URL de l'image générée
#         image_url = response['data'][0]['url']
#         return image_url
#     except Exception as e:
#         # Affichage d'une erreur si la génération échoue
#         return f"Une erreur s'est produite lors de la génération de l'image: {e}"

# # Fonction pour interpréter une image (démonstration)
# def interpret_image(image):
#     # Pour cette démo, on affiche simplement l'image téléchargée
#     st.image(image, caption='Image interprétée')

# # Application Streamlit
# st.title('Générateur d\'image à partir de texte')

# # Entrée utilisateur pour la description du texte
# text_input = st.text_input('Entrez une description pour générer une image', '')

# if text_input:
#     # Générer l'image à partir du texte
#     with st.spinner('Génération de l\'image...'):
#         image_url = generate_image_from_text(text_input)
    
#     if image_url:
#         st.image(image_url, caption='Image générée', use_column_width=True)

# # Section d'analyse d'image
# st.subheader('Interprétez une image')

# uploaded_file = st.file_uploader("Téléchargez une image pour l'interprétation", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Affichage de l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image téléchargée", use_column_width=True)

#     # Interprétation de l'image
#     with st.spinner('Interprétation de l\'image...'):
#         interpret_image(image)


# import streamlit as st
# import requests
# from PIL import Image
# from io import BytesIO
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement
# load_dotenv()

# # Clé d'API DeepAI (vous devez l'obtenir depuis https://deepai.org/machine-learning-model/text2img)
# DEEP_AI_API_KEY = os.getenv('DEEP_AI_API_KEY')

# # URL de l'API DeepAI pour générer une image
# DEEP_AI_URL = "https://api.deepai.org/api/text2img"

# # Fonction pour générer une image à partir du texte via l'API DeepAI
# def generate_image_from_text(text_prompt):
#     response = requests.post(
#         DEEP_AI_URL,
#         data={'text': text_prompt},
#         headers={'api-key': DEEP_AI_API_KEY}
#     )
#     if response.status_code == 200:
#         image_url = response.json()['output_url']
#         return image_url
#     else:
#         return f"Erreur: {response.status_code}, {response.text}"

# # Application Streamlit
# st.title("Générateur d'images à partir de texte avec DeepAI")

# # Entrée utilisateur pour la description du texte
# text_input = st.text_input('Entrez une description pour générer une image', '')

# if text_input:
#     # Générer l'image à partir du texte
#     with st.spinner('Génération de l\'image...'):
#         image_url = generate_image_from_text(text_input)

#     if 'Erreur' not in image_url:
#         st.image(image_url, caption="Image générée", use_column_width=True)
#     else:
#         st.error(image_url)

# # Section d'analyse d'image
# st.subheader('Interprétez une image')

# uploaded_file = st.file_uploader("Téléchargez une image pour l'interprétation", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Affichage de l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image téléchargée", use_column_width=True)


# import streamlit as st
# import requests
# from PIL import Image
# from io import BytesIO
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement
# load_dotenv()

# # Clé d'API DeepAI (vous devez l'obtenir depuis https://deepai.org/machine-learning-model/text2img)
# DEEP_AI_API_KEY = os.getenv('DEEP_AI_API_KEY')

# # URL de l'API DeepAI pour générer une image
# DEEP_AI_URL = "https://api.deepai.org/api/text2img"

# # Fonction pour générer une image à partir du texte via l'API DeepAI
# def generate_image_from_text(text_prompt):
#     if not DEEP_AI_API_KEY:
#         return "Clé API non trouvée ! Veuillez la configurer dans le fichier .env."
    
#     # Envoi de la requête POST avec l'API key dans les headers
#     response = requests.post(
#         DEEP_AI_URL,
#         data={'text': text_prompt},
#         headers={'api-key': DEEP_AI_API_KEY}
#     )
    
#     # Vérification du statut de la réponse
#     if response.status_code == 200:
#         image_url = response.json()['output_url']
#         return image_url
#     else:
#         return f"Erreur: {response.status_code}, {response.text}"

# # Application Streamlit
# st.title("Générateur d'images à partir de texte avec DeepAI")

# # Entrée utilisateur pour la description du texte
# text_input = st.text_input('Entrez une description pour générer une image', '')

# if text_input:
#     # Générer l'image à partir du texte
#     with st.spinner('Génération de l\'image...'):
#         image_url = generate_image_from_text(text_input)

#     if 'Erreur' not in image_url:
#         st.image(image_url, caption="Image générée", use_column_width=True)
#     else:
#         st.error(image_url)

# # Section d'analyse d'image
# st.subheader('Interprétez une image')

# uploaded_file = st.file_uploader("Téléchargez une image pour l'interprétation", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Affichage de l'image téléchargée
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image téléchargée", use_column_width=True)

# import streamlit as st
# import replicate
# import time
# from dotenv import load_dotenv
# import requests
# from PIL import Image
# from io import BytesIO

# load_dotenv()

# st.title("AI Image Generator")

# prompt = st.text_input("Enter a prompt for the image:")

# # Add a button to generate the image
# if st.button("Generate Image"):
#     with st.spinner('Generating image...'):
#         start_time = time.time()
#         output = replicate.run(
#             "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
#             input={
#                 "width": 1024,
#                 "height": 1024,
#                 "prompt": prompt,
#                 "refine": "expert_ensemble_refiner",
#                 "num_outputs": 1,
#                 "apply_watermark": False,
#                 "negative_prompt": "low quality, worst quality",
#                 "num_inference_steps": 25
#             }
#         )
        
#         # The output is typically a list with one or more image URLs
#         if output and len(output) > 0:
#             # Get the first image URL
#             image_url = output[0]
            
#             # Download the image
#             response = requests.get(image_url)
#             if response.status_code == 200:
#                 # Convert the image data to a format Streamlit can display
#                 image = Image.open(BytesIO(response.content))
#                 # Display the generated image
#                 st.image(image)
                
#                 end_time = time.time()
#                 elapsed_time = end_time - start_time
#                 st.write(f"Image generated in {elapsed_time:.2f} seconds")
#             else:
#                 st.error("Failed to download the generated image")
#         else:
#             st.error("No image was generated")


# import streamlit as st
# import os
# import numpy as np
# import pandas as pd
# import urllib.request
# from PIL import Image
# import glob


# def update_params():
#     st.experimental_set_query_params(challenge=st.session_state.day)


# md_files = sorted(
#     [int(x.strip("Day").strip(".md")) for x in glob.glob1("content", "*.md")]
# )

# # Logo and Navigation
# col1, col2, col3 = st.columns((1, 4, 1))
# with col2:
#     st.image(Image.open("C:/Users/Empire/Downloads/streamlit-logo-secondary-colormark-darktext.png"))
# st.markdown("# 30 Days of Streamlit en Français! 🇫🇷")

# days_list = [f"Day {x}" for x in md_files]

# query_params = st.experimental_get_query_params()

# if query_params and query_params["challenge"][0] in days_list:
#     st.session_state.day = query_params["challenge"][0]

# selected_day = st.selectbox(
#     "Choisissez votre défi 👇", days_list, key="day", on_change=update_params
# )

# with st.expander("À propos du challenge #30DaysOfStreamlit"):
#     st.markdown(
#         """

#     Le **#30DaysOfStreamlit** est un défi conçu pour vous aider à démarrer dans la création d'applications Streamlit.
    
#      Vous pourrez notamment :
#      - Configurer un environnement pour créer des apps Streamlit
#      - Créez votre première app
#      - Découvrir l'éventail des widgets à utiliser pour votre application!
#     """
#     )
#     st.write("")

# # Sidebar

# st.sidebar.header("À propos")
# st.sidebar.markdown(
#     "[Streamlit](https://streamlit.io) est une bibliothèque open source Python qui permet la création d'applications Web interactives très facilement!"
# )

# st.sidebar.header("Resources")
# st.sidebar.markdown(
#     """
# - [Documentation de Streamlit](https://docs.streamlit.io/)
# - [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
# - [Ouvrage](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
# - [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
# """
# )

# st.sidebar.header("Déploiement")
# st.sidebar.markdown(
#     "Déployez vos applications Streamlit à l'aide de [Streamlit Community Cloud](https://streamlit.io/cloud) en quelques clics!"
# )

# # Display content
# for i in days_list:
#     if selected_day == i:
#         st.markdown(f"# 🗓️ {i}")
#         j = i.replace(" ", "")
#         with open(f"content/{j}.md", "r") as f:
#             st.markdown(f.read())
#         if os.path.isfile(f"content/figures/{j}.csv") == True:
#             st.markdown("---")
#             st.markdown("### Figure #01")
#             df = pd.read_csv(f"content/figures/{j}.csv", engine="python")
#             for i in range(len(df)):
#                 st.image(f"content/images/{df.img[i]}")
#                 st.info(f"{df.figure[i]}: {df.caption[i]}")


#streamlit run app.py
import streamlit as st
import replicate
import time
from dotenv import load_dotenv

load_dotenv()

st.title("AI Image Generator")

prompt = st.text_input("Enter a prompt for the image:")

# Add a button to generate the image
if st.button("Generate Image"):
    with st.spinner('Generating image...'):
        start_time = time.time()
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": prompt,
                "refine": "expert_ensemble_refiner",
                "num_outputs": 1,
                "apply_watermark": False,
                "negative_prompt": "low quality, worst quality",
                "num_inference_steps": 25
            }
        )

        # Display the generated image
        st.image(output)
        end_time = time.time()
        elapsed_time = end_time - start_time
        st.write(f"Image generated in {elapsed_time:.2f} seconds")

# import streamlit as st
# import replicate
# import time
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement à partir du fichier .env
# load_dotenv()

# # Récupérer le token API Replicate depuis le fichier .env
# REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

# # Vérifier si le token est bien chargé
# if not REPLICATE_API_TOKEN:
#     st.error("Le token API Replicate n'a pas été trouvé. Assurez-vous qu'il est dans votre fichier .env.")
# else:
#     replicate.Client(api_token=REPLICATE_API_TOKEN)  # Authentifier le client Replicate avec le token

# def generate_image():
#     st.subheader("Generate Image")
#     prompt = st.text_input(label="Enter a prompt for the image:", key="generate_image_prompt")

#     if st.button("Generate Image", key="generate_image_button"):
#         with st.spinner("Generating image..."):
#             start_time = time.time()
            
#             try:
#                 # Effectuer l'appel à l'API Replicate pour générer l'image
#                 output = replicate.run(
#                     "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
#                     input={
#                         "width": 1024,
#                         "height": 1024,
#                         "prompt": prompt,
#                         "refine": "expert_ensemble_refiner",
#                         "num_outputs": 1,
#                         "apply_watermark": False,
#                         "negative_prompt": "low quality, worst quality",
#                         "num_inference_steps": 25
#                     }
#                 )

#                 # Afficher l'image générée
#                 st.image(output)
#                 end_time = time.time()
#                 elapsed_time = end_time - start_time
#                 st.write(f"Image generated in {elapsed_time:.2f} seconds")
#             except Exception as e:
#                 st.error(f"An error occurred: {str(e)}")
