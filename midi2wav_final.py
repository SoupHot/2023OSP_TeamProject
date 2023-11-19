from collections import defaultdict
from mido import MidiFile
from pydub import AudioSegment
from pydub.generators import Sine

# MIDI 파일 경로
midi_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\midiFile\airplane.mid"

# WAV 파일 저장 경로
wav_file_path = r"C:\Users\8060s\OneDrive\문서\2학년 2학기\오픈소스 프로그래밍\오픈 소스 팀플\MakeTestMusic\toWAV\airplane.wav"

def note_to_freq(note, concert_A=440.0):
    '''
    from wikipedia: http://en.wikipedia.org/wiki/MIDI_Tuning_Standard#Frequency_values
    '''
    return (2.0 ** ((note - 69) / 12.0)) * concert_A

def midi_to_wav(midi_file_path, wav_file_path):
    mid = MidiFile(midi_file_path)
    output = AudioSegment.silent(mid.length * 1000.0)

    tempo = 120 # bpm

    def ticks_to_ms(ticks):
        tick_ms = (60000.0 / tempo) / mid.ticks_per_beat
        return ticks * tick_ms

    for track in mid.tracks:
        # position of rendering in ms
        current_pos = 0.0

        current_notes = defaultdict(dict)
        # current_notes = {
        #   channel: {
        #     note: (start_time, message)
        #   }
        # }
        
        for msg in track:
            current_pos += ticks_to_ms(msg.time)

            if msg.type == 'note_on':
                current_notes[msg.channel][msg.note] = (current_pos, msg)

            if msg.type == 'note_off':
                start_pos, start_msg = current_notes[msg.channel].pop(msg.note)
            
                duration = current_pos - start_pos
            
                signal_generator = Sine(note_to_freq(msg.note))
                rendered = signal_generator.to_audio_segment(duration=duration-50, volume=-20).fade_out(100).fade_in(30)

                output = output.overlay(rendered, start_pos)

    output.export(wav_file_path, format="wav")
    print(f"WAV 파일이 {wav_file_path}에 생성되었습니다.")

# 함수 호출
midi_to_wav(midi_file_path, wav_file_path)
