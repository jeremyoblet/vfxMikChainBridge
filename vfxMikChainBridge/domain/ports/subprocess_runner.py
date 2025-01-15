from abc import ABC, abstractmethod


class SubprocessRunnerPort(ABC):
    
    @classmethod
    @abstractmethod
    def get_environment(cls):
        """
        Get the needed environment to run the subprocess.
        """
        pass
    
    @classmethod
    @abstractmethod
    def run(cls, command, env=None):
        """
        Run the command in a subprocess with the needed environment.

        Args:
            command (str): The command to run in the subprocess.
            environment (dict): The needed environment to run the subprocess correctly.
        """
        pass
