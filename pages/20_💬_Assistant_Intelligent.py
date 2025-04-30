# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2
# from PIL import Image
# import io

# # Fonction pour afficher les formules mathématiques en LaTeX
# def display_latex(latex_code):
#     st.latex(latex_code)

# # Titre de l'application
# st.title("Traitement d'Image avec des Formules Mathématiques")

# # Introduction
# st.header("Introduction")
# st.write("""
# Le traitement d'image implique une série de transformations mathématiques appliquées à une image dans le but de l'améliorer ou d'en extraire des informations. Ces transformations peuvent inclure des opérations de filtrage, de transformation géométrique, de correction de couleur, et bien d'autres. 

# Dans ce Chatpot, nous allons explorer ces transformations avec des équations mathématiques et leur application à des images.
# """)


# # 1. Transformation de l'intensité lumineuse : Ajustement de la luminosité
# st.header("1. Ajustement de la luminosité")
# st.write("""
# Une des transformations les plus simples consiste à ajuster la luminosité d'une image. Cela peut être accompli en ajoutant une constante à toutes les valeurs de pixel de l'image. 

# Mathématiquement, cette transformation peut être représentée par :
# """)
# display_latex(r"I(x, y) = I_0(x, y) + c")
# st.write("""
# où \( I_0(x, y) \) est l'intensité du pixel à la position \((x, y)\), et \(c\) est la constante ajoutée, qui contrôle la luminosité.

# Un ajustement positif de \(c\) augmentera la luminosité, tandis qu'un ajustement négatif la réduira.
# """)

# # 2. Filtrage spatial : Flou gaussien
# st.header("2. Flou Gaussien")
# st.write("""
# Le flou gaussien est une transformation couramment utilisée dans le traitement d'image pour réduire le bruit et les détails fins de l'image. Le flou gaussien est effectué en convoluant l'image avec un noyau gaussien.

# La formule mathématique pour une convolution avec un noyau gaussien est donnée par :
# """)
# display_latex(r"I'(x, y) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} G(i, j) \cdot I(x-i, y-j)")
# st.write("""
# où \( I(x, y) \) est l'intensité de l'image à la position \((x, y)\), \( G(i, j) \) est le noyau gaussien de taille \( (2k+1) \times (2k+1) \), et \( I'(x, y) \) est l'intensité de l'image filtrée. 

# Le noyau gaussien \( G(i, j) \) est défini par :
# """)
# display_latex(r"G(i, j) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{i^2 + j^2}{2\sigma^2}\right)")
# st.write("""
# où \( \sigma \) est l'écart-type qui détermine l'intensité du flou.
# """)

# # 3. Transformation géométrique : Rotation
# st.header("3. Rotation de l'image")
# st.write("""
# La rotation d'une image implique une transformation géométrique qui modifie l'orientation de l'image dans l'espace. La formule de rotation d'une image autour de l'origine est donnée par :
# """)
# display_latex(r"X' = X \cdot \cos(\theta) - Y \cdot \sin(\theta)")
# display_latex(r"Y' = X \cdot \sin(\theta) + Y \cdot \cos(\theta)")
# st.write("""
# où \( (X, Y) \) sont les coordonnées du pixel avant la rotation, \( (X', Y') \) sont les coordonnées du pixel après la rotation, et \( \theta \) est l'angle de rotation en radians.

# Une rotation de l'image est souvent réalisée en appliquant cette transformation sur chaque pixel de l'image.
# """)

# # 4. Correction de couleur : Transformation RGB vers HSV
# st.header("4. Transformation RGB vers HSV")
# st.write("""
# La transformation d'une image du modèle de couleur RGB (Rouge, Vert, Bleu) vers le modèle HSV (Teinte, Saturation, Valeur) est courante dans les applications de traitement d'image. Les formules de conversion sont les suivantes :
# """)
# display_latex(r"H = \text{arctan}\left(\frac{\sqrt{3}(G-B)}{2R - G - B}\right)")
# display_latex(r"S = \frac{\text{max}(R, G, B) - \text{min}(R, G, B)}{\text{max}(R, G, B)}")
# display_latex(r"V = \text{max}(R, G, B)")
# st.write("""
# où \( R \), \( G \), et \( B \) sont les valeurs des pixels dans le modèle RGB, et \( H \), \( S \), \( V \) sont les valeurs correspondantes dans le modèle HSV.
# """)

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2
# from PIL import Image
# import io

# # --- CONFIGURATION DE LA PAGE ---
# st.set_page_config(page_title="Traitement d'Image et Mathématiques", page_icon="🎨", layout="centered")

# # --- CSS et style de la page ---
# st.markdown("""
#     <style>
#         body {
#             background-color: #f0f4f8;  /* Couleur de fond douce et apaisante */
#             font-family: 'Arial', sans-serif;
#             margin: 0;
#             padding: 0;
#         }

#         h1 {
#             color: #3B82F6;  /* Bleu vibrant pour le titre */
#             font-size: 40px;
#             text-align: center;
#             font-weight: bold;
#             margin-top: 50px;
#         }

#         h2 {
#             color: #1F2937;  /* Gris foncé pour les sous-titres */
#             font-size: 28px;
#             text-align: center;
#             font-weight: 600;
#             margin-top: 30px;
#         }

#         p {
#             font-size: 18px;
#             text-align: center;
#             color: #4B5563;
#             margin-top: 10px;
#             line-height: 1.6;
#         }

#         .button {
#             display: block;
#             width: 200px;
#             margin: 40px auto;
#             padding: 12px 0;
#             text-align: center;
#             background-color: #3B82F6;
#             color: white;
#             font-size: 18px;
#             border-radius: 5px;
#             border: none;
#             cursor: pointer;
#             transition: background-color 0.3s, transform 0.2s;
#         }

#         .button:hover {
#             background-color: #2563EB;
#             transform: scale(1.05);
#         }

#         .uploaded-image {
#             display: block;
#             margin: 20px auto;
#             width: 80%;
#             max-width: 600px;
#         }

#         .img-container {
#             text-align: center;
#             margin-top: 30px;
#         }

#         /* Animation de fade-in pour l'apparition de l'image transformée */
#         @keyframes fadeIn {
#             from { opacity: 0; }
#             to { opacity: 1; }
#         }

#         .fade-in {
#             animation: fadeIn 1s ease-in;
#         }

#     </style>
# """, unsafe_allow_html=True)

# # Fonction pour afficher les formules mathématiques en LaTeX
# def display_latex(latex_code):
#     st.latex(latex_code)

# # Fonction pour afficher l'image avec matplotlib
# def display_image(image):
#     plt.figure(figsize=(8, 8))
#     plt.imshow(image, cmap="gray")
#     plt.axis('off')  # Enlever les axes pour une meilleure présentation
#     st.pyplot(plt)

# # Titre de l'application
# st.title("✨ Traitement d'Image avec des Formules Mathématiques ✨")

# # Introduction
# st.header("Introduction")
# st.write("""
# Le traitement d'image implique une série de transformations mathématiques appliquées à une image dans le but de l'améliorer ou d'en extraire des informations. Ces transformations peuvent inclure des opérations de filtrage, de transformation géométrique, de correction de couleur, et bien d'autres. 

# Dans ce Chatpot, nous allons explorer ces transformations avec des équations mathématiques et leur application à des images. C'est une belle opportunité pour apprendre comment la technologie peut transformer les images tout en utilisant des concepts mathématiques.
# """)

# # 1. Transformation de l'intensité lumineuse : Ajustement de la luminosité
# st.header("1. Ajustement de la luminosité")
# st.write("""
# Une des transformations les plus simples consiste à ajuster la luminosité d'une image. Cela peut être accompli en ajoutant une constante à toutes les valeurs de pixel de l'image. 

# Mathématiquement, cette transformation peut être représentée par :
# """)
# display_latex(r"I(x, y) = I_0(x, y) + c")
# st.write("""
# où \( I_0(x, y) \) est l'intensité du pixel à la position \((x, y)\), et \(c\) est la constante ajoutée, qui contrôle la luminosité.

# Un ajustement positif de \(c\) augmentera la luminosité, tandis qu'un ajustement négatif la réduira.
# """)

# # Téléchargez une image pour tester l'ajustement de la luminosité
# uploaded_image = st.file_uploader("Téléchargez une image pour ajuster la luminosité", type=["jpg", "png", "jpeg"])

# if uploaded_image is not None:
#     image = Image.open(uploaded_image)
#     st.image(image, caption="Image originale", use_column_width=True)

#     # Ajuster la luminosité
#     image_np = np.array(image)
#     c = st.slider("Réglez la luminosité (c)", min_value=-100, max_value=100, value=30)
#     adjusted_image = np.clip(image_np + c, 0, 255)
#     st.subheader(f"Image avec luminosité ajustée de {c}")
#     display_image(adjusted_image)

# # 2. Filtrage spatial : Flou gaussien
# st.header("2. Flou Gaussien")
# st.write("""
# Le flou gaussien est une transformation couramment utilisée dans le traitement d'image pour réduire le bruit et les détails fins de l'image. Le flou gaussien est effectué en convoluant l'image avec un noyau gaussien.

# La formule mathématique pour une convolution avec un noyau gaussien est donnée par :
# """)
# display_latex(r"I'(x, y) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} G(i, j) \cdot I(x-i, y-j)")
# st.write("""
# où \( I(x, y) \) est l'intensité de l'image à la position \((x, y)\), \( G(i, j) \) est le noyau gaussien de taille \( (2k+1) \times (2k+1) \), et \( I'(x, y) \) est l'intensité de l'image filtrée. 

# Le noyau gaussien \( G(i, j) \) est défini par :
# """)
# display_latex(r"G(i, j) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{i^2 + j^2}{2\sigma^2}\right)")
# st.write("""
# où \( \sigma \) est l'écart-type qui détermine l'intensité du flou.
# """)

# # 3. Transformation géométrique : Rotation
# st.header("3. Rotation de l'image")
# st.write("""
# La rotation d'une image implique une transformation géométrique qui modifie l'orientation de l'image dans l'espace. La formule de rotation d'une image autour de l'origine est donnée par :
# """)
# display_latex(r"X' = X \cdot \cos(\theta) - Y \cdot \sin(\theta)")
# display_latex(r"Y' = X \cdot \sin(\theta) + Y \cdot \cos(\theta)")
# st.write("""
# où \( (X, Y) \) sont les coordonnées du pixel avant la rotation, \( (X', Y') \) sont les coordonnées du pixel après la rotation, et \( \theta \) est l'angle de rotation en radians.

# Une rotation de l'image est souvent réalisée en appliquant cette transformation sur chaque pixel de l'image.
# """)

# # 4. Correction de couleur : Transformation RGB vers HSV
# st.header("4. Transformation RGB vers HSV")
# st.write("""
# La transformation d'une image du modèle de couleur RGB (Rouge, Vert, Bleu) vers le modèle HSV (Teinte, Saturation, Valeur) est courante dans les applications de traitement d'image. Les formules de conversion sont les suivantes :
# """)
# display_latex(r"H = \text{arctan}\left(\frac{\sqrt{3}(G-B)}{2R - G - B}\right)")
# display_latex(r"S = \frac{\text{max}(R, G, B) - \text{min}(R, G, B)}{\text{max}(R, G, B)}")
# display_latex(r"V = \text{max}(R, G, B)")
# st.write("""
# où \( R \), \( G \), et \( B \) sont les valeurs des pixels dans le modèle RGB, et \( H \), \( S \), \( V \) sont les valeurs correspondantes dans le modèle HSV.
# """)

# # Bouton interactif
# st.markdown('<a href="https://www.example.com" class="button">En savoir plus sur le traitement d\'image</a>', unsafe_allow_html=True)

import streamlit as st
import numpy as np
import cv2



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
# --- STYLE PERSONNALISÉ POUR LE CHATBOT ---
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(135deg, #f4f7f6, #c1d3e0);
        padding: 0;
        margin: 0;
    }

    .header {
        text-align: center;
        color: #fff;
        font-size: 3em;
        font-weight: bold;
        background-color: #2a3d7c;
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.3);
        margin-top: 50px;
    }

    .subheader {
        font-size: 1.8em;
        color: #2a3d7c;
        text-align: center;
        margin-top: 20px;
    }

    .chat-box {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: 40px auto;
        height: 500px;
        overflow-y: auto;
    }

    .chat-box p {
        font-size: 1.1em;
        color: #333;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
    }

    .user-message {
        background-color: #2a3d7c;
        color: white;
        text-align: right;
        margin-left: 50px;
    }

    .bot-message {
        background-color: #f4f7f6;
        color: #333;
        text-align: left;
        margin-right: 50px;
    }

    .input-container {
        display: flex;
        justify-content: center;
        padding: 20px;
    }

    .input-container input {
        width: 70%;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1.2em;
        margin-right: 10px;
    }

    .input-container button {
        background-color: #2a3d7c;
        color: white;
        padding: 12px 25px;
        border-radius: 5px;
        font-size: 1.2em;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .input-container button:hover {
        background-color: #1a2b55;
    }

    .footer {
        text-align: center;
        font-size: 1em;
        color: #555;
        padding: 20px;
        background-color: #2a3d7c;
        color: white;
        margin-top: 30px;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    .fade-in {
        animation: fadeIn 1.5s ease-in;
    }

    </style>
""", unsafe_allow_html=True)

# --- Ajout du titre et de l'introduction ---
st.markdown('<div class="header fade-in">Bienvenue dans votre Chatbot de Traitement d\'Image</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="subheader fade-in">Posez vos questions sur le traitement d'image et apprenez les concepts avancés !</div>
""", unsafe_allow_html=True)

# --- Section de conversation ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Fonction pour ajouter un message de l'utilisateur et du bot
def add_message(sender, message):
    st.session_state["messages"].append({"sender": sender, "message": message})

# Fonction pour répondre avec des concepts de traitement d'image
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "convolution" in user_input:
        return """
        La convolution est une opération fondamentale en traitement d'image. Elle consiste à appliquer un noyau (ou filtre) sur une image. 
        L'équation mathématique de la convolution est :
        
        \\[
        I'(x, y) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} G(i, j) \cdot I(x-i, y-j)
        \\]
        
        Où \\( I(x, y) \\) est l'intensité de l'image à la position \\( (x, y) \\), et \\( G(i, j) \\) est le noyau gaussien appliqué.
        """
    elif "flou gaussien" in user_input:
        return """
        Le flou gaussien est une forme de lissage qui aide à réduire le bruit dans les images. Le noyau utilisé pour le flou gaussien est une fonction gaussienne.
        L'équation de la fonction gaussienne est :
        
        \\[
        G(i, j) = \\frac{1}{2\\pi\\sigma^2} \\exp\\left(-\\frac{i^2 + j^2}{2\\sigma^2}\\right)
        \\]
        
        Où \\( \\sigma \\) est l'écart-type et détermine l'intensité du flou appliqué.
        """
    elif "transformation" in user_input and "rgb" in user_input:
        return """
        La transformation RGB vers HSV est utilisée pour passer d'un modèle de couleur RGB (Rouge, Vert, Bleu) à HSV (Teinte, Saturation, Valeur). 
        Voici les formules de conversion :
        
        \\[
        H = \\text{arctan}\\left(\\frac{\\sqrt{3}(G-B)}{2R - G - B}\\right)
        \\]
        \\[
        S = \\frac{\\text{max}(R, G, B) - \\text{min}(R, G, B)}{\\text{max}(R, G, B)}
        \\]
        \\[
        V = \\text{max}(R, G, B)
        \\]
        
        Où \\( R, G, B \\) sont les valeurs des pixels dans le modèle RGB, et \\( H, S, V \\) sont les valeurs correspondantes dans le modèle HSV.
        """
    else:
        return "Désolé, je ne comprends pas cette question. Essayez de poser une question sur la convolution, le flou gaussien, ou les transformations d'images."

# Afficher les messages
def display_chat():
    for msg in st.session_state["messages"]:
        if msg["sender"] == "user":
            st.markdown(f'<p class="user-message fade-in">{msg["message"]}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="bot-message fade-in">{msg["message"]}</p>', unsafe_allow_html=True)

display_chat()

# --- Zone de saisie ---
with st.form(key="input_form", clear_on_submit=True):
    user_input = st.text_input("Votre question sur le traitement d'image :", "", max_chars=200)
    submit_button = st.form_submit_button(label="Envoyer")

    if submit_button and user_input:
        add_message("user", user_input)
        # Réponse du chatbot (avec logique de traitement d'image)
        bot_response = get_bot_response(user_input)
        add_message("bot", bot_response)
        display_chat()

# --- Footer ---
st.markdown("""
    <div class="footer">
    <a href="https://openai.com" style="color: #fff;">OpenAI</a>
    </div>
""", unsafe_allow_html=True)

