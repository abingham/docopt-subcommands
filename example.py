import docopt_subcommands


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

COMMAND_MAP = {
    'foo': foo_handler,
    'bar': bar_handler
}

docopt_subcommands.main(
    COMMAND_MAP,
    'docopt-subcommand-example',
    'docopt-subcommand-example v42')
