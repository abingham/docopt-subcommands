from .subcommands import Subcommands
import sys


_commands = []


def command(name=None):
    """A decorator to register a subcommand with the global `Subcommands` instance.
    """
    def decorator(f):
        _commands.append((name, f))
        return f
    return decorator


def main(program=None,
         version=None,
         doc_template=None,
         common_option_handler=None,
         commands=None,
         argv=None,
         exit_at_end=True):
    """Top-level driver for creating subcommand-based programs.

    Args:
        program: The name of your program.
        version: The version string for your program.
        doc_template: The top-level docstring template for your program. If
            `None`, a standard default version is applied.
        common_option_handler: A callable to handle any options which apply to
            the top-level command.
        commands: A `Subcommands` instance.
        argv: The command-line arguments to parse. If `None`, this defaults to
            `sys.argv[1:]`
        exit_at_end: Whether to call `sys.exit()` at the end of the function.

    There are two ways to use this function. First, you can pass `program`,
    `version`, and `doc_template`, in which case `docopt_subcommands` will use
    these arguments along with the subcommands registered with `command()` to
    define you program.

    The second way to use this function is to pass in a `Subcommands` objects
    via the `commands` argument. In this case the `program`, `version`, and
    `doc_template` arguments are ignored, and the `Subcommands` instance takes
    precedence.

    In both cases the `argv` argument can be used to specify the arguments to
    be parsed.

    """
    if commands is None:
        if program is None:
            raise ValueError(
                '`program` required if subcommand object not provided')
        if version is None:
            raise ValueError(
                '`version` required if subcommand object not provided')
        commands = Subcommands(program,
                               version,
                               doc_template=doc_template,
                               common_option_handler=common_option_handler)
        for name, handler in _commands:
            commands.add_command(handler, name)

    if argv is None:
        argv = sys.argv[1:]

    result = commands(argv)
    if exit_at_end:
        sys.exit(result)
    else:
        return result
