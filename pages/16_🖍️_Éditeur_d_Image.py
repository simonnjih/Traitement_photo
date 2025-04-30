import streamlit as st
from PIL import Image, ImageOps
import io



def filter(file,mode):
 with Image.open(file) as img:
    # mode=input("enter mode:")

    fil_img=img.convert(mode)  
 return fil_img
def crop_image(im, left=None, upper=None, right=None, lower=None):
    with Image.open(im) as img:
     
        
        cropped_img = img.crop((left, upper, right, lower))
    return cropped_img


def rotate(im,i):
    with Image.open(im) as img:
        # i=input("how much you wan to rotate:")
        if i == "90":
            tran_img = img.transpose(Image.ROTATE_90)
        elif i == "180":
            tran_img = img.transpose(Image.ROTATE_180)
        elif i == "270":
            tran_img = img.transpose(Image.ROTATE_270)
    return tran_img
# def resize(img,size,option):
   
#     with Image.open(img) as im:
#         match option:
#             case "contain":
#                image= ImageOps.contain(im, size)
#             case "fit":
#                 image=ImageOps.fit(im, size)
#             case "pad":
#                 image=ImageOps.pad(im, size, color="#f00")
           

#         return  image  
def main():

   st.set_page_config(page_title="image eiditor",page_icon=":camera:")

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

   st .title("image edior")#title of page

   st.header("welcome ")#heading
   st.markdown("""
   <style>
    .eyeqlp51.st-emotion-cache-fblp2m.ex0cdmw0
      {       
       visibility:hidden;
      } 
    .st-emotion-cache-ch5dnh.ef3psqc4
      {
      
       visibility:hidden;

      }
     .st-emotion-cache-cio0dv.ea3mdgi1
      {
               visibility:hidden;
      }
      .uploadedFileName.st-emotion-cache-1uixxvy.e1b2p2ww6
      {
               visibility:hidden;
      }.st-emotion-cache-1mdkfbq e1b2p2ww3{
               visibility:hidden;

      }
   </style>     """,unsafe_allow_html=True)
   st.subheader("Upload image: ")#subheading
   img=st.file_uploader("",type=["png","jpg","jpeg"])
   op=st.sidebar.radio("Editor:",options=["filter","resize","rotate","crop"],index=None,horizontal=False)


   if img is not None:
      st.image(img)

      if op=="filter":
         image_modes = ['1', 'L', 'P', 'RGB', 'RGBA']

         mode=st.select_slider("Mode",options=image_modes)
         # i=im.open(img)
         img= filter(img,mode)
         if img is not None:
            st.image(img)


            # Save the processed image to a BytesIO object
            # processed_image = im.safe(img)

            image_stream = io.BytesIO()

            img.save(image_stream,"PNG")  
                  # Download the processed image
            st.download_button("Download Processed Image", image_stream.getvalue(),file_name='processed_image.png', mime='image/png')



         else:
            st.text("error")
      elif op=="rotate":
         # st.text(":curle:")
         l=["90","270","180"]
         value=st.radio("rotate:",options=l,index=None)
         if value is not None:
           img=rotate(img,value)
           if img is not None:


               st.image(img)
               # Save the processed image to a BytesIO object
               # processed_image = im.safe(img)
               image_stream = io.BytesIO()
               img.save(image_stream,"PNG")  
                     # Download the processed image
               st.download_button("Download Processed Image", image_stream.getvalue(),file_name='processed_image.png', mime='image/png')


    #   elif op=="resize":

    #      l2=["contain","fit","pad"]
    #      value2=st.radio("resize",options=l2,index=None)
    #      width=st.slider("width",min_value=0,max_value=1000)
    #      # st.success(width)
    #      height=st.slider("height",min_value=0,max_value=1000)
    #      # st.success(height)
    #      size=(width,height)
    #      if value2 is not None and width is not 0 and height is not 0:
    #         img=resize(img,size,value2)
    #         if img:

    #            st.image(img)
    #            image_stream = io.BytesIO()
    #            img.save(image_stream,"PNG")  
    #                  # Download the processed image
    #            st.download_button("Download Processed Image", image_stream.getvalue(),file_name='processed_image.png', mime='image/png')


      elif op=="crop":
         left=st.slider("left:",min_value=0,max_value=200)
         upper=st.slider("upper:",min_value=0,max_value=200)
         right=st.slider("right:",min_value=0,max_value=200)
         lower=st.slider("lower:",min_value=0,max_value=200)
         if left is not 0 and right !=0 and upper is not 0 and lower!=0:
            if right<=left:
               st.error("🚨 right can`t less than and equal left ")
            elif lower<=upper:
               st.error("🚨lower is less than upper")
            else:   
               img=crop_image(img,left,upper,right,lower)
               st.image(img)
               image_stream = io.BytesIO()
               img.save(image_stream,"PNG")  
                     # Download the processed image
               st.download_button("Download Processed Image", image_stream.getvalue(),file_name='processed_image.png', mime='image/png')
if __name__=="__main__":
     main() 