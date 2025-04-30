import cv2
import numpy as np
import streamlit as st
from PIL import Image
import io

# Charger le classificateur de visage Haar
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fonction pour détecter les visages
def detect_faces(image):
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return faces

# Fonction pour changer la tête (collage du visage)
def change_head(source_image, target_image, source_face, target_face_position):
    # Découper la tête de la source (le visage détecté)
    x, y, w, h = source_face
    source_face_img = source_image[y:y+h, x:x+w]
    
    # Redimensionner la tête pour qu'elle corresponde à la taille du visage cible
    target_face_width = target_face_position[2]  # Largeur de la face cible
    target_face_height = target_face_position[3]  # Hauteur de la face cible
    source_face_resized = cv2.resize(source_face_img, (target_face_width, target_face_height))
    
    # Découper la zone du visage cible sur l'image cible
    x, y, w, h = target_face_position
    target_image[y:y+h, x:x+w] = source_face_resized
    
    return target_image

# Titre de l'application Streamlit
st.title('Changer la Tête des Personnes avec OpenCV')

# Téléchargement des images
uploaded_files = st.file_uploader("Téléchargez deux images (source et cible)", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Si des fichiers ont été téléchargés
if len(uploaded_files) == 2:
    # Charger l'image source (avec le visage à transférer)
    source_file = uploaded_files[0]
    target_file = uploaded_files[1]
    
    source_image = Image.open(source_file)
    target_image = Image.open(target_file)

    # Convertir les images en tableaux NumPy pour OpenCV
    source_image_cv = np.array(source_image)
    target_image_cv = np.array(target_image)
    
    # Détecter les visages dans les images
    source_faces = detect_faces(source_image_cv)
    target_faces = detect_faces(target_image_cv)
    
    # Vérifier s'il y a des visages dans les images
    if len(source_faces) > 0 and len(target_faces) > 0:
        # Prendre le premier visage détecté dans les deux images (on peut aussi ajouter une logique pour choisir)
        source_face = source_faces[0]
        target_face = target_faces[0]
        
        # Changer la tête (coller le visage de la source sur le visage de la cible)
        result_image_cv = change_head(source_image_cv, target_image_cv, source_face, target_face)
        
        # Convertir l'image résultat en format PIL pour affichage
        result_image_pil = Image.fromarray(cv2.cvtColor(result_image_cv, cv2.COLOR_BGR2RGB))
        st.image(result_image_pil, caption="Montage avec tête changée")
        
        # Sauvegarder l'image finale
        st.sidebar.subheader("Télécharger l'image modifiée")
        save_button = st.sidebar.button("Télécharger l'image modifiée")
        
        if save_button:
            # Convertir l'image modifiée en fichier pour téléchargement
            img_byte_arr = io.BytesIO()
            result_image_pil.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            st.download_button(
                label="Télécharger l'image modifiée",
                data=img_byte_arr,
                file_name="montage_tete_changee.png",
                mime="image/png"
            )
    else:
        st.warning("Aucun visage détecté dans l'une ou l'autre des images.")
