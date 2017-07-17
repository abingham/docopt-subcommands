import docopt
import docopt_subcommands as dsc
import pytest


@pytest.fixture()
def reset_commands():
    dsc._commands = []


@pytest.mark.usefixtures("reset_commands")
class TestMain:
    def test_default_top_level_help(self):
        try:
            dsc.main(program='prog',
                     version='prog-1',
                     argv=[],
                     exit_at_end=False)
        except docopt.DocoptExit as e:
            assert e.usage == "Usage: prog [options] <command> [<args> ...]"

    def test_default_subcommand_help(self, capsys):
        @dsc.command('foo')
        def foo_handler(args):
            "usage: {program} {command}"
            pass

        try:
            dsc.main(program='prog',
                     version='prog-1',
                     argv=['foo', '-h'],
                     exit_at_end=False)
        except SystemExit:
            pass

        out, err = capsys.readouterr()
        assert out == "usage: prog foo\n"

    def test_extract_subcommand_name_from_docstring(self, capsys):
        @dsc.command()
        def foo_handler(args):
            "usage: {program} foo"
            pass

        try:
            dsc.main(program='prog',
                     version='prog-1',
                     argv=['foo', '-h'],
                     exit_at_end=False)
        except SystemExit:
            pass

        out, err = capsys.readouterr()
        assert out == "usage: prog foo\n"
