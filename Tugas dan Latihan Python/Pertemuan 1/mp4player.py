from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QStyle, QFileDialog, 
                            QSlider, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
import os
 
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Riz MP4 Player")
        self.setGeometry(600,200,800,600)
        self.setWindowIcon(QIcon('imgs/python.jpg'))
  
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
  
        self.init_ui()
        self.show()
  
    def init_ui(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
  
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
  
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
  
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)
        hboxlayout = QHBoxLayout()
        hboxlayout.setContentsMargins(0,0,0,0)
  
        hboxlayout.addWidget(openBtn)
        hboxlayout.addWidget(self.playBtn)
        hboxlayout.addWidget(self.slider)
  
        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(videowidget)
        vboxlayout.addLayout(hboxlayout)
        vboxlayout.addWidget(self.label)
  
        self.setLayout(vboxlayout)
        self.mediaPlayer.setVideoOutput(videowidget)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video",
                                os.getcwd(),
                                ("Video Files (*.avi  *.mp4)"))
        if filename !='':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
  
    def play_video(self):
  
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())