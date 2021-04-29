#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the packages
import numpy as np
import pytesseract
from PIL import Image
import cv2
import re
import matplotlib.pyplot as plt
from tqdm import tqdm as tq
from transformers import AutoModelWithLMHead, AutoTokenizer , AutoModelForQuestionAnswering
import torch
import tensorflow
from transformers import pipeline
import warnings
from pytesseract import Output
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import spacy
from skimage.filters import threshold_local
import numpy as np
import cv2
from skimage import filters
from skimage.morphology import disk #needed for the mask
warnings.filterwarnings("ignore")


# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# In[ ]:


pip install torch


# In[18]:


pip install pytesseract


# In[2]:


pip install transformers


# # Giving title and uploading a image to our website

# In[2]:


st.title('Smart Text Scanner')


# In[3]:


image = Image.open('C:\Users\RITIK CHADHA\Documents\Untitled Folder\smarttext.jpg')
st.image(image, caption='by Team Rashi')
image


# In[4]:


st.file_uploader("Upload Image")


# In[5]:


#df = pd.DataFrame({
 # 'first column': [1, 2, 3, 4],
  #'second column': [10, 20, 30, 40]
#})


# In[6]:


#option = st.selectbox(
 #   'Which number do you like best?',
  #   df['first column'])
#'You selected: ', option


# # Adding a sidebar to our website

# In[7]:


st.sidebar.title('Choose Language For Translation')
st.sidebar.subheader('Select:')
src = st.sidebar.selectbox("From Language",['English'])
st.sidebar.subheader('Select:')
destination = st.sidebar.selectbox("To Language",['German','French','Hindi'])


# # Adding buttons to our website

# In[8]:


st.button('Translate Text')
st.button('Image to Text')
st.button('Ask a Question')
st.button('Change Template')


# # 'Ask a Question' Button Function

# In[15]:


def question(tex,questions) :
    answer=question_model(context=tex,question=questions,max_ans_length=12)
    return answer['answer']


# In[16]:


questions = st.text_input("Enter Question")
if st.button('Ask a Question'):
    question(tex,questions)
    st.markdown("answer :" +question())
if __name__ == "__main__":
    scanned_image=read_image("../input/textimage/IMG_20210125_155407__01.png",scan=True)
text=read_image("../input/textimage/IMG_20210125_155407__01.png",scan=False)
tex=pytesseract.image_to_string(text)
    


# In[ ]:




