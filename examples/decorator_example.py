# Example of creating a Subcommands object and using its decorators to define
# subcommands.

import docopt_subcommands

# 1. Create a Subcommands object with a program name and version string.
sc = docopt_subcommands.Subcommands(
    'docopt-subcommand-example',
    'docopt-subcommand-example v42')


# 2. Use the Subcommand's `command` decorator to add subcommands.
@sc.command('foo')
def foo_handler(args):
    """usage: {program} {command} <name>

    Apply foo to a name.
    """
    print("Foo, {}".format(args['<name>']))


@sc.command('foo')
def bar_handler(args):
    """usage: {program} {command} <name>

    Apply bar to a name.
    """
    print("Bar, {}".format(args['<name>']))


# 3. Pass the Subcommands object to `main` via the `commands` keyword argument
# to run a program with the subcommands you defined with the decorators above.
docopt_subcommands.main(commands=sc)
