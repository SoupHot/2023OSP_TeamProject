import os
import subprocess

# MIDI 파일 경로
midi_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\midiFile\airplane.mid"

# WAV 파일 저장 경로
wav_file_path = 'C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/toWAV/airplane.wav'

# Timidity 실행 파일 경로
timidity_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\TiMidity++-2.15.0-w32\TiMidity++-2.15.0\timidity.exe"

# 환경 변수 설정
os.environ['PATH'] += os.pathsep + os.path.dirname(timidity_path)

# Timidity를 사용하여 MIDI를 WAV로 변환
try:
    subprocess.run([timidity_path, midi_file_path, "-Ow", "-o", wav_file_path], check=True)
    print(f"WAV 파일이 {wav_file_path}에 생성되었습니다.")
except subprocess.CalledProcessError as e:
    print(f"TiMidity를 사용하여 MIDI를 WAV로 변환하는 중 오류 발생: {e}")
