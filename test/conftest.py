import docopt_subcommands as dsc
from pytest import fixture


@fixture()
def reset_commands():
    "Resets all existing docopt-subcommands commands."
    dsc._commands = []

