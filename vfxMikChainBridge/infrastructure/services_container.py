from ast import Sub
from vfxMikChainBridge.domain.template_processor_service import TemplateProcessorService
from vfxMikChainBridge.domain.templates_collector_service import TemplatesCollectorService
from vfxMikChainBridge.domain.templates_executor_service import TemplatesExecutorService
from vfxMikChainBridge.domain.templates_fetcher_service import TemplatesFetcherService

from vfxMikChainBridge.adapters.file_template_repository import FileTemplateRepository
from vfxMikChainBridge.adapters.subprocess_launcher import SubprocessLauncherAdapter
from vfxMikChainBridge.adapters.subprocess_runner import SubprocessRunnerAdapter


class ServicesContainer:
    def __init__(self, templates_folder, execution_command):
        self.templates_folder = templates_folder
        self.execution_command = execution_command
    
        self.template_repository = FileTemplateRepository(self.templates_folder)
        
        self.subprocess_runner = SubprocessRunnerAdapter()
        self.subprocess_launcher = SubprocessLauncherAdapter()
        
        self.templates_fetcher = TemplatesFetcherService(self.template_repository)
        self.processor_service = TemplateProcessorService(self.template_repository)
        self.collector_service = TemplatesCollectorService(self.processor_service)
        self.executor_service = TemplatesExecutorService(
            self.collector_service,
            self.execution_command,
            self.subprocess_runner
        )
