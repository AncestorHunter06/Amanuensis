import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QTextEdit, QWidget
from PyQt5.QtCore import Qt

class AmanuensisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amanuensis")
        self.setGeometry(100, 100, 800, 600)

        # Create a horizontal splitter
        splitter = QSplitter(Qt.Horizontal)
        self.left_pane = QTextEdit("Left Pane")
        self.right_pane = QTextEdit("Right Pane")
        splitter.addWidget(self.left_pane)
        splitter.addWidget(self.right_pane)

        # Set splitter as central widget
        self.setCentralWidget(splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AmanuensisApp()
    window.show()
    sys.exit(app.exec_())
