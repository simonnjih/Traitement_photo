# import streamlit as st
# from PIL import Image, ImageDraw

# def contact_form():
#     with st.form("contact_form"):
#         name=st.text_input("first Name")
#         email=st.text_input("Email Adress")
#         message=st.text_area("Your message")
#         submit_button=st.form_submit_button("Submit")

#         if submit_button:
#             st.success("Message successfully sent!")
            

# @st.dialog("Contact Me")
# def show_contact_form():
#     contact_form()
    
 
# # --- HERO SECTION ---

# col1, col2=st.columns(2, gap="small", vertical_alignment="center")
# with col1:
#     # Ouvrir l'image
#     image_path = 'D:\DTI\me.jpg'  # Assurez-vous que le chemin est correct
#     image = Image.open(image_path)

# # Créer une image de masque circulaire (l'image originale doit être carrée)
#     width, height = image.size
#     mask = Image.new("L", (width, height), 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, width, height), fill=255)

# # Appliquer le masque à l'image
#     image.putalpha(mask)  # Ajoute la transparence en fonction du masque
#     st.image(image, width=230) 
# with col2:
#     st.title("Elisé", anchor=False)
#     st.write("Architech deeplearning, Math and AI for Science")
#     if st.button("Contact Me"):
#         show_contact_form()



# # ---EXPRERIENCE ET QUALIFICATIONS ---
# st.write("\n")
# st.subheader("COMPETENCES", anchor=False)
# st.write(
#     """
#       -Excellente compétence en mathématique: Polynome orthogonaux, optimisation differential,Différenciation Automatique.\n
#       -EXcellente base en: Python, DotNET, Latex, R, SOlidword, Autocard, Matlab.\n
#       -Excellent Niveau:Tensorflow, pytorch.\n
#       -Compétance Technologie:bigdata, Datamining,Vision par ordinateur, traitement d'image avancer.\n
#       -Interet:Phylosophy, Physique, Football.   
# """
# )
import streamlit as st
from PIL import Image, ImageDraw
import time


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
# --- STYLE CSS AVANCÉ ---
st.markdown("""
    <style>
        body {
            background-color: #F5F6FA;  /* Couleur de fond claire et apaisante */
            font-family: 'Roboto', sans-serif;  /* Police moderne de Google */
            margin: 0;
            padding: 0;
        }

        /* Hero Section - Section principale avec image et texte */
        .hero-section {
            background-color: #ffffff;
            border-radius: 20px;
            padding: 60px 40px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .hero-title {
            font-size: 48px;
            font-weight: 700;
            color: #1F2937;  /* Gris foncé pour un texte très visible */
        }

        .hero-description {
            font-size: 24px;
            color: #4B5563;  /* Gris clair pour le texte secondaire */
            margin-top: 10px;
        }

        .contact-button {
            background-color: #3B82F6;  /* Bleu vif pour l'accent */
            color: white;
            padding: 12px 30px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s, transform 0.2s ease-in-out;
            margin-top: 20px;
        }

        .contact-button:hover {
            background-color: #2563EB;
            transform: translateY(-3px);  /* Effet de survol : bouton qui s'élève */
        }

        /* Formulaire de contact - Formulaire avec un fond doux et des champs élégants */
        .form-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        .form-title {
            font-size: 30px;
            font-weight: 600;
            color: #1F2937;
            margin-bottom: 20px;
        }

        .form-input {
            margin-bottom: 20px;
        }

        .form-submit {
            background-color: #34D399;  /* Vert doux pour la soumission */
            color: white;
            padding: 12px 30px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s;
        }

        .form-submit:hover {
            background-color: #10B981;
        }

        /* Section Compétences */
        .skills-section {
            background-color: #ffffff;
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            margin-top: 40px;
        }

        .skills-title {
            font-size: 32px;
            font-weight: 700;
            color: #1F2937;
            margin-bottom: 25px;
        }

        .skills-list {
            font-size: 18px;
            color: #4B5563;
            line-height: 1.8;
        }

        .skills-list span {
            color: #3B82F6;  /* Bleu pour les mots-clés importants */
        }

        /* Animation d'apparition du titre */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .fade-in {
            animation: fadeIn 1s ease-out;
        }

        /* Animation de pulsation pour les icônes */
        @keyframes pulse {
            0% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.1); opacity: 0.8; }
            100% { transform: scale(1); opacity: 1; }
        }

        .pulse-icon:hover {
            animation: pulse 1.5s infinite;  /* Animation de pulsation pour attirer l'attention */
        }

        /* Barre de progression animée */
        .progress-bar {
            width: 100%;
            height: 15px;
            border-radius: 10px;
            background-color: #D1D5DB;
            margin-top: 10px;
        }

        .progress-bar-fill {
            height: 100%;
            border-radius: 10px;
            background-color: #3B82F6;
        }
    </style>
""", unsafe_allow_html=True)

# --- Fonction du formulaire de contact ---
def contact_form():
    with st.form("contact_form"):
        st.text_input("First Name", key="name", placeholder="Your first name", help="Enter your first name")
        st.text_input("Email Address", key="email", placeholder="Your email address", help="Enter your email")
        st.text_area("Your Message", key="message", placeholder="Write your message here...", help="Enter your message")
        submit_button = st.form_submit_button("Submit", use_container_width=True)

        if submit_button:
            st.success("Message successfully sent!")


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- SECTION HERO ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    image_path = 'D:/DTI/me.jpg'  # Assurez-vous que le chemin est correct
    image = Image.open(image_path)

    # Créer une image de masque circulaire (l'image originale doit être carrée)
    width, height = image.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    # Appliquer le masque à l'image
    image.putalpha(mask)
    st.image(image, width=230)  # Affichage de l'image dans le cercle

with col2:
    st.markdown("<div class='hero-section fade-in'>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Elisé</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-description'>Architect in deep learning, Math, and AI for Science</p>", unsafe_allow_html=True)
    if st.button("Contact Me", key="contact_button", use_container_width=True):
        show_contact_form()
    st.markdown("</div>", unsafe_allow_html=True)


# --- COMPETENCES SECTION ---
def animated_progress_bar():
    # Créer une barre de progression animée pour chaque compétence
    skills = {
        "Python": 90,
        "Machine Learning": 85,
        "Deep Learning": 80,
        "Data Science": 75,
        "AI for Science": 70
    }

    st.subheader("Compétences")

    for skill, percentage in skills.items():
        progress_bar = st.progress(0)  # Initialisation de la barre à 0
        for i in range(percentage + 1):
            time.sleep(0.02)  # Pause pour animer la progression
            progress_bar.progress(i)  # Mise à jour de la barre de progression
        st.write(f"{skill}: {percentage}%")  # Afficher le nom et la progression

# Afficher les barres de progression animées
animated_progress_bar()


# --- SECTION COMPETENCES ---
st.markdown("<div class='skills-section fade-in'>", unsafe_allow_html=True)
st.markdown("<h2 class='skills-title'>COMPETENCES</h2>", unsafe_allow_html=True)
st.markdown(
    """
    - Excellente compétence en mathématique: Polynômes orthogonaux, optimisation différentielle, différenciation automatique.\n
    - Excellente base en: Python, DotNET, Latex, R, Solidworks, AutoCAD, Matlab.\n
    - Excellent niveau: TensorFlow, PyTorch.\n
    - Compétence Technologie: Big Data, Data Mining, Vision par ordinateur, traitement d'image avancé.\n
    - Intérêt: Philosophie, Physique, Football.
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)




