import os

from vfxMikChainBridge.infrastructure.utils import get_prod_root_env_variable

PROD_ROOT = get_prod_root_env_variable()
TEMPLATES_FOLDER = os.path.join(PROD_ROOT, "_admin/mikchain/templates/new_publish/executables")

MCEXEC = "mcexec"

if __name__ == "__main__":
    print('PROD_ROOT: ', PROD_ROOT)
    print('TEMPLATES_FOLDER: ', TEMPLATES_FOLDER)