import docopt_subcommands as dsc
import pytest

UNKNOWN_COMMAND_TEMPLATE = '''"{}" is not a valid command.

prog

Usage: prog [options] <command> [<args> ...]

Options:
  -h --help     Show this screen.
  -v --version  Show the program version.

Available commands:
  foo

See 'prog <command> -h' for help on specific commands.
'''



@pytest.fixture
def foo_command():
    @dsc.command('foo')
    def foo_handler(_):
        "usage: {program} {command}"
        pass


@pytest.mark.usefixtures('reset_commands', 'foo_command')
class TestUnknownCommands:
    def test_unknown_command_displays_usage(self, capsys):
        try:
            dsc.main(program='prog',
                     version='prog-1',
                     argv=['llamas'],
                     exit_at_end=False)
        except SystemExit:
            pass

        out, _ = capsys.readouterr()
        assert out == UNKNOWN_COMMAND_TEMPLATE.format('llamas')

    def test_unknown_command_with_dash_h_displays_usage(self, capsys):
        try:
            dsc.main(program='prog',
                     version='prog-1',
                     argv=['llamas', '-h'],
                     exit_at_end=False)
        except SystemExit:
            pass

        out, _ = capsys.readouterr()
        assert out == UNKNOWN_COMMAND_TEMPLATE.format('llamas')

    def test_help_for_unknown_command_displays_usage(self, capsys):
        try:
            dsc.main(program='prog',
                     version='prog-1',
                     argv=['llamas'],
                     exit_at_end=False)
        except SystemExit:
            pass

        out, _ = capsys.readouterr()
        assert out == UNKNOWN_COMMAND_TEMPLATE.format('llamas')
