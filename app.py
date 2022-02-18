import streamlit as st
from datetime import datetime
import constants as c


st.set_page_config(page_title='Hemifacial Spasm Journey', 
                   page_icon=c.hfs_gif, 
                   layout="wide", 
                   initial_sidebar_state="auto", 
                   menu_items=None
                   )
# add_selectbox = st.sidebar.slider(label = 'Timeline',
#                                   min_value=2017,
#                                   max_value=2022
#                                   )
st.header('My Journey of Treating Hemifacial Spasm', anchor='a')
st.header('2017 - How it started')
st.write(c.start)
st.image(c.twitching_gif,caption='Eye Twitch', width=250)
st.write(c.reaction)

st.header("Progress")
st.write(c.progress)

st.header('2018 - Eye Consultation with [Dr. Dipankar Roy](%s)' % c.dipankar_roy_link)
st.write(c.eye_consultation1 % c.dipankar_roy_link)
st.write(c.eye_consultation1_reaction)

st.header('2019 - Eye Consultation with [Dr. Somnath Majumdar](%s)' % c.somnath_majumdar_link)
col1, col2 = st.columns(2)
with col1:
    st.image('https://fortiskolkata.com/assets/uploads/doctors/dr%20somnath.jpg',
             caption='Dr. Somnath Majumdar',
             width=200)
with col2:
    st.write(c.eye_consultation2)
st.write(c.eye_consultation2_reaction)
st.image(c.hfs_gif,caption="Hemifacial Spasm", width=250)


st.header('2019 - Eye Consultation at [LV Prasad Eye Institute](%s)' % c.lvpei_link)
col1, col2 = st.columns(2)
with col1:
    st.image('https://avocure-uploads.s3.amazonaws.com/uploads/clinic/cover_pic_url/122/dr-taraprasad-das-lv-prasad-eye-institute--banjara-hills-hyderabad-ophthalmologists-2rd1m.jpg',
             caption='LV Prasad Eye Institute Hyderabad',
             width=350)
with col2:
    st.write(c.eye_consultation3)
st.write(c.eye_consultation3_reaction)
st.image(c.tension_gif,caption='Tension',width=250)

st.header('2019 - Neurology Counsultation at [Care Hospital Hi-Tech City](%s)' % c.care_hospital_link)
col1, col2 = st.columns(2)
with col1:
    st.image('https://www.carehospitals.com/wp-content/uploads/2018/09/Dr.-JMK-Murthy.png',
             caption='Dr. J M K Murthy Care Hospital Hi-Tech City Hyderabad',
             width=300)
with col2:
    st.write(c.neuro_consultation1)
st.write(c.neuro_consultation1_reaction)
st.image(c.tension_gif2, caption='More Tension', width=250)

