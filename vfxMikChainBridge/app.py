import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from vfxMikChainBridge.ui.user_interface import UserInterface
from vfxMikChainBridge.adapters.api import APIAdapter

from vfxMikChainBridge.infrastructure.services_container import ServicesContainer
from vfxMikChainBridge.infrastructure.constants import MCEXEC, TEMPLATES_FOLDER

def run():
    app = QApplication(sys.argv)
    app_window = QMainWindow()
    app_window.setWindowTitle("MikChain Bridge")
    services_container = ServicesContainer(TEMPLATES_FOLDER, MCEXEC)
    api = APIAdapter(services_container)
    main_widget = UserInterface(api)
    app_window.setCentralWidget(main_widget)
    app_window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    run()
