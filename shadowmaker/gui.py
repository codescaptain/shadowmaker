import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from image_processor import process_image

class SilhouetteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Silhouette Creator')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.select_button = QPushButton('Select File', self)
        self.select_button.clicked.connect(self.showFileDialog)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def showFileDialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select an Image File", "",
                                                   "Image Files (*.jpg *.jpeg *.png *.bmp *.tiff)", options=options)
        if file_path:
            process_image(file_path)

def main():
    print("Starting the application...")  # Debugging print
    app = QApplication(sys.argv)
    ex = SilhouetteApp()
    print("App created, showing the window...")  # Debugging print
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
