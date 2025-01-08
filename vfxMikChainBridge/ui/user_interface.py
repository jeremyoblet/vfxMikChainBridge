from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QListWidget, QAbstractItemView, QFrame
from PySide2.QtCore import Qt

from vfxMikChainBridge.adapters.mikchain_launcher import MikChainLauncher
from vfxMikChainBridge.adapters.api import APIAdapter

from vfxMikChainBridge.ui.components.preset_manager_widget import PresetLoaderWidget
from vfxMikChainBridge.ui.components.templates_collector_widget import TemplateCollectorWidget


class UserInterface(QWidget):
    def __init__(self, api, parent=None):
        super(UserInterface, self).__init__(parent)
        # self.setGeometry(100, 100, 300, 200)
        self.api = api

        self.v_layout_main = QVBoxLayout()
        self.setLayout(self.v_layout_main)
        
        # self.preset_loader_widget = PresetLoaderWidget(self.v_layout_main )
        
        # self.separator_1 = QFrame()
        # self.separator_1.setFrameShape(QFrame.HLine)
        # self.separator_1.setFrameShadow(QFrame.Sunken)
        # self.v_layout_main.addWidget(self.separator_1)

        self.templates_collector_widget = TemplateCollectorWidget(self.api, self.v_layout_main)

        self.btn_run_all_steps = QPushButton("Run all")
        self.v_layout_main.addWidget(self.btn_run_all_steps)
        
        self.separator_2 = QFrame()
        self.separator_2.setFrameShape(QFrame.HLine)
        self.separator_2.setFrameShadow(QFrame.Sunken)
        self.v_layout_main.addWidget(self.separator_2)
        
        self.btn_launch_mikchain = QPushButton("Open new MikChain")
        self.btn_launch_mikchain.clicked.connect(self.launch_mikchain)
        self.v_layout_main.addWidget(self.btn_launch_mikchain)
    
        
    def launch_mikchain(self):
        mikchain_launcher = MikChainLauncher()
        mikchain_launcher.launch_subprocess("mikchain --template auto_turntable_base")
        # mikchain_launcher.launch_subprocess("mikchain")
