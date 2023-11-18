from pydub import AudioSegment

def convert_wav_to_mp3(wav_file, mp3_file, bitrate='192k'):
    # WAV 파일 로드
    sound = AudioSegment.from_wav(wav_file)

    # MP3로 변환 및 저장
    sound.export(mp3_file, format="mp3", bitrate=bitrate)
    print(f"MP3 파일이 {mp3_file}에 생성되었습니다.")

# WAV 파일 경로 및 MP3 파일 경로 설정
wav_file_path = 'C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/toWAV/example_music21.wav'
mp3_file_path = 'C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/toMP3/example_music21.mp3'

# WAV를 MP3로 변환
convert_wav_to_mp3(wav_file_path, mp3_file_path)

# bank 1
# 1 %font FluidR3_GM.sf2 0 1
