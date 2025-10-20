import sys
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QSplitter, QTextEdit, QAction, QToolBar,
        QFileDialog, QDockWidget, QFormLayout, QLineEdit, QLabel, QWidget, QVBoxLayout
)
from PyQt5.QtCore import Qt

class AmanuensisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amanuensis - Transcription Application")
        self.setGeometry(100, 100, 800, 600)
        
        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        templates_menu = menubar.addMenu("Templates")

        # File Menu Actions
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Templates Menu (Placeholder)
        template_action = QAction("Apply Template", self)
        template_action.triggered.connect(self.apply_template)
        templates_menu.addAction(template_action)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        # Metadata Sidebar (Dock Widget)
        metadata_dock = QDockWidget("Metadata", self)
        metadata_widget = QWidget()
        metadata_layout = QFormLayout()
        self.plot_id = QLineEdit()
        self.last_name = QLineEdit()
        self.gps_coords = QLineEdit()
        metadata_layout.addRow(QLabel("Plot ID:"), self.plot_id)
        metadata_layout.addRow(QLabel("Last Name:"), self.last_name)
        metadata_layout.addRow(QLabel("GPS Coordinates:"), self.gps_coords)
        metadata_widget.setLayout(metadata_layout)
        metadata_dock.setWidget(metadata_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, metadata_dock)


        # Main Splitter (Editor Area)
        splitter = QSplitter(Qt.Horizontal)
        self.left_pane = QTextEdit("Transcription Editor")
        self.right_pane = QTextEdit("Preview or Notes")
        splitter.addWidget(self.left_pane)
        splitter.addWidget(self.right_pane)
        splitter.setSizes([400, 400])  # Initial sizes for panes

        # Set central widget
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(splitter)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def open_file(self):
        file_name, _ = QFieldDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'r') as file:
                self.left_pane.setText(file.read())
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.left_pane.toPlainText())

    def apply_template(self):
        # Placeholder for template functionality
        self.left_pane.setText("Applied template: [Sample Transcription Format]")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AmanuensisApp()
    window.show()
    sys.exit(app.exec_())
