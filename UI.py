from PySide2 import QtWidgets                            
import sys       
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance   

def maya_main_window():
    maya_main_pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(maya_main_pointer), QtWidgets.QWidget)

#class TestWindow(QtWidgets.QMainWindow):
class TestWindow(QtWidgets.QDialog):    
    def __init__(self):
        super().__init__(maya_main_window())

        self.setWindowTitle('File manager')     
        self.setMinimumWidth(500)              
        self.setMinimumHeight(500)

        self._create_widgets()
        self._create_layouts()
        self._create_connections()

    def _create_widgets(self):

        self.asset_lw = QtWidgets.QListWidget()
        self.department_lw = QtWidgets.QListWidget()
        self.version_lw = QtWidgets.QListWidget()
        

        self.version_label = QtWidgets.QLabel("Version Info:")
        
        self.open_btn = QtWidgets.QPushButton("Open")
        self.import_btn = QtWidgets.QPushButton("Import")
        self.reference_btn = QtWidgets.QPushButton("Reference")
        self.save_btn = QtWidgets.QPushButton("SAVE")

        

        

    def _create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        lw_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(lw_layout)

        for lw in (self.asset_lw,
                   self.department_lw,
                   self.version_lw):
            lw_layout.addWidget(lw)

        main_layout.addWidget(self.version_label)

        button_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)

        for btn in (self.open_btn,
                   self.import_btn,
                   self.reference_btn,
                   self.save_btn):
            button_layout.addWidget(btn)


        

    def _create_connections(self):
        print("connections")

print(__name__)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv) 
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
