import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width, height)
# f = cv2.VideoWriter_fourcc(*"avc1")
# f = cv2.VideoWriter_fourcc(*"H264")
f = cv2.VideoWriter_fourcc(*"mp4v")
file_name=input("Enter video file name: ")
output = cv2.VideoWriter(f"{file_name}.mp4", f, 30.0, dim)
now_start_time = time.time()
dur = 5
end_time = now_start_time + dur

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()
print("__END__")
