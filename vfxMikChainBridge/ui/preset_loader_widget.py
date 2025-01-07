from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QListWidget, QAbstractItemView
from PySide2.QtCore import Qt


class PresetLoaderWidget(QWidget):
    def __init__(self, layout, parent=None):
        super(PresetLoaderWidget, self).__init__(parent)

        self.v_layout_main = QVBoxLayout()
        self.setLayout(self.v_layout_main)

        self.lbl_title = QLabel('P R E S E T S')
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.v_layout_main.addWidget(self.lbl_title)
        
        self.btn_create_new_preset = QPushButton('New preset')
        self.btn_save_preset = QPushButton('Save preset')

        self.h_preset_widget_layout = QHBoxLayout()
        self.cbx_presets = QComboBox()
        self.btn_load_preset = QPushButton('Load preset')
        
        self.h_preset_widget_layout.addWidget(self.cbx_presets)
        self.h_preset_widget_layout.addWidget(self.btn_load_preset)
        
        self.v_layout_main.addWidget(self.btn_create_new_preset)
        self.v_layout_main.addWidget(self.btn_save_preset)
        self.v_layout_main.addLayout(self.h_preset_widget_layout)

        self.items_list = ["Preset 1", "Preset 2", "Preset 3"]
        self.cbx_presets.addItems(self.items_list)
        
        layout.addWidget(self)
