name = "vfxMikChainBridge"
version = "0.0.1"

requires = [
    "python-2.7+<4",
    "vfxLogs-1|dev",
    "pyside2-5.15",
]

custom = {
    "description": "Bridge between BasicBrowser and MikChain",
    "wiki": "",
    "authors": ["oblet-joffrej"],
    "maintainers": ["oblet-joffrej"],
}

private_build_requires = ["cmake-3", "sphinx-7.0", "sphinx_rtd_theme", "coreQt"]



def pre_commands():
    info("Using {this.name}-{this.version}")


def pre_test_commands():
    import  os
    env.PYTHONPATH.append("tests")


def commands():
    import os

    env.PYTHONPATH.append("{base}")
