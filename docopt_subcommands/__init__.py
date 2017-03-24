from .subcommands import Subcommands
import sys


def main(subc,
         argv=None,
         top_level_doc=None):
    """Top-level driver for creating subcommand-based programs.

    When docstrings are displayed, the following values are interpolated into
    them:

      {program}: The name of the program
      {version}: The program's version string
      {available_commands}: A comma-separated list of the available command names
      {command}: The current command (if applicable)

    When `top_level_doc` is displayed, the following values are interpolated
    into it:

      {program}: the name of the program
      {available_commands}: A comma-separated list of available command names.

    When subcommand docstrings are displayed, the following values are
    interpolated into them:

    Args:
      commands: A dict-like mapping from command names to subcommand handlers.
      program: The top-level name of your program.
      version: The version string for your program.
      argv: The command-line arguments to parse. If `None`, this defaults to
        `sys.argv[1:]`

      top_level_doc: The top-level docstring for your program. If `None`, a
        standard default version is applied.

    """
    if argv is None:
        argv = sys.argv[1:]

    sys.exit(subc(argv))
