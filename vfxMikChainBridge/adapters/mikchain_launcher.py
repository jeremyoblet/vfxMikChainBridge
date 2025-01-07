import os
import subprocess

from vfxMikChainBridge.domain.ports.subprocess_launcher import SubprocessLauncher


class MikChainLauncher(SubprocessLauncher):
    
    @classmethod
    def get_environment(cls):
        """
        Returns a copy of the environment variables.
        """
        return os.environ.copy()

    @classmethod
    def launch_subprocess(cls, command):
        """
        Launches a subprocess with the given command and environment.
        """
        environment = cls.get_environment()
        subprocess.Popen(
            [command],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=environment,
            shell=True
        )
