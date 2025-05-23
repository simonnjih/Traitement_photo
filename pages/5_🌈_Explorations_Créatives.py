
import streamlit as st
st.set_page_config(page_title="Studio Émotionnel 🎨", layout="wide")

import io
import base64
import cv2
from PIL import Image
#from filters import *
import cv2
import numpy as np
import streamlit as st
from scipy.interpolate import UnivariateSpline

@st.cache_data
def bw_filter(img):
    img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    return img_gray

@st.cache_data
def vignette(img, level=2):
    height, width = img.shape[:2]

    # Generate vignette mask using Gaussian kernels.
    X_resultant_kernel = cv2.getGaussianKernel(width, width / level)
    Y_resultant_kernel = cv2.getGaussianKernel(height, height / level)

    # Generating resultant_kernel matrix.
    kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = kernel / kernel.max()

    img_vignette = np.copy(img)

    # Apply the mask to each channel in the input image.
    for i in range(3):
        img_vignette[:, :, i] = img_vignette[:, :, i] * mask

    return img_vignette

@st.cache_data
def sepia(img):
        img_sepia = img.copy()
        # Converting to RGB as sepia matrix below is for RGB.
        img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_BGR2RGB)
        img_sepia = np.array(img_sepia, dtype=np.float64)
        img_sepia = cv2.transform(img_sepia, np.matrix([[0.393, 0.769, 0.189],
                                                        [0.349, 0.686, 0.168],
                                                        [0.272, 0.534, 0.131]]))
        # Clip values to the range [0, 255].
        img_sepia = np.clip(img_sepia, 0, 255)
        img_sepia = np.array(img_sepia, dtype=np.uint8)
        img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_RGB2BGR)
        return img_sepia

@st.cache_data
def pencil_sketch(img, ksize=5):
    img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0, 0)
    img_sketch, _ = cv2.pencilSketch(img_blur)
    return img_sketch

@st.cache_data
def stylization(img, sigma_s = 10, sigma_r = 0.1):
    img_blur = cv2.GaussianBlur(img, (5,5), 0, 0)
    img_style = cv2.stylization(img_blur, sigma_s = sigma_s, sigma_r = sigma_r)
    return img_style

@st.cache_data
def blur_img(img, k=9):
    blur = cv2.GaussianBlur(img, (k,k), 0, 0)
    return blur

@st.cache_data
def sharping_filter(img, k=5):
    kernel = np.array([[ 0, -1,  0],
                       [-1,  k, -1],
                       [ 0, -1,  0]])
    img_sharp = cv2.filter2D(img, ddepth = -1, kernel = kernel)
    # Clip values to the range [0, 255].
    img_sharp = np.clip(img_sharp, 0, 255)
    return img_sharp

@st.cache_data
def HDR(img):
    img_hdr = cv2.detailEnhance(img, sigma_s = 10, sigma_r = 0.1)
    return img_hdr

@st.cache_data
def invert(img):
    img_inv = cv2.bitwise_not(img)
    return img_inv

@st.cache_data
def warm_filter(img):
    # We are giving y values for a set of x values.
    # And calculating y for [0-255] x values accordingly to the given range.
    increase_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 75, 155, 255])(range(256))

    # Similarly construct a lookuptable for decreasing pixel values.
    decrease_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 45, 95, 255])(range(256))
    # Split the blue, green, and red channel of the image.
    blue_channel, green_channel, red_channel = cv2.split(img)

    # Increase red channel intensity using the constructed lookuptable.
    red_channel = cv2.LUT(red_channel, increase_table).astype(np.uint8)

    # Decrease blue channel intensity using the constructed lookuptable.
    blue_channel = cv2.LUT(blue_channel, decrease_table).astype(np.uint8)

    # Merge the blue, green, and red channel.
    img_warm = cv2.merge((blue_channel, green_channel, red_channel))
    return img_warm

@st.cache_data
def Cold_filter(img):
    # We are giving y values for a set of x values.
    # And calculating y for [0-255] x values accordingly to the given range.
    increase_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 75, 155, 255])(range(256))

    # Similarly construct a lookuptable for decreasing pixel values.
    decrease_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 45, 95, 255])(range(256))
    # Split the blue, green, and red channel of the image.
    blue_channel, green_channel, red_channel = cv2.split(img)

    # Decrease red channel intensity using the constructed lookuptable.
    red_channel = cv2.LUT(red_channel, decrease_table).astype(np.uint8)

    # Increase blue channel intensity using the constructed lookuptable.
    blue_channel = cv2.LUT(blue_channel, increase_table).astype(np.uint8)

    # Merge the blue, green, and red channel.
    img_cold = cv2.merge((blue_channel, green_channel, red_channel))
    return img_cold

@st.cache_data
def embossed_edges(img):
    kernel = np.array([[0, -3, -3],
                       [3,  0, -3],
                       [3,  3,  0]])

    img_emboss = cv2.filter2D(img, -1, kernel=kernel)
    return img_emboss

@st.cache_data
def right_sobel(img):
    # Right Sobel Filter
    kernel = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_img = cv2.filter2D(img, -1, kernel, borderType = cv2.BORDER_REPLICATE)
    return sobel_img

@st.cache_data
def bright(img, level):
    img_bright = cv2.convertScaleAbs(img, beta = level)
    return img_bright

@st.cache_data
def outline(img, k=9):
    k = max(k, 9)
    kernel = np.array([[-1, -1, -1],
                       [-1, k, -1],
                       [-1, -1, -1]])

    img_outline = cv2.filter2D(img, ddepth=-1, kernel=kernel)
    return img_outline

# Generating a link to download a particular image file.
# @st.cache_data
def get_image_download_link(img, filename, text):
    buffered = io.BytesIO()
    img.save(buffered, format = 'JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href

# # Set title.
# st.title('Artistic Image Filters')

# # Upload image.
# uploaded_file = st.file_uploader('Choose an image file:', type=['png','jpg'])

# if uploaded_file is not None:
#     # Convert the file to an opencv image.
#     raw_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     img = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)
#     input_col, output_col = st.columns(2)
#     with input_col:
#         st.header('Original')
#         # Display uploaded image.
#         st.image(img, channels='BGR')

#     st.header('Filter Examples:')
#     # Display a selection box for choosing the filter to apply.
#     option = st.selectbox('Select a filter:',
#                           ( 'None',
#                             'Black and White',
#                             'Sepia / Vintage',
#                             'Vignette Effect',
#                             'Pencil Sketch',
#                             'Stylization',
#                             'Blur',
#                             'Sharp',
#                             'HDR',
#                             'Invert Color',
#                             'Sommer Effect',
#                             'Cold Effect',
#                             'Embossed Edges',
#                             'Right Sobel',
#                             'Brightnis',
#                             'Outline'
#                          ))

#     # Define columns for thumbnail images.
#     #col1, col2, col3, col4 = st.columns(4)
#     #with col1:
#     #    st.caption('Black and White')
#     #    st.image('filter_bw.jpg')
#     #with col2:
#     #    st.caption('Sepia / Vintage')
#     #    st.image('filter_sepia.jpg')
#     #with col3:
#     #    st.caption('Vignette Effect')
#     #    st.image('filter_vignette.jpg')
#     #with col4:
#     #    st.caption('Pencil Sketch')
#     #    st.image('filter_pencil_sketch.jpg')

#     # Flag for showing output image.
#     output_flag = 1
#     # Colorspace of output image.
#     color = 'BGR'

#      # Generate filtered image based on the selected option.
#     if option == 'None':
#         # Don't show output image.
#         output_flag = 0
#     elif option == 'Black and White':
#         output = bw_filter(img)
#         color = 'GRAY'
#     elif option == 'Sepia / Vintage':
#         output = sepia(img)
#     elif option == 'Vignette Effect':
#         level = st.slider('level', 0, 5, 2)
#         output = vignette(img, level)
#     elif option == 'Pencil Sketch':
#         ksize = st.slider('Blur kernel size', 1, 11, 5, step=2)
#         output = pencil_sketch(img, ksize)
#         color = 'GRAY'
#     elif option == 'Stylization':
#         sigma_s = st.slider('sigma_s',0, 200, 40, step = 10)
#         #sigma_r = st.slider('sigma_r', 0, 1,value = 0.1, step = 0.1)
#         output = stylization(img, sigma_s) #, sigma_r
#     elif option == 'Blur':
#         ksize = st.slider('Gaussian Blur kernel size', 1, 13, 7, step = 2)
#         output = blur_img(img, ksize)
#     elif option == 'Sharp':
#         output = sharping_filter(img)
#     elif option == 'HDR':
#         output = HDR(img)
#     elif option == 'Invert Color':
#         output = invert(img)
#     elif option == 'Sommer Effect':
#         output = warm_filter(img)
#     elif option == 'Cold Effect':
#         output = Cold_filter(img)
#     elif option == 'Embossed Edges':
#         output = embossed_edges(img)
#     elif option == 'Right Sobel':
#         output = right_sobel(img)
#     elif option == 'Brightnis':
#         level = st.slider('Brightnis Level', -50, 50, 25, step = 5)
#         output = bright(img, level)
#     elif option == 'Outline':
#         k = st.slider('Outline level', 5, 17, 9, step = 9)
#         output = outline(img, k)

#     with output_col:
#         if output_flag == 1:
#             st.header('Output')
#             st.image(output, channels=color)
#             # fromarray convert cv2 image into PIL format for saving it using download link.
#             if color == 'BGR':
#                 result = Image.fromarray(output[:,:,::-1])
#             else:
#                 result = Image.fromarray(output)
#             # Display link.
#             st.markdown(get_image_download_link(result,'output.png','Download '+'Output'),
#                         unsafe_allow_html=True)


# st.set_page_config(page_title="🎨 Artistic Studio", layout="wide")

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

# Style CSS personnalisé
st.markdown("""
    <style>
        .main {
            background-color: #fdf6f0;
        }
        .stApp {
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            color: #6c3483;
            font-size: 3em;
            text-align: center;
        }
        h2, h3 {
            color: #884ea0;
        }
        .css-1aumxhk {
            background-color: #ffffff88 !important;
        }
        .download-link {
            color: white;
            background-color: #884ea0;
            padding: 0.6em 1.2em;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
        }
        .download-link:hover {
            background-color: #a569bd;
        }
    </style>
""", unsafe_allow_html=True)

# ✨ Titre de la page
st.markdown("## 📷✨ Bienvenue dans votre studio de filtres artistiques")
st.markdown("Transformez vos **photos ordinaires en chefs-d’œuvre émotionnels**. Laissez parler votre créativité avec des filtres puissants, inspirants, et magnifiquement rendus. 🎭🎨")

# Upload
uploaded_file = st.file_uploader("🌈 Importez une image pour la transformer :", type=['png','jpg','jpeg'])

# Fonctions de filtres (utilisées dans ton code initial)
# ... [tes fonctions de filtres sont déjà parfaites, pas besoin de les réafficher ici]

# 📸 Affichage et sélection
if uploaded_file is not None:
    raw_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🖼️ Image Originale")
        st.image(img, channels='BGR')

    with col2:
        st.markdown("### 🎭 Sélectionnez un filtre artistique :")
        option = st.selectbox("",
            (
                'None',
                'Black and White',
                'Sepia / Vintage',
                'Vignette Effect',
                'Pencil Sketch',
                'Stylization',
                'Blur',
                'Sharp',
                'HDR',
                'Invert Color',
                'Sommer Effect',
                'Cold Effect',
                'Embossed Edges',
                'Right Sobel',
                'Brightnis',
                'Outline'
            )
        )

        output_flag = 1
        color = 'BGR'

        if option == 'None':
            output_flag = 0
        elif option == 'Black and White':
            output = bw_filter(img)
            color = 'GRAY'
        elif option == 'Sepia / Vintage':
            output = sepia(img)
        elif option == 'Vignette Effect':
            level = st.slider('🎯 Intensité du vignettage', 0, 5, 2)
            output = vignette(img, level)
        elif option == 'Pencil Sketch':
            ksize = st.slider('🖌️ Niveau du flou artistique', 1, 11, 5, step=2)
            output = pencil_sketch(img, ksize)
            color = 'GRAY'
        elif option == 'Stylization':
            sigma_s = st.slider('🎨 Style artistique (sigma_s)', 0, 200, 60, step=10)
            output = stylization(img, sigma_s)
        elif option == 'Blur':
            ksize = st.slider('🌫️ Intensité du flou', 1, 13, 7, step=2)
            output = blur_img(img, ksize)
        elif option == 'Sharp':
            output = sharping_filter(img)
        elif option == 'HDR':
            output = HDR(img)
        elif option == 'Invert Color':
            output = invert(img)
        elif option == 'Sommer Effect':
            output = warm_filter(img)
        elif option == 'Cold Effect':
            output = Cold_filter(img)
        elif option == 'Embossed Edges':
            output = embossed_edges(img)
        elif option == 'Right Sobel':
            output = right_sobel(img)
        elif option == 'Brightnis':
            level = st.slider('☀️ Luminosité', -50, 50, 25, step=5)
            output = bright(img, level)
        elif option == 'Outline':
            k = st.slider('✏️ Détection des contours', 5, 17, 9, step=2)
            output = outline(img, k)

    if output_flag == 1:
        st.markdown("## 🌟 Résultat Émotionnel")
        st.image(output, channels=color)

        if color == 'BGR':
            result = Image.fromarray(output[:,:,::-1])
        else:
            result = Image.fromarray(output)

        # Bouton de téléchargement
        buffered = io.BytesIO()
        result.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        st.markdown(
            f'<a href="data:file/jpg;base64,{img_str}" download="artistic_output.jpg" class="download-link">📥 Télécharger l’image artistique</a>',
            unsafe_allow_html=True
        )

        st.markdown("### 💬 Astuce")
        st.markdown("> *Chaque filtre raconte une histoire. Explorez-les tous pour trouver celui qui fera vibrer votre émotion.* 💖")

# Message si aucune image
else:
    st.markdown("🎬 **Commencez dès maintenant en important une photo.** Transformez-la avec amour et émotion.")
