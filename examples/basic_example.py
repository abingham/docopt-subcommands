# Basic, most common usage of docopt_subcommands

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


# 2. Pass a program name and version string to `main` to run a program with the
# subcommands you defined with the decorators above.
dsc.main(
    program='docopt-subcommand-example',
    version='docopt-subcommand-example v42')
