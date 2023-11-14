import streamlit as st

st.text('OSP Team Project')

img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
if img_file:
    st.image(img_file)