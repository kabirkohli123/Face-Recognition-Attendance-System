import streamlit as st
import cv2
import numpy as np
import pickle
import time
import os
import pandas as pd
from datetime import datetime
from PIL import Image

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

def load_background():
    st.markdown(
        """
        <style>
            .stApp {
                background: url('https://source.unsplash.com/1600x900/?futuristic,tech');
                background-size: cover;
                color: white;
            }
            .header-text {
                text-align: center;
                font-size: 32px;
                font-weight: bold;
            }
            .info-box {
                padding: 15px;
                border-radius: 10px;
                background-color: rgba(0, 0, 0, 0.6);
                color: white;
                text-align: center;
                font-size: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_title="AI Attendance System", layout="wide")
load_background()

st.markdown("<div class='header-text'>🤖 AI-Powered Attendance System</div>", unsafe_allow_html=True)
st.markdown("<div class='info-box'>Face Recognition Based Attendance Tracking</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    try:
        img_path = os.path.join(os.getcwd(), "data/NewBack2.webp")
        img = Image.open(img_path)
        st.image(img, width=300)
    except Exception as e:
        st.error("Error loading background image. Ensure 'NewBack2.webp' is in the correct directory.")

with col2:
    st.markdown(
        """
        <div class='info-box'>
        - **Live Face Recognition** 🎥<br>
        - **Automated Attendance Marking** 📝<br>
        - **Secure & Fast Processing** 🔒
        </div>
        """,
        unsafe_allow_html=True,
    )




df=pd.read_csv("Attendance/Attendance_" + date + ".csv")

st.dataframe(df.style.highlight_max(axis=0))