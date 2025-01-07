from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QListWidget, QAbstractItemView, QCheckBox, QListWidgetItem, QLineEdit, QSizePolicy
from PySide2.QtCore import Qt
from PySide2.QtCore import QPropertyAnimation, QEasingCurve
from PySide2.QtCore import Signal, Slot

class VariableWidget(QWidget):
    def __init__(self, variable_name, variable_value, variable_type, parent=None):
        super(VariableWidget, self).__init__(parent)
        
        self.variable_name = variable_name
        self.variable_value = variable_value
        self.variable_type = variable_type
        
        self.h_layout_variables = QHBoxLayout()
        self.setLayout(self.h_layout_variables)
        
        self.lbl_variable_name = QLabel(self.variable_name)
        self.line_edit_variable_value = QLineEdit()
        self.line_edit_variable_value.setText(self.variable_value)
        # self.cmb_box_variable_type = QComboBox()
        self.line_edit_variable_type = QLineEdit()
        self.line_edit_variable_type.setText(self.variable_type)

        self.h_layout_variables.addWidget(self.lbl_variable_name)
        self.h_layout_variables.addWidget(self.line_edit_variable_value)
        self.h_layout_variables.addWidget(self.line_edit_variable_type)
        
    @Slot()
    def adjust_size(self):
        """Adjust the size of the main window and its central widget."""
        self.adjustSize()
        
class VariableListWidget(QListWidget):
    
    def __init__(self, parent=None):
        super(VariableListWidget, self).__init__(parent)
        
        self.variable_1 = VariableWidget('ASSET_TYPE', 'character', 'str')
        self.variable_2 = VariableWidget('ASSET_NAME', 'blackwolf', 'bool')
        self.variable_3 = VariableWidget('TASK', 'mod', 'str')
        
        self.add_variable(self.variable_1)
        self.add_variable(self.variable_2)
        self.add_variable(self.variable_3)
        
    def add_variable(self, global_variable):        
        list_item_step_1 = QListWidgetItem()
        step_vars = global_variable
        list_item_step_1.setSizeHint(step_vars.sizeHint())
        self.addItem(list_item_step_1)
        self.setItemWidget(list_item_step_1, step_vars)


        
class StepWidget(QWidget):
    def __init__(self, name, parent=None):
        super(StepWidget, self).__init__(parent)
        
        self.v_layout_main = QVBoxLayout()
        self.setLayout(self.v_layout_main)
        
        self.header_widget = QWidget()
        self.h_layout_header = QHBoxLayout()
        self.header_widget.setLayout(self.h_layout_header)
        
        self.chk_box_step_activation = QCheckBox()
        self.btn_step_title = QPushButton(name)
        self.cmb_box_execution_mode = QComboBox()
        self.execution_modes_list = ["Farm", "Local", "Dry run"]
        self.cmb_box_execution_mode.addItems(self.execution_modes_list)
        self.btn_step_template_open = QPushButton('open')
        self.btn_step_remove = QPushButton('remove')
        
        self.h_layout_header.addWidget(self.chk_box_step_activation)
        self.h_layout_header.addWidget(self.btn_step_title)
        self.h_layout_header.addWidget(self.cmb_box_execution_mode)
        self.h_layout_header.addWidget(self.btn_step_template_open)
        self.h_layout_header.addWidget(self.btn_step_remove)

        self.titles_widget = QWidget()
        self.h_layout_titles = QHBoxLayout()
        self.titles_widget.setLayout(self.h_layout_titles)
        
        self.lbl_variable_name = QLabel('variable name')
        self.lbl_variable_value = QLabel('variable value')
        self.lbl_variable_type = QLabel('variable type')
        
        self.h_layout_titles.addWidget(self.lbl_variable_name)
        self.h_layout_titles.addWidget(self.lbl_variable_value)
        self.h_layout_titles.addWidget(self.lbl_variable_type)

        self.list_widget_global_variable = VariableListWidget()
        self.list_widget_global_variable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.v_layout_main.addWidget(self.header_widget)
        self.v_layout_main.addWidget(self.titles_widget)
        self.v_layout_main.addWidget(self.list_widget_global_variable)
        
        self.btn_step_title.clicked.connect(self.toggle_expansion)

    def toggle_expansion(self):
        self.list_widget_global_variable.setVisible(not self.list_widget_global_variable.isVisible())

