import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MP3PlayerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MP3 Player")
        self.setGeometry(100, 100, 400, 200)

        self.media_player = QMediaPlayer(self)
        self.playlist = []

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_music)
        layout.addWidget(self.play_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_music)
        layout.addWidget(self.pause_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_music)
        layout.addWidget(self.stop_button)

        self.open_button = QPushButton("Open MP3")
        self.open_button.clicked.connect(self.open_music)
        layout.addWidget(self.open_button)

        self.setLayout(layout)

    def play_music(self):
        if self.playlist:
            self.media_player.play()

    def pause_music(self):
        self.media_player.pause()

    def stop_music(self):
        self.media_player.stop()

    def open_music(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("MP3 files (*.mp3)")
        file_dialog.selectNameFilter("MP3 files (*.mp3)")

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                self.playlist.append(file_path)
                self.play_selected_music()

    def play_selected_music(self):
        if self.playlist:
            current_file = self.playlist[-1]
            media_content = QMediaContent(QUrl.fromLocalFile(current_file))
            self.media_player.setMedia(media_content)
            self.play_music()

if __name__ == "__main__":
    app = QApplication([])
    mp3_player = MP3PlayerApp()
    mp3_player.show()
    app.exec_()
