import os
import subprocess

from vfxMikChainBridge.domain.ports.subprocess_runner import SubprocessRunnerPort


class SubprocessRunnerAdapter(SubprocessRunnerPort):
    
    @classmethod
    def get_environment(cls):
        """
        Returns a copy of the environment variables.
        """
        return os.environ.copy()

    @classmethod
    def run(cls, command, env=None):
        """
        Runs a subprocess with the given command and environment.
        """
        environment = env
        try:
            process = subprocess.Popen(
                [command],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=environment,
                shell=True
            )
            
            stdout, stderr = process.communicate()
            print("STDOUT:")
            print(stdout)
            print("STDERR:")
            print(stderr)
            
        except Exception as e:
            print(f"Problem in subprocess execution: {e}")