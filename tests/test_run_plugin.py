import os
from pymdmix_core.plugin.base import PluginManager, MDMIX_PLUGIN_MANAGER
from unittest.mock import patch
import pytest
from .conftest import FPATH, run_command


def test_plugin_manager_load_run_plugin():
    plugin_manager = PluginManager()
    plugin_manager.load_plugin("pymdmix_run")

    assert "run" in plugin_manager.plugins


@pytest.mark.parametrize("times", range(1, 3))
def test_run_plugin_on_files(capfd, times):
    input_file = os.path.join(FPATH, "test.mdmix")
    plugin_manager = MDMIX_PLUGIN_MANAGER
    plugin_manager.load_plugin("pymdmix_core")
    plugin_manager.load_plugin("pymdmix_run")
    command = ["run"] + times * [input_file]
    run_command(" ".join(command), plugin_manager)
    out, _  = capfd.readouterr()
    out = out.split("\n")
    assert out.count("\t- plugin") == times
    assert out.count("\t- run") == times


@patch("pymdmix_run.run.sys.stdin", open(os.path.join(FPATH, "test.mdmix"), 'r'))
def test_run_plugin_on_stdin(capfd):
    plugin_manager = MDMIX_PLUGIN_MANAGER
    plugin_manager.load_plugin("pymdmix_core")
    plugin_manager.load_plugin("pymdmix_run")
    run_command("run", plugin_manager)
    out, _  = capfd.readouterr()
    out = out.split("\n")
    assert out.count("\t- plugin") == 1
    assert out.count("\t- run") == 1
