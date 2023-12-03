import streamlit as st
import requests
from gpt4imageprompt import analyze_image

st.title('OSP Team Project')
st.subheader('2023OSP 오픈더소스')

img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])

if img_file:
    st.image(img_file)
    image_description = analyze_image(st.secrets["API_KEY"], img_file)
    st.text(image_description)


    with st.spinner('음악을 생성하는 중입니다...'):
        # API 엔드포인트 URL
        url = st.secrets["URL"]
        prompt = image_description # 예시 프롬프트
        duration = 30  # 예시 지속 시간 (초)

        # API 호출하여 음악 파일 받기
        response = requests.get(f"{url}/{prompt}/{duration}")

        # 받은 파일을 로컬 시스템에 저장
        file_path = "downloaded_music.wav"
        with open(file_path, "wb") as file:
            file.write(response.content)

    st.audio(file_path, format='audio/wav')