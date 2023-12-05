import streamlit as st
import requests
from gpt4imageprompt import analyze_image

def get_music(prompt, duration):
    try:
        # API 엔드포인트 URL
        url = st.secrets["URL"]
        prompt = image_description # 예시 프롬프트

        # API 호출하여 음악 파일 받기
        response = requests.get(f"{url}/{prompt}/{duration}")

        # 응답 상태 검증
        if response.status_code != 200:
            raise Exception("API 요청 실패")

        # 받은 파일을 로컬 시스템에 저장
        file_path = "downloaded_music.wav"
        with open(file_path, "wb") as file:
            file.write(response.content)

        return file_path, response.status_code
    except Exception as e:
        return None, None

st.title('Pic To Music')
st.header('사진과 함께 음악을 즐겨보세요.')
st.subheader('OSP Team Project - 2023 OSP 오픈더소스')

if 'duration' not in st.session_state:
    st.session_state['duration'] = None

if 'img_file' not in st.session_state:
    st.session_state['img_file'] = None

if 'duration_selected' not in st.session_state:
    st.session_state['duration_selected'] = False

if st.session_state['duration_selected'] == False:
    st.session_state['duration'] = st.slider('음악의 길이를 선택해 주세요.', 1, 60, 30)
    duration_select_button = st.button('Submit', key='duration_button')
    if st.session_state['duration'] is not None and duration_select_button:
        st.session_state['duration_selected'] = True
        st.rerun()
    else:
        st.stop()

if 'img_uploaded' not in st.session_state:
    st.session_state['img_file'] = st.file_uploader('이미지를 업로드해 주세요(이 서비스는 사용자의 이미지를 저장하지 않습니다.).', type=['png', 'jpg', 'jpeg'])
    if st.session_state['img_file'] is not None:
        st.session_state['img_uploaded'] = True

music_gen = st.button('음악 생성', key='music_gen')

if music_gen and st.session_state['img_file']:    
    with st.spinner('음악을 생성하는 중입니다...'):
        image_description = analyze_image(st.secrets["API_KEY"], st.session_state['img_file'])
        file_path, response_status = get_music(image_description, st.session_state['duration'])

    if file_path and response_status is not None:
        st.image(st.session_state['img_file'])
        # st.text(image_description)
        st.audio(file_path, format='audio/wav')
        st.info('서비스에 대한 평가를 설문으로 남겨주세요.')
        st.link_button("설문 참여", "https://docs.google.com/forms/d/e/1FAIpQLSe98TGLm_obqZcz7mlD8EKqatggfEm77bt-Lmt1zgGAd55-0A/viewform?usp=sf_link")
    else:
        st.error("잠시 후 다시 시도해 주세요.")

elif music_gen and not st.session_state['img_file']:
        st.warning('이미지를 업로드해 주세요.')
        st.stop()