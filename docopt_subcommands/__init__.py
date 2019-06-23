from .subcommands import Subcommands
import sys


_commands = []
_non_command = None


def command(name=None):
    """A decorator to register a subcommand with the global `Subcommands` instance.
    """
    def decorator(f):
        _commands.append((name, f))
        return f
    return decorator


def non_command(f):
    global _non_command
    _non_command = f


def main(program=None,
         doc_template=None,
         commands=None,
         argv=None,
         exit_at_end=True):
    """Top-level driver for creating subcommand-based programs.

    Args: program: The name of your program. doc_template: The top-level docstring template for your program. If `None`,
        a standard default version is applied. commands: A `Subcommands` instance. argv: The command-line arguments to
        parse. If `None`, this defaults to `sys.argv[1:]` exit_at_end: Whether to call `sys.exit()` at the end of the
        function.

    There are two ways to use this function. First, you can pass `program` and `doc_template`, in which case
    `docopt_subcommands` will use these arguments along with the subcommands registered with `command()` to define you
    program.

    The second way to use this function is to pass in a `Subcommands` objects via the `commands` argument. In this case
    the `program` and `doc_template` arguments are ignored, and the `Subcommands` instance takes precedence.

    In both cases the `argv` argument can be used to specify the arguments to be parsed.

    """
    if commands is None:
        if program is None:
            raise ValueError(
                '`program` required if subcommand object not provided')
        commands = Subcommands(program,
                               doc_template=doc_template)
        for name, handler in _commands:
            commands.add_command(handler, name)

        if _non_command is not None:
            commands.set_non_command_handler(_non_command)

    if argv is None:
        argv = sys.argv[1:]

    result = commands(argv)
    if exit_at_end:
        sys.exit(result)
    else:
        return result
