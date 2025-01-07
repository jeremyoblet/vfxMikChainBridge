from abc import ABC, abstractmethod


class SubprocessLauncher(ABC):
    
    @classmethod
    @abstractmethod
    def get_environment(cls):
        """
        Get the needed environment to run the subprocess.
        """
        pass
    
    @classmethod
    @abstractmethod
    def launch_subprocess(cls, environment, command):
        """
        Run the command in a subprocess with the needed environment.

        Args:
            command (str): The command to run in the subprocess.
            environment (dict): The needed environment to run the subprocess correctly.
        """
        pass
