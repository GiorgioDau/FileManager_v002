from PySide2 import QtWidgets                            
import sys       
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance 
import os  


ASSET_PATH = "C:/Users/Gioxo/Documents/GitHub/FileManager_v002/assets"

def maya_main_window():
    maya_main_pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(maya_main_pointer), QtWidgets.QWidget)


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
        
        assets = self._list_asset()
        for asset in assets:
            self.asset_lw.addItem(asset)
        
        
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
        self.asset_lw.currentTextChanged.connect(self.update_departments_lw)
        self.department_lw.currentTextChanged.connect(self.update_versions_lw)
        self.asset_lw.setCurrentRow(0)

        

    def _list_asset(self) -> list:
        if not os.path.exists(ASSET_PATH):
            os.mkdir(ASSET_PATH)
            return[]
        else:
            print(os.listdir(ASSET_PATH))
            return os.listdir(ASSET_PATH)

    def _list_departments(self) -> list:
        current_asset = self.asset_lw.currentItem().text()
        asset_path = os.path.join(ASSET_PATH, current_asset)
        return os.listdir(asset_path)

    def _list_versions(self) -> list:
        current_asset = self.asset_lw.currentItem().text()
        print("list_version")
        current_department_item = self.department_lw.currentItem()
        current_department = current_department_item.text()
        department_path = os.path.join(ASSET_PATH, current_asset, current_department)
        return os.listdir(department_path)

    def update_departments_lw(self):

        self.department_lw.currentTextChanged.disconnect(self.update_versions_lw)
        self.department_lw.clear()
        departments = self._list_departments()
        for department in departments:
            self.department_lw.addItem(department)

        self.department_lw.currentTextChanged.connect(self.update_versions_lw)    
        self.department_lw.setCurrentRow(0)

    def update_versions_lw(self):
        self.version_lw.clear()
        versions = self._list_versions()
        for version in versions:
            self.version_lw.addItem(version)
        self.version_lw.setCurrentRow(0)







print(__name__)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv) 
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
