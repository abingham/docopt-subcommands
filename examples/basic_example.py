# Basic, most common usage of docopt_subcommands

import docopt_subcommands as dsc


# 1. Use the `command` decorator to add subcommands functions.
@dsc.command()
def foo_handler(common_args, command_args):
    """usage: {program} foo <name>

    Apply foo to a name.
    """
    print("Foo, {}".format(command_args['<name>']))


@dsc.command()
def bar_handler(common_args, command_args):
    """usage: {program} bar <name>

    Apply bar to a name.
    """
    print("Bar, {}".format(command_args['<name>']))


# 2. Pass a program name and version string to `main` to run a program with the
# subcommands you defined with the decorators above.
dsc.main(
    'docopt-subcommand-example',
)