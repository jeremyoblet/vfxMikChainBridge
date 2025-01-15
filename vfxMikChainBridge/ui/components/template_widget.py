from PySide2.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QListWidget, QListWidgetItem, QLineEdit, QSizePolicy


class TemplateGlobalVariableWidget(QWidget):
    def __init__(self, variable_name, variable_value, variable_type, parent=None):
        super(TemplateGlobalVariableWidget, self).__init__(parent)
        
        self.variable_name = str(variable_name)
        self.variable_value = str(variable_value)
        self.variable_type = str(variable_type)
        
        self.h_layout_variables = QHBoxLayout()
        self.setLayout(self.h_layout_variables)
        
        self.lbl_variable_name = QLabel(self.variable_name)
        self.line_edit_variable_value = QLineEdit()
        self.line_edit_variable_value.setText(self.variable_value)
        self.line_edit_variable_type = QLineEdit()
        self.line_edit_variable_type.setText(self.variable_type)

        self.h_layout_variables.addWidget(self.lbl_variable_name)
        self.h_layout_variables.addWidget(self.line_edit_variable_value)
        self.h_layout_variables.addWidget(self.line_edit_variable_type)
        
        
class TemplateGlobalVariablesListWidget(QListWidget):
    
    def __init__(self, global_variables, parent=None):
        super(TemplateGlobalVariablesListWidget, self).__init__(parent)

        for var in global_variables:
            new_var = TemplateGlobalVariableWidget(var.name, var.value, var.type)
            self.add_variable(new_var)
            
    def add_variable(self, global_variable):        
        list_item_template_1 = QListWidgetItem()
        template_vars = global_variable
        list_item_template_1.setSizeHint(template_vars.sizeHint())
        self.addItem(list_item_template_1)
        self.setItemWidget(list_item_template_1, template_vars)
 
        
class TemplateWidget(QWidget):
    def __init__(self, api, template_name, parent=None):
        super(TemplateWidget, self).__init__(parent)
        self.api = api
        self.global_variables = self.api.get_global_variables_from_template_name(template_name)
        
        self.v_layout_main = QVBoxLayout()
        self.setLayout(self.v_layout_main)
        
        self.header_widget = QWidget()
        self.h_layout_header = QHBoxLayout()
        self.header_widget.setLayout(self.h_layout_header)
        
        self.btn_template_title = QPushButton(template_name)
        self.v_layout_main.addWidget(self.btn_template_title)

        self.titles_widget = QWidget()
        self.h_layout_titles = QHBoxLayout()
        self.titles_widget.setLayout(self.h_layout_titles)
        
        self.lbl_variable_name = QLabel('variable name')
        self.lbl_variable_value = QLabel('variable value')
        self.lbl_variable_type = QLabel('variable type')
        
        self.h_layout_titles.addWidget(self.lbl_variable_name)
        self.h_layout_titles.addWidget(self.lbl_variable_value)
        self.h_layout_titles.addWidget(self.lbl_variable_type)

        self.v_layout_main.addWidget(self.titles_widget)


        self.list_widget_global_variable = TemplateGlobalVariablesListWidget(self.global_variables)
        self.list_widget_global_variable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.v_layout_main.addWidget(self.list_widget_global_variable)
        