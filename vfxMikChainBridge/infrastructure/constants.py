import os

from vfxMikChainBridge.infrastructure.utils import get_prod_root_env_variable

PROD_ROOT = get_prod_root_env_variable()
TEMPLATES_FOLDER = os.path.join(PROD_ROOT, "_admin/mikchain/templates/new_publish/executables")
MCEXEC = "mcexec"
