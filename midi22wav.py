import os
import subprocess

# MIDI 파일 경로
midi_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\midiFile\example_music21.mid"

# WAV 파일 저장 경로
wav_file_path = 'C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/toWAV/example_music21.wav'

# Timidity 실행 파일 경로
timidity_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\TiMidity++-2.15.0-w32\TiMidity++-2.15.0\timw32g.exe"

# Timidity를 사용하여 MIDI를 WAV로 변환
try:
    subprocess.run(f"{timidity_path} {midi_file_path} -Ow -o {wav_file_path}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"WAV 파일이 {wav_file_path}에 생성되었습니다.")
except subprocess.CalledProcessError as e:
    print(f"TiMidity를 사용하여 MIDI를 WAV로 변환하는 중 오류 발생: {e}")
