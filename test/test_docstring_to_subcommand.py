from docopt_subcommands.subcommands import docstring_to_subcommand
from hypothesis import given, assume
import pytest

import strategies as ST


def test_empty_docstring():
    with pytest.raises(ValueError):
        docstring_to_subcommand("")


@given(ST.ascii_string)
def test_no_usage_leader(name):
    assume(name != 'usage')
    with pytest.raises(ValueError):
        docstring_to_subcommand("{}: {{command}} foo".format(name))


def test_missing_subcommand_throws_exception():
    with pytest.raises(ValueError):
        docstring_to_subcommand("usage: {{command}}")


@given(ST.ascii_string)
def test_correct_docstring_gives_subcommand_name(name):
    doc = """usage: {{command}} {}

    Something.

    Something else.
    """.format(name)

    subcommand = docstring_to_subcommand(doc)
    assert subcommand == name


@given(ST.ascii_string, ST.whitespace)
def test_extra_whitespace_gives_subcommand_name(name, space):
    doc = """{1}usage:{1}{{command}}{1}{0}{1}
    {1}
    Something.
    {1}
    Something else.
    {1}
    """.format(name, space)

    subcommand = docstring_to_subcommand(doc)
    assert subcommand == name
