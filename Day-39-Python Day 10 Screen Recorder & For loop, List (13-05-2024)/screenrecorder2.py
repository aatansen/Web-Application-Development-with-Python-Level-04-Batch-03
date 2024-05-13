import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
import threading

class VideoRecorder(QWidget):
    def __init__(self):
        super().__init__()

        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)

        self.dim = (self.width, self.height)
        self.fourcc = cv2.VideoWriter_fourcc(*"avc1")
        self.output = None
        self.recording = False
        self.paused = False
        self.start_time = 0
        self.duration = 30

        self.initUI()

    def initUI(self):
        self.startButton = QPushButton('Start', self)
        self.pauseButton = QPushButton('Pause', self)
        self.stopButton = QPushButton('Stop', self)

        self.startButton.clicked.connect(self.startRecording)
        self.pauseButton.clicked.connect(self.pauseRecording)
        self.stopButton.clicked.connect(self.stopRecording)

        layout = QVBoxLayout()
        layout.addWidget(self.startButton)
        layout.addWidget(self.pauseButton)
        layout.addWidget(self.stopButton)

        self.setLayout(layout)
        self.setWindowTitle('Video Recorder')

    def startRecording(self):
        if not self.recording:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Video", "", "Video Files (*.mp4)")
            if file_name:
                self.output = cv2.VideoWriter(f"{file_name}.mp4", self.fourcc, 30.0, self.dim)
                self.recording = True
                self.paused = False
                self.start_time = time.time()
                threading.Thread(target=self.record).start()

    def pauseRecording(self):
        self.paused = not self.paused

    def stopRecording(self):
        self.recording = False

    def record(self):
        while self.recording:
            if not self.paused:
                image = pyautogui.screenshot()
                frame_1 = np.array(image)
                frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
                self.output.write(frame)

            c_time = time.time()
            if c_time - self.start_time > self.duration:
                self.stopRecording()

            time.sleep(0.03)  # Sleep for a short duration to prevent high CPU usage

        if self.output is not None:
            self.output.release()
            print("__END__")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = VideoRecorder()
    recorder.show()
    sys.exit(app.exec_())
