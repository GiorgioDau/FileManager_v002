from PySide6 import QtWidgets
import sys

class TestWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TestWindow')     
        self.setMinimumWidth(500)              
        self.setMinimumHeight(500)
        self._create_widgets()
        self._create_layouts()
        self._create_connections()

    def _create_widgets(self):
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.message_label = QtWidgets.QLabel("Message")
        self.line_edit = QtWidgets.QLineEdit("Inserisci il tuo messaggio qui")
        self.button = QtWidgets.QPushButton("Send Message")
        self.output_label = QtWidgets.QLabel("test")

        

    def _create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(main_layout) 

        horizontal_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(horizontal_layout)
        
        #for....
        horizontal_layout.addWidget(self.message_label)
        horizontal_layout.addWidget(self.line_edit)

        main_layout.addWidget(self.button)
        main_layout.addWidget(self.output_label)


        

    def _create_connections(self):
        print("connections")

app = QtWidgets.QApplication(sys.argv) 
window = TestWindow()
window.show()
sys.exit(app.exec())
