from music21 import note, stream, tempo
import re

def make_midi(txt):
    # 음표 생성
    n1 = note.Note("C4", quarterLength=1)  # 도
    n2 = note.Note("C#4", quarterLength=1) # 도# (레♭)
    n3 = note.Note("D4", quarterLength=1)  # 레
    n4 = note.Note("D#4", quarterLength=1) # 레# (미♭)
    n5 = note.Note("E4", quarterLength=1)  # 미
    n6 = note.Note("F4", quarterLength=1)  # 파
    n7 = note.Note("F#4", quarterLength=1) # 파# (솔♭)
    n8 = note.Note("G4", quarterLength=1)  # 솔
    n9 = note.Note("G#4", quarterLength=1) # 솔# (라♭)
    n10 = note.Note("A4", quarterLength=1) # 라
    n11 = note.Note("A#4", quarterLength=1) # 라# (시♭)
    n12 = note.Note("B4", quarterLength=1) # 시
    n13 = note.Note("C5", quarterLength=1) # 도

    note_dict = {
        "C4": n1,
        "C#4": n2,
        "D4": n3,
        "D#4": n4,
        "E4": n5,
        "F4": n6,
        "F#4": n7,
        "G4": n8,
        "G#4": n9,
        "A4": n10,
        "A#4": n11,
        "B4": n12,
        "C5": n13
    }

    # 정규표현식을 사용하여 원하는 패턴을 찾아냄
    pattern = re.compile(r"[CDEFGAB]#?\d,?")
    nlist = pattern.findall(txt)

    # 결과를 저장할 리스트
    note_list = []

    # 찾아낸 패턴을 리스트에 저장
    for i in nlist:
        if "," in i:
            note_list.append(note_dict.get(i[:-1]))
        else:
            note_list.append(note_dict.get(i))

    # 음표를 포함하는 스트림 생성
    stream1 = stream.Stream()

    # 중복 포함하여 음표 추가
    for note_obj in note_list:
        cloned_note = note_obj.__deepcopy__()  # music21 객체를 복제
        stream1.append(cloned_note)  # 복제된 객체를 스트림에 추가

    # 템포 설정
    stream1.append(tempo.MetronomeMark(number=120))

    # 저장할 폴더 경로 설정
    output_folder = "C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/midiFile/"

    # 스트림을 미디 파일로 저장
    file_path = output_folder + "airplane.mid"
    stream1.write("midi", file_path)
    print(f"MIDI 파일이 {file_path}에 생성되었습니다.")

#사용 예시
txt = "이것은 비행기라는 곡입니다. E4, D4, C4, D4, E4, E4, E4, D4, D4, D4, E4, E4, E4, E4, D4, C4, D4, E4, E4, E4, D4, D4, E4, D4, C4 감사합니다."
make_midi(txt)
