import docopt_subcommands

sc = docopt_subcommands.Subcommands(
    'docopt-subcommand-example',
    'docopt-subcommand-example v42')


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


docopt_subcommands.main(commands=sc)
