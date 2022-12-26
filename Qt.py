from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic 
import sys 


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.load_ui("DRONEAPP.ui", self)

app = QApplication(sys.argv)
window = ui()
window.show()
sys.exit(app.exec())