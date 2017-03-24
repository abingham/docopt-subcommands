import docopt_subcommands as dsc


@dsc.command('foo')
def foo_handler(args):
    """usage: {program} {command} <name>

    Apply foo to a name.
    """
    print("Foo, {}".format(args['<name>']))


@dsc.command('foo')
def bar_handler(args):
    """usage: {program} {command} <name>

    Apply bar to a name.
    """
    print("Bar, {}".format(args['<name>']))


dsc.main(
    program='docopt-subcommand-example',
    version='docopt-subcommand-example v42')
