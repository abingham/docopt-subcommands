# Example showing how to handle custom pre-command options.
#
# We'll add a "--verbose" options which is common to all commands.

from docopt_subcommands import command, main

# We need to provide a new top-level documentation template which contains
# our --verbose option.
DOC_TEMPLATE = """{program}

Usage: {program} [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.
  -v --version  Show the program version.
  --verbose     Use verbose output

Available commands:
  {available_commands}

See '{program} <command> -h' for help on specific commands.
"""

# Use the `command` decorator to add subcommand functions.
@command()
def foo_handler(precommand_args, args):
    """usage: {program} foo <name>

    Apply foo to a name.
    """
    if precommand_args['--version']:
        print('version!')
        return
    if precommand_args['--verbose']:
        print('[verbose mode]')
    print("Foo, {}".format(args['<name>']))


@command()
def bar_handler(precommand_args, args):
    """usage: {program} bar [options] <name>

    Apply bar to a name.

    Options:
      --fnord    Insert a fnord
    """
    if precommand_args['--version']:
        print('version!')
        return

    if precommand_args['--verbose']:
        print('[verbose mode]')

    print("Bar, {}".format(args['<name>']))
    if args['--fnord']:
        print('fnord')


# 5. Pass out Subcommands subclass instance to `main()`.
main(program='example', doc_template=DOC_TEMPLATE)
