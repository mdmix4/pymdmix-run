from argparse import ArgumentParser, Namespace
from pymdmix_core.plugin.base import Plugin


class RunPlugin(Plugin):

    NAME = "run"
    HELP_STRING: str = ""
    LOAD_CONFIG: bool = False
    CONFIG_FILE: str = ""
    ALLOW_EMPTY_ACTION = True

    def __init__(self, master_parser: ArgumentParser) -> None:
        super().__init__(master_parser)

    def init_actions(self, action_subparser):
        return super().init_actions(action_subparser)

    def init_parser(self) -> None:
        return super().init_parser()

    def run(self, args: Namespace) -> None:
        return super().run(args)
