import keyboard
import time

def toggle_pause():
    keyboard.send('play/pause media')

DetectKeyDown = 0
# s 키에 핫키 설정
print("키설정.")
key = keyboard.read_event().name
print(key,"누르면 재생.")
while keyboard.is_pressed(key):
    pass
while True:
    if keyboard.is_pressed(key):
        toggle_pause()
        while keyboard.is_pressed(key):
            time.sleep(0.1)  # 키가 눌린 상태에서 반복 실행 방지
            DetectKeyDown += 0.1
        if DetectKeyDown > 1.5:
            toggle_pause()
        DetectKeyDown = 0
    if keyboard.is_pressed('f12'):
        break
    time.sleep(0.03)
