from music21 import note, stream, tempo

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

# 음표를 포함하는 스트림 생성
stream1 = stream.Stream()
stream1.append([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13])

# 템포 설정
stream1.append(tempo.MetronomeMark(number=120))

# 저장할 폴더 경로 설정
output_folder = "C:/Users/8060s/OneDrive/문서/2학년 2학기/오픈소스 프로그래밍/오픈 소스 팀플/MakeTestMusic/midiFile/"

# 스트림을 미디 파일로 저장
file_path = output_folder + "testMusic.mid"
stream1.write("midi", file_path)
