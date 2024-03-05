import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from FrmBioskop import FormBioskop

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel(self)
        self.label.setText("Pilih Menu")
        self.label.setGeometry(100, 50, 100, 30)

        self.FormBioskop_button = QPushButton(self)
        self.FormBioskop_button.setText("Kasir")
        self.FormBioskop_button.setGeometry(50, 100, 150, 30)
        self.FormBioskop_button.clicked.connect(self.open_FormBioskop)

    def open_FormBioskop(self):
        self.form_bioskop = FormBioskop()
        self.form_bioskop.show()

def main():
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
