import os
from audiocraft.models import musicgen
from audiocraft.data.audio import audio_write

# 필요한 라이브러리를 설치하는 부분입니다. 
# 이 부분은 비주얼 스튜디오 코드의 터미널에서 실행해야 합니다.
# !pip install --upgrade spacy
# !pip install --upgrade spacy==3.5.2
# !python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft

def generate_music(prompt, output_dir, output_filename_prefix, duration=30):
    """
    음악을 생성하고 저장하는 함수입니다.
    
    Args:
    prompt (str): 음악 생성을 위한 프롬프트 텍스트.
    output_dir (str): 생성된 음악 파일을 저장할 디렉토리 경로.
    output_filename_prefix (str): 생성된 음악 파일의 이름 접두사.
    duration (int, optional): 음악의 길이(초 단위). 기본값은 30초입니다.
    """
    # 생성할 음악 파일의 경로가 존재하지 않으면 생성합니다.
    os.makedirs(output_dir, exist_ok=True)

    # 사전 훈련된 모델을 불러옵니다.
    # device를 'cpu'로 설정하면 CPU를 사용하여 음악을 생성합니다.
    # device를 'cuda'로 설정하면 GPU를 사용하여 음악을 생성합니다.
    model = musicgen.MusicGen.get_pretrained('facebook/musicgen-small', device='cpu')

    # 생성 매개변수 설정
    model.generation_params = {'use_sampling': True,
                               'temp': 1.0,
                               'top_k': 250,
                               'top_p': 0.0,
                               'cfg_coef': 3.0,
                               'two_step_cfg': False}
    model.set_generation_params(duration=duration)

    # 음악 생성
    output_musics = model.generate([prompt], progress=True)

    # 생성된 음악 파일을 저장합니다.
    for i, output_music in enumerate(output_musics):
        output_file_path = os.path.join(output_dir, f'{output_filename_prefix}_{i}.wav')
        audio_write(output_file_path, output_music.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)

# 함수 사용 예시
file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\final_music"
prompt_text = 'I am on the battlefield and I am going to wipe out all my enemies. I am the strongest. I am full of confidence. Sparta.'
generate_music(prompt_text, file_path, 'Sparta')

