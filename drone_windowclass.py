from PyQt6.QtWidgets import QApplication, QWidget
import sys 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DRONE GUI APPLICATION")
        self.setGeometry(500, 300, 500, 300)

        app =QApplication
        Window = Window()
        Window.show()
        sys.exit(app.exec)