import keyboard
import win32api
import time

VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1

while True:
    key = keyboard.read_key(suppress=False)
    if key == "f9":
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PREV_TRACK, 0)
        win32api.keybd_event(VK_MEDIA_PREV_TRACK, hwcode)
        time.sleep(0.2)

    elif key == "f10":
        hwcode = win32api.MapVirtualKey(VK_MEDIA_NEXT_TRACK, 0)
        win32api.keybd_event(VK_MEDIA_NEXT_TRACK, hwcode)
        time.sleep(0.2)
    
    elif key == "f8":
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)
        time.sleep(0.2)