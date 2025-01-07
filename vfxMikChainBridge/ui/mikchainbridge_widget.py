from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QListWidget, QAbstractItemView, QFrame
from PySide2.QtCore import Qt

from vfxMikChainBridge.adapters.mikchain_launcher import MikChainLauncher

from vfxMikChainBridge.ui.preset_loader_widget import PresetLoaderWidget
from vfxMikChainBridge.ui.steps_handler_widget import StepsHandlerWidget


class MikChainBridgeWidget(QWidget):
    def __init__(self, parent=None):
        super(MikChainBridgeWidget, self).__init__(parent)
        # self.setGeometry(100, 100, 300, 200)
        
        self.v_layout_main = QVBoxLayout()
        self.setLayout(self.v_layout_main)
        
        self.preset_loader_widget = PresetLoaderWidget(self.v_layout_main )
        
        self.separator_1 = QFrame()
        self.separator_1.setFrameShape(QFrame.HLine)
        self.separator_1.setFrameShadow(QFrame.Sunken)
        self.v_layout_main.addWidget(self.separator_1)

        self.step_handler_widget = StepsHandlerWidget(self.v_layout_main)

        self.btn_run_all_steps = QPushButton("Run all")
        self.v_layout_main.addWidget(self.btn_run_all_steps)
        
        self.separator_2 = QFrame()
        self.separator_2.setFrameShape(QFrame.HLine)
        self.separator_2.setFrameShadow(QFrame.Sunken)
        self.v_layout_main.addWidget(self.separator_2)
        
        self.btn_launch_mikchain = QPushButton("Open new MikChain")
        self.btn_launch_mikchain.clicked.connect(self.on_button_click)
        self.v_layout_main.addWidget(self.btn_launch_mikchain)
        
        
        
    def on_button_click(self):
        mikchain_launcher = MikChainLauncher()
        mikchain_launcher.launch_subprocess_with_rez_env("mikchain --template auto_turntable_base")
        # mikchain_launcher.launch_subprocess_with_rez_env("mikchain")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("MikChain Bridge")
    main_widget = MikChainBridgeWidget()
    main_window.setCentralWidget(main_widget)
    main_window.show()
    sys.exit(app.exec_())
