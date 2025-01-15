from PySide2.QtWidgets import QPushButton, QVBoxLayout, QWidget, QFrame

from vfxMikChainBridge.ui.components.preset_manager_widget import PresetLoaderWidget
from vfxMikChainBridge.ui.components.templates_collector_widget import TemplateCollectorWidget


class UserInterface(QWidget):
    def __init__(self, api, parent=None):
        super(UserInterface, self).__init__(parent)
        self.api = api

        self.v_layout_main = QVBoxLayout()
        self.setLayout(self.v_layout_main)
        
        self.preset_loader_widget = PresetLoaderWidget(self.v_layout_main)
        
        self.separator_1 = QFrame()
        self.separator_1.setFrameShape(QFrame.HLine)
        self.separator_1.setFrameShadow(QFrame.Sunken)
        self.v_layout_main.addWidget(self.separator_1)

        self.templates_collector_widget = TemplateCollectorWidget(self.api, self.v_layout_main)

        self.btn_run_all_steps = QPushButton("Run all")
        self.btn_run_all_steps.clicked.connect(self.execute_templates)
        self.v_layout_main.addWidget(self.btn_run_all_steps)
        
        self.separator_2 = QFrame()
        self.separator_2.setFrameShape(QFrame.HLine)
        self.separator_2.setFrameShadow(QFrame.Sunken)
        self.v_layout_main.addWidget(self.separator_2)
        
        self.btn_launch_mikchain = QPushButton("Open new MikChain")
        self.btn_launch_mikchain.clicked.connect(self.launch_mikchain)
        self.v_layout_main.addWidget(self.btn_launch_mikchain)

    def execute_templates(self):
        self.api.execute_templates()
    
    def launch_mikchain(self):
        self.api.launch_new_empty_mikchain()
