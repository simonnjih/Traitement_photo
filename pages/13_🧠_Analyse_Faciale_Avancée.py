# import cv2
# import numpy as np
# import streamlit as st
# from deepface import DeepFace
# from PIL import Image

# # Fonction pour la détection des visages avec OpenCV
# def detect_faces(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir l'image en niveaux de gris
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Détecter les visages
    
#     # Dessiner les rectangles autour des visages détectés
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
#     return image, faces

# # Fonction pour analyser les émotions avec DeepFace
# def analyze_emotions(image):
#     try:
#         # Analyser les émotions sur l'image (ici on détecte les visages et les émotions associés)
#         analysis = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
#         return analysis
#     except Exception as e:
#         return str(e)

# # Interface utilisateur avec Streamlit
# st.title('Détection de Visages et Emotions')

# uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Convertir l'image téléchargée en format OpenCV
#     image = Image.open(uploaded_file)
#     img_array = np.array(image)
#     img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
#     # Détection des visages
#     detected_image, faces = detect_faces(img_bgr)
    
#     # Convertir l'image avec les visages détectés en format PIL pour l'afficher sur Streamlit
#     detected_image_rgb = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)
#     st.image(detected_image_rgb, caption="Visage(s) détecté(s)", use_column_width=True)
    
#     if len(faces) > 0:
#         # Analyser les émotions des visages détectés
#         st.subheader("Analyse des émotions:")
#         for i, (x, y, w, h) in enumerate(faces):
#             face_image = img_bgr[y:y+h, x:x+w]
#             emotion_analysis = analyze_emotions(face_image)
            
#             if isinstance(emotion_analysis, list):  # Si plusieurs visages sont détectés
#                 for emotion in emotion_analysis:
#                     st.write(f"Visage {i+1} - Emotion: {emotion['dominant_emotion']}")
#                     st.image(face_image, caption=f"Visage {i+1}", width=150)
#                     st.write(f"Confiance: {emotion['emotions'][emotion['dominant_emotion']]:.2f}")
#             else:
#                 st.write(f"Erreur d'analyse des émotions: {emotion_analysis}")
#     else:
#         st.warning("Aucun visage détecté dans l'image.")


import cv2
import numpy as np
import streamlit as st
from deepface import DeepFace
from PIL import Image

# Fonction pour la détection des visages avec OpenCV
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir l'image en niveaux de gris
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Détecter les visages
    
    # Dessiner les rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return image, faces

# Fonction pour analyser les émotions avec DeepFace
def analyze_emotions(image):
    try:
        # Analyser les émotions sur l'image (ici on détecte les visages et les émotions associés)
        analysis = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False, detector_backend='mtcnn')
        return analysis
    except Exception as e:
        return str(e)

# Interface utilisateur avec Streamlit
# # 🎨 Mise en page
# st.set_page_config(page_title="Les Visages de l'Âme", layout="wide")
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(to right, #f6f7fb, #dee6f0);
#         }
#         .title {
#             font-size: 3em;
#             text-align: center;
#             color: #2a3d7c;
#             font-weight: bold;
#             margin-top: 40px;
#         }
#         .subtitle {
#             font-size: 1.3em;
#             color: #444;
#             text-align: center;
#             margin-bottom: 40px;
#             font-style: italic;
#         }
#         .emotion-box {
#             background-color: #ffffff;
#             border-radius: 15px;
#             padding: 25px;
#             margin-bottom: 30px;
#             box-shadow: 0px 5px 18px rgba(0,0,0,0.1);
#         }
#         .face-caption {
#             font-size: 1.1em;
#             font-weight: bold;
#             margin-top: 10px;
#             text-align: center;
#             color: #2a3d7c;
#         }
#         .emotion-key {
#             font-weight: bold;
#             color: #1a2c60;
#         }
#         .emotion-value {
#             color: #e64c4c;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # 🖼️ Titre & Description
# st.markdown('<div class="title">🎭 Les Visages de l\'Âme</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Une exploration silencieuse des émotions humaines à travers le regard de l’intelligence artificielle.</div>', unsafe_allow_html=True)

# # 📤 Upload
# uploaded_file = st.file_uploader("📷 Téléchargez une image contenant un visage", type=["jpg", "png", "jpeg"])

# if uploaded_file:
#     image = Image.open(uploaded_file).convert("RGB")
#     img_array = np.array(image)
#     img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

#     st.image(image, caption="Image originale", use_column_width=True)

#     st.markdown("### 📌 Résultat de la détection des visages")

#     detected_img, faces = detect_faces(img_bgr)
#     detected_img_rgb = cv2.cvtColor(detected_img, cv2.COLOR_BGR2RGB)
#     st.image(detected_img_rgb, caption="Visages détectés", use_column_width=True)

#     if len(faces) > 0:
#         st.markdown("### 🧠 Analyse émotionnelle des visages")
#         for i, (x, y, w, h) in enumerate(faces):
#             face_image = img_bgr[y:y+h, x:x+w]
#             emotion_result = analyze_emotions(face_image)

#             st.markdown(f'<div class="emotion-box">', unsafe_allow_html=True)
#             col1, col2 = st.columns([1, 2])
#             with col1:
#                 st.image(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB), width=150)
#                 st.markdown(f'<div class="face-caption">Visage {i+1}</div>', unsafe_allow_html=True)
#             with col2:
#                 if isinstance(emotion_result, list):
#                     emotion_data = emotion_result[0]
#                 else:
#                     emotion_data = emotion_result

#                 if isinstance(emotion_data, dict) and "dominant_emotion" in emotion_data:
#                     st.markdown(f"**Émotion dominante :** 🎯 <span class='emotion-value'>{emotion_data['dominant_emotion'].capitalize()}</span>", unsafe_allow_html=True)
#                     st.markdown("**Détails des émotions :**")
#                     for k, v in emotion_data["emotions"].items():
#                         st.markdown(f"<span class='emotion-key'>{k.capitalize()}</span> : {v:.2f}%", unsafe_allow_html=True)
#                 else:
#                     st.error("❌ Impossible d'analyser les émotions.")
#             st.markdown("</div>", unsafe_allow_html=True)
#     else:
#         st.warning("Aucun visage détecté. Essayez une autre image.")

# import cv2
# import numpy as np
# import streamlit as st
# from deepface import DeepFace
# from PIL import Image


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

# 🎨 Style CSS
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        font-weight: bold;
        color: #2a3d7c;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        color: #444;
        margin-bottom: 40px;
    }
    .emotion-key {
        font-weight: bold;
        color: #444;
    }
    .emotion-value {
        font-weight: bold;
        color: #ff4b4b;
    }
    .face-caption {
        text-align: center;
        font-size: 1.1em;
        margin-top: 5px;
        color: #555;
    }
    .story {
        font-style: italic;
        font-size: 1.2em;
        color: #3c3c3c;
        margin-bottom: 20px;
        padding: 20px;
        background-color: #f4f7f6;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 💫 Titre & Story
st.markdown('<div class="title">🎭Détection des Visages & Émotions</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Quand la machine lit les émotions humaines... 🤖❤️</div>', unsafe_allow_html=True)

st.markdown("""
<div class="story">
Chaque visage raconte une histoire. Un sourire timide, un regard intense, une larme silencieuse.
Aujourd’hui, grâce à l’IA, nous donnons à la machine la capacité de ressentir — ou du moins de reconnaître.  
Bienvenue dans un monde où vos expressions deviennent des données,  
mais où l'émotion, elle, reste infiniment humaine.
</div>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convertir l'image téléchargée en format OpenCV
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    # Détection des visages
    detected_image, faces = detect_faces(img_bgr)
    
    # Convertir l'image avec les visages détectés en format PIL pour l'afficher sur Streamlit
    detected_image_rgb = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)
    st.image(detected_image_rgb, caption="Visage(s) détecté(s)", use_column_width=True)
    
    if len(faces) > 0:
        # Analyser les émotions des visages détectés
        st.subheader("🎭Analyse des émotions:")
        for i, (x, y, w, h) in enumerate(faces):
            face_image = img_bgr[y:y+h, x:x+w]
            
            # Affichage de l'image du visage détecté pour le débogage
            st.image(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB), caption=f"Visage {i+1}", width=150)
            
            # Analyser les émotions
            emotion_analysis = analyze_emotions(face_image)
            
            # Vérification de la réponse de DeepFace
            st.write(f"Analyse pour le visage {i+1}:")
            st.write(emotion_analysis)  # Affiche l'objet retourné pour débogage
            
            if isinstance(emotion_analysis, list):  # Si plusieurs visages sont détectés
                for emotion in emotion_analysis:
                    # Vérification de la présence des clés 'emotions' et 'dominant_emotion'
                    if 'emotions' in emotion and 'dominant_emotion' in emotion:
                        st.write(f"Visage {i+1} - Emotion: {emotion['dominant_emotion']}")
                        st.write(f"Confiance: {emotion['emotions'][emotion['dominant_emotion']]:.2f}")
                    else:
                        st.write(f"emotion du visage {i+1}.{emotion['dominant_emotion']}")
            else:
                st.write(f"❌Erreur d'analyse des émotions: {emotion_analysis}")
    else:
        st.warning("😕Aucun visage détecté dans l'image.")

# import cv2
# import numpy as np
# import streamlit as st
# from deepface import DeepFace
# from PIL import Image

# # 🧠 Fonctions
# def detect_faces(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 153, 255), 2)
#     return image, faces

# def analyze_emotions(image):
#     try:
#         analysis = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False, detector_backend='mtcnn')
#         return analysis
#     except Exception as e:
#         return str(e)

# # 🎨 Mise en page
# st.set_page_config(page_title="Les Visages de l'Âme", layout="wide")
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(to right, #f6f7fb, #dee6f0);
#         }
#         .title {
#             font-size: 3em;
#             text-align: center;
#             color: #2a3d7c;
#             font-weight: bold;
#             margin-top: 40px;
#         }
#         .subtitle {
#             font-size: 1.3em;
#             color: #444;
#             text-align: center;
#             margin-bottom: 40px;
#             font-style: italic;
#         }
#         .emotion-box {
#             background-color: #ffffff;
#             border-radius: 15px;
#             padding: 25px;
#             margin-bottom: 30px;
#             box-shadow: 0px 5px 18px rgba(0,0,0,0.1);
#         }
#         .face-caption {
#             font-size: 1.1em;
#             font-weight: bold;
#             margin-top: 10px;
#             text-align: center;
#             color: #2a3d7c;
#         }
#         .emotion-key {
#             font-weight: bold;
#             color: #1a2c60;
#         }
#         .emotion-value {
#             color: #e64c4c;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # 🖼️ Titre & Description
# st.markdown('<div class="title">🎭 Les Visages de l\'Âme</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Une exploration silencieuse des émotions humaines à travers le regard de l’intelligence artificielle.</div>', unsafe_allow_html=True)

# # 📤 Upload
# uploaded_file = st.file_uploader("📷 Téléchargez une image contenant un visage", type=["jpg", "png", "jpeg"])

# if uploaded_file:
#     image = Image.open(uploaded_file).convert("RGB")
#     img_array = np.array(image)
#     img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

#     st.image(image, caption="Image originale", use_column_width=True)

#     st.markdown("### 📌 Résultat de la détection des visages")

#     detected_img, faces = detect_faces(img_bgr)
#     detected_img_rgb = cv2.cvtColor(detected_img, cv2.COLOR_BGR2RGB)
#     st.image(detected_img_rgb, caption="Visages détectés", use_column_width=True)

#     if len(faces) > 0:
#         st.markdown("### 🧠 Analyse émotionnelle des visages")
#         for i, (x, y, w, h) in enumerate(faces):
#             face_image = img_bgr[y:y+h, x:x+w]
#             emotion_result = analyze_emotions(face_image)

#             st.markdown(f'<div class="emotion-box">', unsafe_allow_html=True)
#             col1, col2 = st.columns([1, 2])
#             with col1:
#                 st.image(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB), width=150)
#                 st.markdown(f'<div class="face-caption">Visage {i+1}</div>', unsafe_allow_html=True)
#             with col2:
#                 if isinstance(emotion_result, list):
#                     emotion_data = emotion_result[0]
#                 else:
#                     emotion_data = emotion_result

#                 if isinstance(emotion_data, dict) and "dominant_emotion" in emotion_data:
#                     st.markdown(f"**Émotion dominante :** 🎯 <span class='emotion-value'>{emotion_data['dominant_emotion'].capitalize()}</span>", unsafe_allow_html=True)
#                     st.markdown("**Détails des émotions :**")
#                     for k, v in emotion_data["emotions"].items():
#                         st.markdown(f"<span class='emotion-key'>{k.capitalize()}</span> : {v:.2f}%", unsafe_allow_html=True)
#                 else:
#                     st.error("❌ Impossible d'analyser les émotions.")
#             st.markdown("</div>", unsafe_allow_html=True)
#     else:
#         st.warning("Aucun visage détecté. Essayez une autre image.")

# import cv2
# import numpy as np
# import streamlit as st
# from deepface import DeepFace
# from PIL import Image

# # 🎨 Style CSS
# st.markdown("""
#     <style>
#     .title {
#         font-size: 3em;
#         font-weight: bold;
#         color: #2a3d7c;
#         text-align: center;
#         margin-bottom: 10px;
#     }
#     .subtitle {
#         font-size: 1.5em;
#         text-align: center;
#         color: #444;
#         margin-bottom: 40px;
#     }
#     .emotion-key {
#         font-weight: bold;
#         color: #444;
#     }
#     .emotion-value {
#         font-weight: bold;
#         color: #ff4b4b;
#     }
#     .face-caption {
#         text-align: center;
#         font-size: 1.1em;
#         margin-top: 5px;
#         color: #555;
#     }
#     .story {
#         font-style: italic;
#         font-size: 1.2em;
#         color: #3c3c3c;
#         margin-bottom: 20px;
#         padding: 20px;
#         background-color: #f4f7f6;
#         border-radius: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # 💫 Titre & Story
# st.markdown('<div class="title">Détection des Visages & Émotions</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Quand la machine lit les émotions humaines... 🤖❤️</div>', unsafe_allow_html=True)

# st.markdown("""
# <div class="story">
# Chaque visage raconte une histoire. Un sourire timide, un regard intense, une larme silencieuse.
# Aujourd’hui, grâce à l’IA, nous donnons à la machine la capacité de ressentir — ou du moins de reconnaître.  
# Bienvenue dans un monde où vos expressions deviennent des données,  
# mais où l'émotion, elle, reste infiniment humaine.
# </div>
# """, unsafe_allow_html=True)

# # 📷 Uploader l’image
# uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

# # 🔎 Fonctions
# def detect_faces(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     return image, faces

# def analyze_emotions(image):
#     try:
#         result = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False, detector_backend='mtcnn')
#         if isinstance(result, list) and len(result) > 0:
#             return result[0]
#         return result
#     except Exception as e:
#         return {"error": str(e)}

# # 🚀 App Logic
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     img_array = np.array(image)
#     img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

#     st.subheader("🧠 Analyse en cours...")
#     detected_image, faces = detect_faces(img_bgr)
#     detected_image_rgb = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)
#     st.image(detected_image_rgb, caption="Image avec visage(s) détecté(s)", use_column_width=True)

#     if len(faces) > 0:
#         st.markdown("---")
#         st.subheader("🎭 Émotions détectées")

#         for i, (x, y, w, h) in enumerate(faces):
#             face_image = img_bgr[y:y+h, x:x+w]
#             st.image(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB), caption=f"Visage {i+1}", width=150)

#             with st.spinner(f"Analyse du visage {i+1}..."):
#                 emotion_result = analyze_emotions(face_image)

#                 if isinstance(emotion_result, dict) and "dominant_emotion" in emotion_result and "emotions" in emotion_result:
#                     dominant = emotion_result['dominant_emotion'].capitalize()
#                     confidence = emotion_result['emotions'][emotion_result['dominant_emotion']]
                    
#                     st.markdown(f"**Émotion dominante :** 🎯 <span class='emotion-value'>{dominant}</span>", unsafe_allow_html=True)
#                     st.markdown("**Détails des émotions :**")
#                     for k, v in emotion_result["emotions"].items():
#                         st.markdown(f"<span class='emotion-key'>{k.capitalize()}</span> : {v:.2f}%", unsafe_allow_html=True)
#                 elif "error" in emotion_result:
#                     st.error(f"Erreur : {emotion_result['error']}")
#                 else:
#                     st.warning("❌ Émotion non détectée.")
#     else:
#         st.warning("😕 Aucun visage détecté dans cette image.")
