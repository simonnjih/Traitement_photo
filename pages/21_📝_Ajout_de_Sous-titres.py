import streamlit as st
from groq import Groq
import base64
import os
import json

# Set up Groq API Key
os.environ['GROQ_API_KEY'] = json.load(open('credentials.json', 'r'))['groq_token']

# Function to encode the image
def encode_image(image_path):
   with open(image_path, "rb") as image_file:
       return base64.b64encode(image_file.read()).decode('utf-8')
   

# Function to generate caption
def generate_caption(uploaded_image):
   base64_image = base64.b64encode(uploaded_image.read()).decode('utf-8')
   client = Groq()
   chat_completion = client.chat.completions.create(
       messages=[
           {
               "role": "user",
               "content": [
                   {"type": "text", "text": "What's in this image?"},
                   {
                       "type": "image_url",
                       "image_url": {
                           "url": f"data:image/jpeg;base64,{base64_image}",
                       },
                   },
               ],
           }
       ],
       model="llama-3.2-90b-vision-preview",
   )
   return chat_completion.choices[0].message.content

# Streamlit App
st.title("Llama Captioner")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
   # Show the uploaded image
   st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

   if st.button("Generate Caption"):
       with st.spinner("Generating caption..."):
           caption = generate_caption(uploaded_file)
       st.success("Caption Generated!")
       st.write("**Caption:**", caption)

#        st.sidebar.radio("📂 Modules disponibles", [
#     "🏠 Accueil Créatif",
#     "ℹ️ À propos de l’application",
#     "🎥 Studio Photo & Vidéo",
#     "✨ Contraste Éclatant",
#     "🤖 Génération par l’IA",
#     "🧩 Reconstruction Magique",
#     "📸 Séance Photo Émotionnelle",
#     "👤 À propos de moi",
#     "🧓 Rajeunir ou Vieillir",
#     "🔄 Changer de Visage",
#     "💬 Assistant Intelligent",
#     "💇 Style Capillaire (IA)",
#     "📈 Ajustement de Courbes",
#     "🧠 Analyse Faciale Avancée",
#     "🖍️ Éditeur d’Image",
#     "🖼️ Image 2D Classique",
#     "🧊 Image 3D Immersive",
#     "🎞️ Montage Créatif",
#     "🔍 Amélioration de Netteté",
#     "📝 Ajout de Sous-titres",
#     "🚗 Transformation Véhicule",
#     "🚀 Détection Avancée (Yolox V5)",
#     "🌈 Explorations Créatives",
#     "🔽 Réduire le menu"
# ])
