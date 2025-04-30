# import streamlit as st
# from streamlit_image_comparison import image_comparison
# import cv2


# st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")

# st.header("🔭 J. Webb Space Telescope vs Hubble Telescope")

# st.write("")
# "This is a reproduction of the fantastic [WebbCompare](https://www.webbcompare.com/index.html) app by [John Christensen](https://twitter.com/JohnnyC1423). It's built in Streamlit and takes only 10 lines of Python code. If you like this app, please star [John's original repo](https://github.com/JohnEdChristensen/WebbCompare)!"
# st.write("")

# st.markdown("### Southern Nebula")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
#     img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
#     label1="Hubble",
#     label2="Webb",
# )


# st.markdown("### Galaxy Cluster SMACS 0723")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
#     img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
#     label1="Hubble",
#     label2="Webb",
# )

# st.markdown("### Carina Nebula")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/carina_2800.png",
#     img2="https://www.webbcompare.com/img/webb/carina_2800.jpg",
#     label1="Hubble",
#     label2="Webb",
# )

# st.markdown("### Stephan's Quintet")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
#     img2="https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg",
#     label1="Hubble",
#     label2="Webb",
# )

# -*- coding: utf-8 -*-
# """
# Created on Tue Oct 27 20:37:29 2020

# @author: aniket wattamwar
# """

# import streamlit as st
# from PIL import Image
# import cv2 
# import numpy as np



# def main():

#     selected_box = st.sidebar.selectbox(
#     'Choose one of the following',
#     ('Welcome','Image Processing', 'Video', 'Face Detection', 'Feature Detection', 'Object Detection')
#     )
    
#     if selected_box == 'Welcome':
#         welcome() 
#     if selected_box == 'Image Processing':
#         photo()
#     if selected_box == 'Video':
#         video()
#     if selected_box == 'Face Detection':
#         face_detection()
#     if selected_box == 'Feature Detection':
#         feature_detection()
#     if selected_box == 'Object Detection':
#         object_detection() 
 

# def welcome():
    
#     st.title('Image Processing using Streamlit')
    
#     st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
#              + ' from the left. I have implemented only a few to show how it works on Streamlit. ' + 
#              'You are free to add stuff to this app.')
    
#     st.image('-5848214997551926325_121.jpg',use_column_width=True)


# def load_image(filename):
#     image = cv2.imread(filename)
#     return image
 
# def photo():

#     st.header("Thresholding, Edge Detection and Contours")
    
#     if st.button('See Original Image of Tom'):
        
#         original = Image.open('-5848214997551926325_121.jpg')
#         st.image(original, use_column_width=True)
        
#     image = cv2.imread('-5848214997551926325_121.jpg')
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     x = st.slider('Change Threshold value',min_value = 50,max_value = 255)  

#     ret,thresh1 = cv2.threshold(image,x,255,cv2.THRESH_BINARY)
#     thresh1 = thresh1.astype(np.float64)
#     st.image(thresh1, use_column_width=True,clamp = True)
    
#     st.text("Bar Chart of the image")
#     histr = cv2.calcHist([image],[0],None,[256],[0,256])
#     st.bar_chart(histr)
    
#     st.text("Press the button below to view Canny Edge Detection Technique")
#     if st.button('Canny Edge Detector'):
#         image = load_image("-5848214997551926325_121.jpg")
#         edges = cv2.Canny(image,50,300)
#         cv2.imwrite('-5848214997551926325_121.jpg',edges)
#         st.image(edges,use_column_width=True,clamp=True)
      
#     y = st.slider('Change Value to increase or decrease contours',min_value = 50,max_value = 255)     
    
#     if st.button('Contours'):
#         im = load_image("-5848214997551926325_121.jpg")
          
#         imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#         ret,thresh = cv2.threshold(imgray,y,255,0)
#         image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
#         img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
 
        
#         st.image(thresh, use_column_width=True, clamp = True)
#         st.image(img, use_column_width=True, clamp = True)
         

    
# def video():
#     uploaded_file = st.file_uploader("Choose a video file to play")
#     if uploaded_file is not None:
#          bytes_data = uploaded_file.read()
 
#          st.video(bytes_data)
         
#     video_file = open('typing.mp4', 'rb')
         
 
#     video_bytes = video_file.read()
#     st.video(video_bytes)
 

# def face_detection():
    
#     st.header("Face Detection using haarcascade")
    
#     if st.button('See Original Image'):
        
#         original = Image.open('friends.jpeg')
#         st.image(original, use_column_width=True)
    
    
#     image2 = cv2.imread("friends.jpeg")

#     face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#     faces = face_cascade.detectMultiScale(image2)
#     print(f"{len(faces)} faces detected in the image.")
#     for x, y, width, height in faces:
#         cv2.rectangle(image2, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    
#     cv2.imwrite("faces.jpg", image2)
    
#     st.image(image2, use_column_width=True,clamp = True)
 

# def feature_detection():
#     st.subheader('Feature Detection in images')
#     st.write("SIFT")
#     image = load_image("tom1.jpg")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     sift = cv2.xfeatures2d.SIFT_create()    
#     keypoints = sift.detect(gray, None)
     
#     st.write("Number of keypoints Detected: ",len(keypoints))
#     image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     st.image(image, use_column_width=True,clamp = True)
    
    
#     st.write("FAST")
#     image_fast = load_image("tom1.jpg")
#     gray = cv2.cvtColor(image_fast, cv2.COLOR_BGR2GRAY)
#     fast = cv2.FastFeatureDetector_create()
#     keypoints = fast.detect(gray, None)
#     st.write("Number of keypoints Detected: ",len(keypoints))
#     image_  = cv2.drawKeypoints(image_fast, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     st.image(image_, use_column_width=True,clamp = True)

    
    
# def object_detection():
    
#     st.header('Object Detection')
#     st.subheader("Object Detection is done using different haarcascade files.")
#     img = load_image("clock.jpg")
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    
#     clock = cv2.CascadeClassifier('haarcascade_wallclock.xml')  
#     found = clock.detectMultiScale(img_gray,  
#                                    minSize =(20, 20)) 
#     amount_found = len(found)
#     st.text("Detecting a clock from an image")
#     if amount_found != 0:  
#         for (x, y, width, height) in found:
     
#             cv2.rectangle(img_rgb, (x, y),  
#                           (x + height, y + width),  
#                           (0, 255, 0), 5) 
#     st.image(img_rgb, use_column_width=True,clamp = True)
    
    
#     st.text("Detecting eyes from an image")
    
#     image = load_image("eyes.jpg")
#     img_gray_ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
#     img_rgb_ = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        
#     eye = cv2.CascadeClassifier('haarcascade_eye.xml')  
#     found = eye.detectMultiScale(img_gray_,  
#                                        minSize =(20, 20)) 
#     amount_found_ = len(found)
        
#     if amount_found_ != 0:  
#         for (x, y, width, height) in found:
         
#             cv2.rectangle(img_rgb_, (x, y),  
#                               (x + height, y + width),  
#                               (0, 255, 0), 5) 
#         st.image(img_rgb_, use_column_width=True,clamp = True)
    
    
    
    
# if __name__ == "__main__":
#     main()

# 

# -*- coding: utf-8 -*-
# """
# Created on Tue Oct 27 20:37:29 2020

# @author: aniket wattamwar
# """

# import streamlit as st
# from PIL import Image
# import cv2 
# import numpy as np



# def main():

#     selected_box = st.sidebar.selectbox(
#     'Choose one of the following',
#     ('Welcome','Image Processing', 'Video', 'Face Detection', 'Feature Detection', 'Object Detection')
#     )
    
#     if selected_box == 'Welcome':
#         welcome() 
#     if selected_box == 'Image Processing':
#         photo()
#     if selected_box == 'Video':
#         video()
#     if selected_box == 'Face Detection':
#         face_detection()
#     if selected_box == 'Feature Detection':
#         feature_detection()
#     if selected_box == 'Object Detection':
#         object_detection() 
 

# def welcome():
    
#     st.title('Image Processing using Streamlit')
    
#     st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
#              + ' from the left. I have implemented only a few to show how it works on Streamlit. ' + 
#              'You are free to add stuff to this app.')
    
#     st.image('hackershrine.jpg',use_column_width=True)


# def load_image(filename):
#     image = cv2.imread(filename)
#     return image
 
# def photo():

#     st.header("Thresholding, Edge Detection and Contours")
    
#     if st.button('See Original Image of Tom'):
        
#         original = Image.open('tom.jpg')
#         st.image(original, use_column_width=True)
        
#     image = cv2.imread('tom.jpg')
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     x = st.slider('Change Threshold value',min_value = 50,max_value = 255)  

#     ret,thresh1 = cv2.threshold(image,x,255,cv2.THRESH_BINARY)
#     thresh1 = thresh1.astype(np.float64)
#     st.image(thresh1, use_column_width=True,clamp = True)
    
#     st.text("Bar Chart of the image")
#     histr = cv2.calcHist([image],[0],None,[256],[0,256])
#     st.bar_chart(histr)
    
#     st.text("Press the button below to view Canny Edge Detection Technique")
#     if st.button('Canny Edge Detector'):
#         image = load_image("jerry.jpg")
#         edges = cv2.Canny(image,50,300)
#         cv2.imwrite('edges.jpg',edges)
#         st.image(edges,use_column_width=True,clamp=True)
      
#     y = st.slider('Change Value to increase or decrease contours',min_value = 50,max_value = 255)     
    
#     if st.button('Contours'):
#         im = load_image("jerry1.jpg")
          
#         imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#         ret,thresh = cv2.threshold(imgray,y,255,0)
#         image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
#         img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
 
        
#         st.image(thresh, use_column_width=True, clamp = True)
#         st.image(img, use_column_width=True, clamp = True)
         

    
# def video():
#     uploaded_file = st.file_uploader("Choose a video file to play")
#     if uploaded_file is not None:
#          bytes_data = uploaded_file.read()
 
#          st.video(bytes_data)
         
#     video_file = open('typing.mp4', 'rb')
         
 
#     video_bytes = video_file.read()
#     st.video(video_bytes)
 

# def face_detection():
    
#     st.header("Face Detection using haarcascade")
    
#     if st.button('See Original Image'):
        
#         original = Image.open('friends.jpeg')
#         st.image(original, use_column_width=True)
    
    
#     image2 = cv2.imread("friends.jpeg")

#     face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#     faces = face_cascade.detectMultiScale(image2)
#     print(f"{len(faces)} faces detected in the image.")
#     for x, y, width, height in faces:
#         cv2.rectangle(image2, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    
#     cv2.imwrite("faces.jpg", image2)
    
#     st.image(image2, use_column_width=True,clamp = True)
 

# def feature_detection():
#     st.subheader('Feature Detection in images')
#     st.write("SIFT")
#     image = load_image("tom1.jpg")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     sift = cv2.xfeatures2d.SIFT_create()    
#     keypoints = sift.detect(gray, None)
     
#     st.write("Number of keypoints Detected: ",len(keypoints))
#     image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     st.image(image, use_column_width=True,clamp = True)
    
    
#     st.write("FAST")
#     image_fast = load_image("tom1.jpg")
#     gray = cv2.cvtColor(image_fast, cv2.COLOR_BGR2GRAY)
#     fast = cv2.FastFeatureDetector_create()
#     keypoints = fast.detect(gray, None)
#     st.write("Number of keypoints Detected: ",len(keypoints))
#     image_  = cv2.drawKeypoints(image_fast, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     st.image(image_, use_column_width=True,clamp = True)

    
    
# def object_detection():
    
#     st.header('Object Detection')
#     st.subheader("Object Detection is done using different haarcascade files.")
#     img = load_image("clock.jpg")
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    
#     clock = cv2.CascadeClassifier('haarcascade_wallclock.xml')  
#     found = clock.detectMultiScale(img_gray,  
#                                    minSize =(20, 20)) 
#     amount_found = len(found)
#     st.text("Detecting a clock from an image")
#     if amount_found != 0:  
#         for (x, y, width, height) in found:
     
#             cv2.rectangle(img_rgb, (x, y),  
#                           (x + height, y + width),  
#                           (0, 255, 0), 5) 
#     st.image(img_rgb, use_column_width=True,clamp = True)
    
    
#     st.text("Detecting eyes from an image")
    
#     image = load_image("eyes.jpg")
#     img_gray_ = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
#     img_rgb_ = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        
#     eye = cv2.CascadeClassifier('haarcascade_eye.xml')  
#     found = eye.detectMultiScale(img_gray_,  
#                                        minSize =(20, 20)) 
#     amount_found_ = len(found)
        
#     if amount_found_ != 0:  
#         for (x, y, width, height) in found:
         
#             cv2.rectangle(img_rgb_, (x, y),  
#                               (x + height, y + width),  
#                               (0, 255, 0), 5) 
#         st.image(img_rgb_, use_column_width=True,clamp = True)
    
    
    
    
# if __name__ == "__main__":
#     main()


import streamlit as st
from PIL import Image
import cv2
import numpy as np

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

def main():
    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome', 'Image Processing', 'Video', 'Face Detection', 'Feature Detection', 'Object Detection')
    )

    if selected_box == 'Welcome':
        welcome()
    if selected_box == 'Image Processing':
        photo()
    if selected_box == 'Video':
        video()
    if selected_box == 'Face Detection':
        face_detection()
    if selected_box == 'Feature Detection':
        feature_detection()
    if selected_box == 'Object Detection':
        object_detection()

def welcome():
    st.title('Image Processing using Streamlit')
    st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
                 + ' from the left. I have implemented only a few to show how it works on Streamlit. '
                 + 'You are free to add stuff to this app.')

def load_image(uploaded_file):
    """ Fonction pour charger l'image à partir du fichier téléchargé. """
    image = Image.open(uploaded_file)
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def photo():
    st.header("Thresholding, Edge Detection and Contours")
    
    # Téléchargement de l'image par l'utilisateur
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        
        st.image(image, use_column_width=True, caption="Original Image")
        
        # Appliquer la conversion en niveaux de gris
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Slider pour le seuil de binarisation
        x = st.slider('Change Threshold value', min_value=50, max_value=255)  
        ret, thresh1 = cv2.threshold(gray_image, x, 255, cv2.THRESH_BINARY)
        st.image(thresh1, use_column_width=True, clamp=True, caption="Thresholded Image")
        
        # Histogramme
        st.text("Bar Chart of the image")
        histr = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        st.bar_chart(histr)

        # Canny Edge Detection
        if st.button('Canny Edge Detector'):
            edges = cv2.Canny(image, 50, 300)
            st.image(edges, use_column_width=True, caption="Canny Edge Detection")

        # Contours
        y = st.slider('Change Value to increase or decrease contours', min_value=50, max_value=255)     
        if st.button('Contours'):
            imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(imgray, y, 255, 0)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            img = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)
            st.image(img, use_column_width=True, caption="Contours Image")
            
def video():
    uploaded_file = st.file_uploader("Choose a video file to play", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.video(bytes_data)

def face_detection():
    st.header("Face Detection using Haarcascade")

    # Téléchargement de l'image par l'utilisateur
    uploaded_file = st.file_uploader("Upload an Image for Face Detection", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = load_image(uploaded_file)
        
        # Chargement du classificateur de visages
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(image)
        
        for x, y, width, height in faces:
            cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
        
        st.image(image, use_column_width=True, caption="Detected Faces")

def feature_detection():
    st.subheader('Feature Detection in images')

    # Téléchargement de l'image par l'utilisateur
    uploaded_file = st.file_uploader("Upload an Image for Feature Detection", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = load_image(uploaded_file)
        
        # SIFT Feature Detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()    
        keypoints = sift.detect(gray, None)
        st.write("Number of keypoints Detected: ", len(keypoints))
        image_sift = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        st.image(image_sift, use_column_width=True, caption="SIFT Keypoints")

        # FAST Feature Detection
        fast = cv2.FastFeatureDetector_create()
        keypoints = fast.detect(gray, None)
        st.write("Number of keypoints Detected: ", len(keypoints))
        image_fast = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        st.image(image_fast, use_column_width=True, caption="FAST Keypoints")

def object_detection():
    st.header('Object Detection')
    
    # Téléchargement de l'image par l'utilisateur
    uploaded_file = st.file_uploader("Upload an Image for Object Detection", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = load_image(uploaded_file)
        
        # Conversion en niveaux de gris
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Détection d'objet : détecter des yeux (par exemple)
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(img_gray)
        
        for (x, y, w, h) in eyes:
            cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        st.image(img_rgb, use_column_width=True, caption="Detected Objects (Eyes)")

if __name__ == "__main__":
    main()
