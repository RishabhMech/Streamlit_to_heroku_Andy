#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries
import nltk

import SessionState
import streamlit as st
#import streamlit_theme as stheme

from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot.storage import StorageAdapter

import time,datetime
from datetime import datetime, date, time

import json

# Streamlit web Theme
st.sidebar.title("Menu Based Hair styler ChatBot")
st.title("""
Andy, the Hair Styler  
We've got range of services, built just for you!
""")

### gif from local file
import base64
file_ = open(r"media/hairstyle.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

#### Begin Conv.
st.text_area("Andy:", value="Hi I'm Andy! What can I help you with?", height=50, max_chars=None, key=None)


# Declare session state for the 1 user API
session_state= SessionState.get(button_c1=False, button_c2=False, button_submit=False, bdt=False, bs2=False)
b1,b2 = st.beta_columns([0.5,0.5]) 
with b1:
    button_c1=st.button("Make an appointment!")
with b2:
    button_c2=st.button("Nah thanks! I'm all good!")

if button_c1:
    session_state.button_c1=True
if button_c2:
    session_state.button_c2=True
    
dt=""
if session_state.button_c1:
    st.text_area("Andy:", value="Please choose your preferences!", height=50, max_chars=None, key=None)
    session_state.cb1 = st.checkbox('cut')
    session_state.cb2 = st.checkbox('wash')
    session_state.cb3 = st.checkbox('color')     
    
    tst=""
    if session_state.cb1:
        tst=tst+" ✦cut✦ "
    if session_state.cb2:
        tst=tst+" ✦wash✦ "
    if session_state.cb3:
        tst=tst+" ✦color✦ "
    session_state.cb=session_state.cb1+session_state.cb2+session_state.cb3
    
    if session_state.cb<3:
        st.text_area("Andy:", value='You selected '+str(session_state.cb)+ 'services--> ' +tst, height=50, max_chars=None, key=None) 
    else:
        st.text_area("Andy:", value='That\'s one premium appointment!' +tst, height=50, max_chars=None, key=None)
        
    if st.button("Submit"):
        session_state.button_submit=True
    if session_state.button_submit:
        st.text_area("Andy:", value="Choose your day available!", height=50, max_chars=None, key=None)
        session_state.dt= st.date_input('Open Calendar')
        st.text_area("Andy:", value='Booking appointment for '+ str(session_state.dt), height=50, max_chars=None, key=None)
        
        session_state.button_submit2=st.button("Done")
        if session_state.button_submit2:
            st.text_area("Andy:", value="Congrats! We've your appointment. Please leave feedbacks, if any!", height=50, max_chars=None, key=None)
        
if session_state.button_c2:
    st.text_area("Andy:", value="Find me here, take care!", height=50, max_chars=None, key=None)
