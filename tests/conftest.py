import os
import shlex
from typing import Optional

from pymdmix_core.plugin import PluginManager
from pymdmix_core.parser import get_mdmix_parser


FPATH = os.path.join("tests", "fixtures")
PLUGIN_PACKAGE = "pymdmix_run"
PLUGIN_NAME = "run"


def get_plugin_manager():
    plugin_manager = PluginManager(get_mdmix_parser())
    plugin_manager.load_plugin(PLUGIN_PACKAGE)
    return plugin_manager


def run_command(command: str, plugin_manager: Optional[PluginManager] = None):
    plugin_manager = plugin_manager if plugin_manager is not None else get_plugin_manager()
    args = plugin_manager.parser.parse_args(shlex.split(command))
    plugin = plugin_manager.plugins[PLUGIN_NAME]
    plugin.run(args)
