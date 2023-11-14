from midi2audio import FluidSynth

def convert_midi_to_mp3(midi_file, mp3_file):
    sound_font_path = r"C:\Users\8060s\Downloads\FluidR3_GM\FluidR3_GM.sf2"
    fs = FluidSynth(sound_font=sound_font_path)
    fs.midi_to_audio(midi_file, mp3_file)

# 사용 예시
midi_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\midiFile\example_music21.mid"
mp3_file_path = 'C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/toMP3/example_music21.mp3'
convert_midi_to_mp3(midi_file_path, mp3_file_path)