import unittest
from unittest.mock import MagicMock, create_autospec

from vfxMikChainBridge.adapters.subprocess_runner import SubprocessRunnerAdapter

from vfxMikChainBridge.domain.templates_executor_service import TemplatesExecutorService


class TestTemplatesExecutorService(unittest.TestCase):
    def setUp(self):
        self.mock_templates_collector_service = MagicMock()
        self.mock_templates_collector_service.get_collected_templates.return_value = [
            MagicMock(absolute_file_path="/path/to/template1", global_variables={"KEY1": "VALUE1", "KEY2": "VALUE2"}),
            MagicMock(absolute_file_path="/path/to/template2", global_variables={"KEY3": "VALUE3"}),
        ]
        
        self.mock_subprocess_runner = create_autospec(SubprocessRunnerAdapter)
        self.binary_command = "fake_binary"
        self.executor_service = TemplatesExecutorService(
            self.mock_templates_collector_service,
            self.binary_command,
            self.mock_subprocess_runner,
        )

    def test_collect_templates(self):
        self.executor_service.collect_templates()
        self.mock_templates_collector_service.get_collected_templates.assert_called_once()
        self.assertEqual(len(self.executor_service.collected_templates), 2)

    def test_build_execution_command_from_global_variables(self):
        template = MagicMock(
            absolute_file_path="/path/to/template",
            global_variables={"KEY1": "VALUE1", "KEY2": "VALUE2"},
        )
        command = self.executor_service.build_execution_command_from_global_variables(template)
        expected_command = (
            "fake_binary /path/to/template --key1=value1 --key2=value2"
        )
        
        self.assertEqual(command, expected_command)

    def test_execute_templates(self):
        templates_collection = [
            MagicMock(absolute_file_path="/path/to/template1", global_variables={"KEY1": "VALUE1"}),
            MagicMock(absolute_file_path="/path/to/template2", global_variables={"KEY2": "VALUE2"}),
        ]
        self.executor_service.execute_templates(templates_collection)
        expected_calls = [
            unittest.mock.call("fake_binary /path/to/template1 --key1=value1"),
            unittest.mock.call("fake_binary /path/to/template2 --key2=value2"),
        ]
        self.mock_subprocess_runner.run.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(self.mock_subprocess_runner.run.call_count, len(templates_collection))


if __name__ == "__main__":
    unittest.main()
