from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QListWidget, QAbstractItemView, QSpacerItem, QSizePolicy, QListWidget, QListWidgetItem, QSpacerItem
from PySide2.QtCore import Qt, Signal, Slot

from vfxMikChainBridge.ui.step_widget import StepWidget


class StepsHandlerWidget(QWidget):
    def __init__(self, layout, parent=None):
        super(StepsHandlerWidget, self).__init__(parent)
        
        self.steps = []
        
        self.v_layout_main = QVBoxLayout(self)
        self.setLayout(self.v_layout_main)
        
        self.h_layout_button_bar = QHBoxLayout()

        self.lbl_title = QLabel('T E M P L A T E S')
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.v_layout_main.addWidget(self.lbl_title)

        self.cbx_templates = QComboBox()
        self.v_layout_main.addWidget(self.cbx_templates)

        self.v_layout_main.addLayout(self.h_layout_button_bar)

        self.btn_add = QPushButton('add')
        self.btn_add.setObjectName("addButton")
        self.btn_add.setToolTip("Add a new global variable")
        self.h_layout_button_bar.addWidget(self.btn_add)

        self.btn_clear = QPushButton('clear')
        self.btn_clear.setObjectName("deleteButton")
        self.btn_clear.setToolTip("Clear all global variables")
        self.h_layout_button_bar.addWidget(self.btn_clear)
        
        self.list_widget_steps = QListWidget()
        self.list_widget_steps.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.v_layout_main.addWidget(self.list_widget_steps)

        self.items_list = ["Template 1", "Template 2", "Template 3"]
        self.cbx_templates.addItems(self.items_list)
        layout.addWidget(self)
        
        self.fake_populate()

        self.adjust_size()

        
    def fake_populate(self):
        list_item_step_1 = QListWidgetItem()
        list_item_step_2 = QListWidgetItem()
        list_item_step_3 = QListWidgetItem()

        step_conform = StepWidget('COMFORM')
        step_make_artefactt = StepWidget('MAKE ARTEFACT')
        step_make_turn_table = StepWidget('MAKE TURN TABLE')

        list_item_step_1.setSizeHint(step_conform.sizeHint())
        list_item_step_2.setSizeHint(step_make_artefactt.sizeHint())
        list_item_step_3.setSizeHint(step_make_turn_table.sizeHint())

        self.list_widget_steps.addItem(list_item_step_1)
        self.list_widget_steps.addItem(list_item_step_2)
        self.list_widget_steps.addItem(list_item_step_3)

        self.list_widget_steps.setItemWidget(list_item_step_1, step_conform)
        self.list_widget_steps.setItemWidget(list_item_step_2, step_make_artefactt)
        self.list_widget_steps.setItemWidget(list_item_step_3, step_make_turn_table)


    @Slot()
    def adjust_size(self):
        """Adjust the size of the main window and its central widget."""
        self.adjustSize()