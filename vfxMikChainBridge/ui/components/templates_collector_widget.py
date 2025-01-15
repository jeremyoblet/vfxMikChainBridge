from pathlib import Path

from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QListWidget, QAbstractItemView, QListWidget, QListWidgetItem
from PySide2.QtCore import Qt

from vfxMikChainBridge.ui.components.template_widget import TemplateWidget


class TemplateCollectorWidget(QWidget):
    def __init__(self, api, layout, parent=None):
        super(TemplateCollectorWidget, self).__init__(parent)
        
        self.api = api
        
        self.steps = []
        
        self.v_layout_main = QVBoxLayout(self)
        self.setLayout(self.v_layout_main)
        
        self.h_layout_button_bar = QHBoxLayout()

        # Title
        self.lbl_title = QLabel('T E M P L A T E S')
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.v_layout_main.addWidget(self.lbl_title)

        # Available templates
        self.cbx_templates = QComboBox()
        self.v_layout_main.addWidget(self.cbx_templates)
        
        # Populate combobox with templates
        self.api.populate_available_templates()
        self.available_templates = self.api.get_available_templates()
        self.available_templates_names = [Path(template).stem for template in self.available_templates]
        self.cbx_templates.addItems(self.available_templates_names)
        
        self.v_layout_main.addLayout(self.h_layout_button_bar)

        # Add button
        self.btn_add = QPushButton('add')
        self.btn_add.setObjectName("addButton")
        self.btn_add.setToolTip("Add a new global variable")
        self.btn_add.clicked.connect(self.add_template_in_collector)
        self.h_layout_button_bar.addWidget(self.btn_add)

        # Clear button
        self.btn_clear = QPushButton('clear')
        self.btn_clear.setObjectName("deleteButton")
        self.btn_clear.setToolTip("Clear all global variables")
        self.btn_clear.clicked.connect(self.clear_collected_templates)
        self.h_layout_button_bar.addWidget(self.btn_clear)
        
        # List widget
        self.list_widget_steps = QListWidget()
        self.list_widget_steps.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.v_layout_main.addWidget(self.list_widget_steps)
        
        layout.addWidget(self)
        """Adjust the size of the main window and its central widget."""
        self.adjustSize()
        
    def add_template_in_collector(self):
        """
        Add a new item to the list widget based on the selected combobox template
        and add it to the backend via the API.
        """
        selected_template_name = self.cbx_templates.currentText()
        
        for template_path in self.available_templates:
            if selected_template_name in template_path:
                self.api.add_template_in_collection(template_path)
                
        print(f"Added template to backend: {selected_template_name}")
        print("Collected templates in backend:", self.api.get_collected_templates())

        template_widget = TemplateWidget(self.api, selected_template_name)

        list_item = QListWidgetItem(self.list_widget_steps)
        list_item.setSizeHint(template_widget.sizeHint())
        self.list_widget_steps.addItem(list_item)
        self.list_widget_steps.setItemWidget(list_item, template_widget)
        print(f"Added template to UI: {selected_template_name}")

    def clear_collected_templates(self):
        """
        Clear all items in the list widget.
        """
        self.list_widget_steps.clear()
        self.api.clear_collection()
        print("All templates cleared.")
