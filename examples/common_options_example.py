# Example showing how to handle common top-level options.

import docopt_subcommands as dsc


# 1. Use the `command` decorator to add subcommands functions.
@dsc.command('foo')
def foo_handler(args):
    """usage: {program} {command} <name>

    Apply foo to a name.
    """
    print("Foo, {}".format(args['<name>']))


@dsc.command('bar')
def bar_handler(args):
    """usage: {program} {command} <name>

    Apply bar to a name.
    """
    print("Bar, {}".format(args['<name>']))


# 2. Provide a custom top-level docstring template that includes your common
# option(s). In this case we've added a "verbose" option.
DOC_TEMPLATE = """{program}

Usage: {program} [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.
  -v --verbose  Use verbose logging

Available commands:
  {available_commands}

See '{program} help <command>' for help on specific commands.
"""


# 3. Provide a function which handles top-level options. This is passed the
# config parsed from the command line using `DOC_TEMPLATE`.
def handle_common_options(config):
    if config['--verbose']:
        print('enabling verbose logging')


# 4. Pass the custom doc-template and command-handler to `main()`.
dsc.main(
    'docopt-subcommand-example',
    'docopt-subcommand-example v42',
    doc_template=DOC_TEMPLATE,
    common_option_handler=handle_common_options)
