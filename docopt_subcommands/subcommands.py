import textwrap

from docopt import docopt

DEFAULT_DOC_TEMPLATE = """{program}

Usage: {program} [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.

Available commands:
  {available_commands}

See '{program} <command> -h' for help on specific commands.
"""


def dedent(s):
    """Removes the hanging dedent from all the first line of a string."""
    head, _, tail = s.partition('\n')
    dedented_tail = textwrap.dedent(tail)
    result = "{head}\n{tail}".format(
        head=head,
        tail=dedented_tail)
    return result


def docstring_to_subcommand(docstring):
    usage = [l for l in docstring.split() if l]
    if len(usage) < 3:
        raise ValueError(
            "Subcommand docstring must start with 'usage: {program} <subcommand>'")
    if usage[0] != 'usage:':
        raise ValueError(
            "Subcommand docstring must start with 'usage: {program} <subcommand>'")
    return usage[2]


class Subcommands:
    """A simple form of sub-command support for docopt.

    Fundamentally, you provide a mapping from command names to command
    handlers. This parses the command line, figures out the requested
    command, and routes execution to the mapped handler.
    Each subcommand handler should provide a docstring which will determine
    the docopt specification for that handler. This is used to generate the
    command-line parse for the subcommand, its help message, etc.

    Args:
        program: The name of the program.

        doc_template: The top-level documentation string for your program.
            This is passed to docopt for generating the top-level command line
            parser. It *must* contain a "<command>" entry in the command line
            where the subcommand is specified. Optionally it can contain an
            "{available_commands}" string interpolation placeholder where
            available commands will be displayed in help output.

        commands: A dict mapping commands names to handler function. A handler
            will be invoked when its corresponding command name is requested by
            the user. It will be invoked with the configuration parsed by
            docopt for handler's docstring.
    """

    def __init__(self,
                 program,
                 doc_template=None):
        if doc_template is None:
            doc_template = DEFAULT_DOC_TEMPLATE

        self._doc_template = doc_template
        self._commands = {}
        self._non_command_handler = lambda _: 0
        self.program = program

    @property
    def top_level_doc(self):
        """The top-level documentation string for the program.
        """
        return self._doc_template.format(
            available_commands='\n  '.join(sorted(self._commands)),
            program=self.program)

    def command(self, name=None):
        """A decorator to add subcommands.
        """
        def decorator(f):
            self.add_command(f, name)
            return f
        return decorator

    def add_command(self, handler, name=None):
        """Add a subcommand `name` which invokes `handler`.
        """
        if name is None:
            name = docstring_to_subcommand(handler.__doc__)

        # TODO: Prevent overwriting 'help'?
        self._commands[name] = handler
        
    def set_non_command_handler(self, handler):
        self._non_command_handler = handler

    def __call__(self, argv):
        """Run the subcommand processor and invoke the necessary handler.

        You pass in some command line arguments. This then determines the
        correct handler and executes it. If no matching handler can be found,
        then a help message is shown. Also, command-specific help messages can
        be displayed.
        """
        # Parse top-level options, primarily looking for the sub-command to run.
        common_config = docopt(self.top_level_doc,
                               argv=argv,
                               options_first=True)

        command = common_config['<command>']
        if command is None:
            return self._non_command_handler(common_config)

        # Try to find a command handler, defaulting to 'help' if no match it found.
        try:
            handler = self._commands[command]
            argv = [command] + common_config['<args>']
        except KeyError:
            print('"{}" is not a valid command.\n'.format(command))
            return self(['-h'])

        # Parse the sub-command options
        command_config = docopt(
            dedent(
                handler.__doc__.format(
                    program=self.program,
                    command=command)),
            argv)

        # run the command
        return handler(common_config, command_config)
