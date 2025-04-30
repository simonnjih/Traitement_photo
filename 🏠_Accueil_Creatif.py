import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Multipage App",
    page_icon="🧊"
)
    #choice=st.sidebar.radio("Faite un choix de fonctionalité:", ["About the my application", "IA_generation", "reconstutuer une image", "améliorer le contraste", "Autre"])

#st.logo("D:\DTI\logoia.png")
#st.title("Home of Image")
st.sidebar.success("Select a page about")
#choice=st.sidebar.radio("",["About the my application", "IA_generation", "reconstutuer une image", "améliorer le contraste", "Autre"])
import streamlit as st


st.markdown("""
    <style>
    /* Masquer le bouton View less/View more */
    [data-testid="stSidebarNav"] button {
        display: none;
    }

    /* Ajouter notre propre texte stylisé */
    .custom-toggle {
        font-size: 0.9rem;
        color: #6c63ff;
        text-align: center;
        margin-top: 10px;
    }
    </style>

""", unsafe_allow_html=True)

# Style personnalisé pour la sidebar
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

# Style personnalisé pour la page d'accueil
st.markdown("""
    <style>
    /* Style global */
    .header {
        text-align: center;
        color: #fff;
        font-size: 3.5em;
        font-weight: bold;
        background-color: #2a3d7c;
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
    }
    .subheader {
        font-size: 1.8em;
        color: #fff;
        text-align: center;
    }
    .intro-text {
        font-size: 1.4em;
        color: #333;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        line-height: 1.6;
    }
    .feature-card {
        background-color: #f4f7f6;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        margin: 15px;
        transition: transform 0.3s ease-in-out;
    }
    .feature-card:hover {
        transform: translateY(-10px);
    }
    .feature-card h4 {
        color: #2a3d7c;
        font-size: 1.4em;
    }
    .feature-card p {
        color: #555;
        font-size: 1.1em;
    }
    .button {
        background-color: #2a3d7c;
        color: white;
        padding: 18px 35px;
        font-size: 1.2em;
        border-radius: 7px;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #1a2b55;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 250px;
        margin-top: 30px;
    }
    .video-container {
        margin-top: 40px;
        display: flex;
        justify-content: center;
    }
    .video-container iframe {
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
        max-width: 80%;
        height: 500px;
    }
    /* Dégradé d'arrière-plan */
    .background {
        background: linear-gradient(135deg, #f4f7f6, #c1d3e0);
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Ajouter le logo (assurez-vous de télécharger l'image "logo.png" dans votre projet)
#st.image("logoia.png", use_column_width=False, width=250, caption="Maths and AI for Science", output_format="PNG")

# Ajouter un titre et une image de fond
st.markdown('<div class="header">Bienvenue dans le Traitement d\'Image Avancé</div>', unsafe_allow_html=True)

# Ajout d'une introduction
st.markdown("""
    <div class="intro-text">
    Découvrez un monde où la science, les mathématiques et l'IA se rencontrent pour repousser les frontières du traitement d'images. Transformez vos images en œuvres d'art grâce à des algorithmes puissants.
    </div>
""", unsafe_allow_html=True)

# Section de vidéo
st.markdown("""
    <div class="subheader">Regardez la magie en action</div>
""", unsafe_allow_html=True)




# Section des fonctionnalités
st.markdown('<div class="subheader">Fonctionnalités principales</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
        <h4>Amélioration des images</h4>
        <p>Boostez la qualité de vos photos en quelques secondes avec des filtres et des techniques d'amélioration visuelle avancées.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
        <h4>Analyse d'images</h4>
        <p>Détectez les objets, les visages, ou même les émotions grâce à notre système d'intelligence artificielle intégré.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
        <h4>Effets spéciaux</h4>
        <p>Transformez vos images avec des effets créatifs uniques pour des rendus spectaculaires.</p>
        </div>
    """, unsafe_allow_html=True)




