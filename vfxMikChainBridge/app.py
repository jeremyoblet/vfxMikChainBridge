import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from vfxMikChainBridge.ui.user_interface import UserInterface
from vfxMikChainBridge.adapters.api import APIAdapter

from vfxMikChainBridge.domain.template_processor_service import TemplateProcessorService
from vfxMikChainBridge.domain.templates_collector_service import TemplatesCollectorService
from vfxMikChainBridge.domain.templates_executor_service import TemplatesExecutorService
from vfxMikChainBridge.domain.templates_fetcher_service import TemplatesFetcherService

def run():
    app = QApplication(sys.argv)
    app_window = QMainWindow()
    app_window.setWindowTitle("MikChain Bridge")
    templates_collector = TemplatesCollectorService()
    templates_fetcher = TemplatesFetcherService()
    api = APIAdapter(templates_collector, templates_fetcher)
    main_widget = UserInterface(api)
    app_window.setCentralWidget(main_widget)
    app_window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    run()
