import streamlit as st
from gpt4imageprompt import analyze_image

st.title('OSP Team Project')
st.subheader('2023OSP 오픈더소스')

img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
print(img_file)

if img_file:
    st.image(img_file)
    image_description = analyze_image(st.secrets["API_KEY"], img_file)
    st.text(image_description)
    print(image_description)
    audio_file = open('airplane.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')