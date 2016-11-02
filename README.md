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

`docopt` subcommands is here to help you create similar kinds of command-line
tools.

## Quickstart

The basic idea behind `docopt-subcommands` is simple:

 1. You provide a separate *handler function* for each subcommand.
 2. The docstring for each handler function defines the docopt definition for
    that subcommand.
 3. You provide a dict-like mapping from subcommand names to handler functions.
 4. You provide a program name, version string, and (optionally) a top-level
    documentation string.

Then `docopt-subcommands` does the work of stitching everything together into a subcommand-driven program. Here's how it looks:
```python
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


```
