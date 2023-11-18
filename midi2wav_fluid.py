from midi2audio import FluidSynth

def midi_to_wav(midi_file_path, wav_file_path, soundfont_path):
    fs = FluidSynth(soundfont_path)
    fs.midi_to_audio(midi_file_path, wav_file_path)

# MIDI 파일 경로
midi_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\midiFile\airplane.mid"

# WAV 파일 저장 경로
wav_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\toWAV\airplane.wav"

# SoundFont 파일 경로 수정
soundfont_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\TiMidity++-2.15.0-w32\TiMidity++-2.15.0\FluidR3_GM.sf2"

# MIDI를 WAV로 변환
midi_to_wav(midi_file_path, wav_file_path, soundfont_path)


