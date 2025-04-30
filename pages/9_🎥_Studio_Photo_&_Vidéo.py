# import streamlit as st
# import tensorflow as tf
# import tensorflow_hub as hub
# import numpy as np
# import imageio
# from PIL import Image
# from skimage import transform
# import io

# # Définir la taille du vecteur latent et la fonction de génération de l'image à partir du module
# latent_dim = 512

# # Charger le modèle ProGAN depuis TensorFlow Hub
# @st.cache_resource
# def load_model():
#     progan = hub.load("https://tfhub.dev/google/progan-128/1").signatures['default']
#     return progan

# progan = load_model()

# # Fonction d'interpolation entre deux vecteurs
# def interpolate_hypersphere(v1, v2, num_steps):
#     # Convertir les vecteurs en float32
#     v1 = tf.cast(v1, tf.float32)
#     v2 = tf.cast(v2, tf.float32)

#     v1_norm = tf.norm(v1)
#     v2_norm = tf.norm(v2)
#     v2_normalized = v2 * (v1_norm / v2_norm)

#     vectors = []
#     for step in range(num_steps):
#         interpolated = v1 + (v2_normalized - v1) * step / (num_steps - 1)
#         interpolated_norm = tf.norm(interpolated)
#         interpolated_normalized = interpolated * (v1_norm / interpolated_norm)
#         vectors.append(interpolated_normalized)
#     return tf.stack(vectors)

# # Affichage d'une image
# def display_image(image):
#     image = tf.constant(image)
#     image = tf.image.convert_image_dtype(image, tf.uint8)
#     return Image.fromarray(image.numpy())

# # Générer une image depuis un vecteur latent
# def get_module_space_image():
#     vector = tf.random.normal([1, latent_dim], dtype=tf.float32)  # Utilisation de float32
#     images = progan(vector)['default'][0]
#     return images

# # Fonction de téléchargement d'image par l'utilisateur
# def upload_image():
#     uploaded = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])
#     if uploaded is not None:
#         image = Image.open(uploaded)
#         image = np.array(image)
#         image_resized = transform.resize(image, [128, 128], mode='reflect')
#         return image_resized
#     return None

# # Fonction de recherche du vecteur latent le plus proche
# def find_closest_latent_vector(initial_vector, num_optimization_steps, steps_per_image, target_image):
#     images = []
#     losses = []

#     vector = tf.Variable(initial_vector, dtype=tf.float32)  # Assurez-vous que le vecteur est en float32
#     optimizer = tf.optimizers.Adam(learning_rate=0.01)
#     loss_fn = tf.losses.MeanAbsoluteError(reduction="sum")

#     for step in range(num_optimization_steps):
#         if (step % 100) == 0:
#             print()
#         print('.', end='')
#         with tf.GradientTape() as tape:
#             image = progan(vector.read_value())['default'][0]
#             if (step % steps_per_image) == 0:
#                 images.append(image.numpy())
#             target_image_difference = loss_fn(image, target_image[:,:,:3])
#             # Regularisation de la longueur du vecteur latent
#             regularizer = tf.abs(tf.norm(vector) - np.sqrt(latent_dim))

#             loss = target_image_difference + regularizer
#             losses.append(loss.numpy())
#         grads = tape.gradient(loss, [vector])
#         optimizer.apply_gradients(zip(grads, [vector]))

#     return images, losses

# # Interface Streamlit
# st.title("ProGAN: Transformation d'image via interpolation et optimisation latente")

# image_from_module_space = st.checkbox('Générer une image depuis l\'espace du module', value=True)

# if image_from_module_space:
#     target_image = get_module_space_image()
#     st.image(display_image(target_image), caption="Image générée depuis l'espace latent", use_column_width=True)
# else:
#     target_image = upload_image()
#     if target_image is not None:
#         st.image(target_image, caption="Image téléchargée", use_column_width=True)

#     if target_image is not None:
#         # Initialiser un vecteur latent aléatoire
#         initial_vector = tf.random.normal([1, latent_dim], dtype=tf.float32)  # Utilisation de float32

#         # Paramètres pour l'optimisation
#         num_optimization_steps = st.slider("Nombre d'étapes d'optimisation", 100, 500, 200)
#         steps_per_image = st.slider("Nombre d'étapes par image", 1, 10, 5)

#         st.write("Optimisation en cours...")

#         # Trouver le vecteur latent le plus proche de l'image cible
#         images, loss = find_closest_latent_vector(initial_vector, num_optimization_steps, steps_per_image, target_image)

#         # Affichage de l'animation
#         st.write("Animation générée...")
#         animate(images)

#         # Affichage du résultat final
#         st.image(np.concatenate([images[-1], target_image], axis=1), caption="Image optimisée et cible", use_column_width=True)
        
#         # Télécharger l'animation si souhaité
#         with open('./animation.gif', "rb") as f:
#             st.download_button("Télécharger l'animation", f, file_name="animation.gif")


import streamlit as st
import cv2
import numpy as np
import tempfile
import os
from PIL import Image
import io

# Configuration Streamlit
st.set_page_config(page_title="🎥 Vidéo Cartoon 3D", page_icon="🎬", layout="centered")


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
        .stApp {
            background-color: #f0f0f5;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #6d3e84;
            font-size: 2.8em;
            margin-bottom: 0.2em;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #5f4d63;
            margin-bottom: 2em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎥 Studio Cartoon Vidéo 3D</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Donnez une touche artistique à vos vidéos avec style dessin animé 3D ✨</div>', unsafe_allow_html=True)

# 📥 Upload Vidéo
video_file = st.file_uploader("🎬 Téléchargez une vidéo (max ~100MB)", type=["mp4", "mov", "avi"])

# 🎨 Fonction de cartoonisation vidéo
def cartoonize_frame(frame):
    img_bilateral = cv2.bilateralFilter(frame, 9, 75, 75)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    cartoon = cv2.bitwise_and(img_bilateral, img_bilateral, mask=edges)

    # Effet 3D
    gradient = cv2.GaussianBlur(gray, (5, 5), 0)
    gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX)
    gradient_color = cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR)
    cartoon_3d = cv2.addWeighted(cartoon, 0.85, gradient_color, 0.15, 0)

    return cartoon_3d

# 🛠️ Traitement vidéo
if video_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    cap = cv2.VideoCapture(tfile.name)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = "output_cartoon.avi"
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    st.info("⏳ Traitement en cours... cela peut prendre un moment selon la longueur de la vidéo.")

    progress_bar = st.progress(0)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_idx = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cartoon_frame = cartoonize_frame(frame)
        out.write(cartoon_frame)

        frame_idx += 1
        progress_bar.progress(min(frame_idx / frame_count, 1.0))

    cap.release()
    out.release()

    st.success("✅ Transformation terminée avec succès !")
    with open(output_path, "rb") as f:
        st.download_button(
            label="📥 Télécharger la vidéo transformée",
            data=f,
            file_name="video_cartoon_3d.avi",
            mime="video/avi"
        )
