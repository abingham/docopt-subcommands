# Example of using Subcommands without decorators (i.e. Subcommands for crazy
# people).

import docopt_subcommands

# 1. Create a Subcommands object with a program name and version string.
sc = docopt_subcommands.Subcommands(
    'docopt-subcommand-example',
    'docopt-subcommand-example v42')


# 2. Define your handlers without registering them yet.
def foo_handler(args):
    """usage: {program} {command} <name>

    Apply foo to a name.
    """
    print("Foo, {}".format(args['<name>']))


def bar_handler(args):
    """usage: {program} {command} <name>

    Apply bar to a name.
    """
    print("Bar, {}".format(args['<name>']))


# 3. Register your handlers and associated command names with
# `Subcommands.add_command()`.
sc.add_command(foo_handler, 'foo')
sc.add_command(bar_handler, 'bar')

# 4. Pass the Subcommands object to `main` via the `commands` keyword argument
# to run a program with the subcommands you defined with `add_command()`.
docopt_subcommands.main(commands=sc)
