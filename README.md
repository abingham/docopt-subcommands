[![Build Status](https://travis-ci.org/abingham/docopt-subcommands.png?branch=master)](https://travis-ci.org/abingham/docopt-subcommands)

# docopt-subcommands

A simple implementation of subcommands for docopt.

`docopt-subcommands` allows you to create subcommand-based programs
using [docopt](https://github.com/docopt/docopt). A subcommand-based program is
one in which the main program a "subcommand" argument to tell it what to do.

The classic example of such a program is [git](https://git-scm.com/). The `git`
command with not arguments doesn't do much of anything. Instead, its the first
argument to `git` - the *subcommand* - that tells it what to actually do. For
example:

```
git log
```

will give you the log for your repository. Likewise:

```
git rebase
```

is the subcommand for rebasing.

`docopt-subcommands` is here to help you create similar kinds of command-line
tools.

## Quickstart

The basic idea behind `docopt-subcommands` is simple:

 1. You provide a separate *handler function* for each subcommand.
 2. The docstring for each handler function defines the docopt definition for
    that subcommand.
 3. You register your handler functions with the names of the subcommands which
    will invoke them.
 4. You provide a program name, version string, and (optionally) a top-level
    documentation string.

Then `docopt-subcommands` does the work of stitching everything together into a
subcommand-driven program. Here's how it looks (from the included `basic_example.py`):

```python
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
```

If you run this program at the commands line you'll see that you have a nice,
subcommand-based CLI program:

```shell
$ python basic_example.py
Usage: docopt-subcommand-example [options] <command> [<args> ...]
$ python basic_example.py -h
docopt-subcommand-example

Usage: docopt-subcommand-example [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.

Available commands:
  bar
  foo
  help

See 'docopt-subcommand-example help <command>' for help on specific commands.

$ python basic_example.py foo
usage: docopt-subcommand-example foo <name>

$ python basic_example.py foo -h
usage: docopt-subcommand-example foo <name>

    Apply foo to a name.

$ python basic_example.py foo Bubba
Foo, Bubba
```

For more examples, see the `examples` directory.
