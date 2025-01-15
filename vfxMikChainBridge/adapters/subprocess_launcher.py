import os
import subprocess

from vfxMikChainBridge.domain.ports.subprocess_runner import SubprocessRunnerPort


class SubprocessLauncherAdapter(SubprocessRunnerPort):
    
    @classmethod
    def get_environment(cls):
        """
        Returns a copy of the environment variables.
        """
        return os.environ.copy()

    @classmethod
    def run(cls,command, env=None):
        """
        Launches a subprocess with the given command and environment.
        """
        environment = env
        try:
            subprocess.Popen(
                [command],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=environment,
                shell=True
        )
            
        except Exception as e:
            print(f"Problem in subprocess execution: {e}")