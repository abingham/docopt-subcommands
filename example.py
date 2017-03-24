import docopt_subcommands

sc = docopt_subcommands.Subcommands(
    'docopt-subcommand-example',
    'docopt-subcommand-example v42')


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


sc.add_command('foo', foo_handler)
sc.add_command('bar', bar_handler)

docopt_subcommands.main(sc)
