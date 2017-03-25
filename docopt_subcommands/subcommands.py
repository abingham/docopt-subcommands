from docopt import docopt

DEFAULT_DOC_TEMPLATE = """{program}

Usage: {program} [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.

Available commands:
  {available_commands}

See '{program} help <command>' for help on specific commands.
"""


class Subcommands:
    """A simple form of sub-command support for docopt.

    Fundamentally, you provide a mapping from command names to command
    handlers. This parses the command line, figures out the requested
    command, and routes execution to the mapped handler.
    Each subcommand handler should provide a docstring which will determine
    the docopt specification for that handler. This is used to generate the
    command-line parse for the subcommand, its help message, etc.

    Args:
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
        program: The name of the program.
        version: The version of the program.
    """

    def __init__(self,
                 program,
                 version,
                 doc_template=None):
        if doc_template is None:
            doc_template = DEFAULT_DOC_TEMPLATE

        self._doc_template = doc_template
        self._commands = {'help': self._handle_help}
        self.program = program

        self.version = version

    @property
    def top_level_doc(self):
        """The top-level documentation string for the program.
        """
        return self._doc_template.format(
            available_commands='\n  '.join(sorted(self._commands)),
            program=self.program)

    def command(self, name):
        """A decorator to add subcommands.
        """
        def decorator(f):
            self.add_command(name, f)
            return f
        return decorator

    def add_command(self, name, handler):
        """Add a subcommand `name` which invokes `handler`.
        """
        # TODO: Prevent overwriting 'help'?
        self._commands[name] = handler

    def __call__(self, argv):
        """Run the subcommand processor and invoke the necessary handler. You pass in
        some command line arguments. This then determines the correct handler
        and executes it. If no matching handler can be found, then a help
        message is shown. Also, command-specific help messages can be
        displayed.

        """
        # Parse top-level options, primarily looking for the sub-command to run.
        args = docopt(self.top_level_doc,
                      argv=argv,
                      options_first=True,
                      version=self.version)

        command = args['<command>']
        if command is None:
            command = 'help'

        # Try to find a command handler, defaulting to 'help' if no match it found.
        try:
            handler = self._commands[command]
        except KeyError:
            handler = self._handle_help
            argv = ['help']

        # Parse the sub-command options
        args = docopt(
            handler.__doc__.format(
                program=self.program,
                command=command),
            argv,
            version=self.version)

        # run the command
        return handler(args)

    def _handle_help(self, config):
        """usage: {program} {command} [<command>]
        Get the top-level help, or help for <command> if specified.
        """
        command = config['<command>']
        if not command:
            options = self.top_level_doc
        elif command not in self._commands:
            print('"{}}" is not a valid command', command)
            options = self.top_level_doc
        else:
            options = self._commands[command].__doc__

        return docopt(
            options.format(
                program=self.program,
                command=command),
            ['--help'],
            version=self.version)
