import argparse

from pytest import mark
from pps.cli import arg_parser


@mark.parametrize('arg, namespace', [
    ('--show', argparse.Namespace(show=True)),
])
def test_arg_parser(arg, namespace):
    parser = arg_parser()
    actual = parser.parse_args(arg.split(' '))

    assert actual == namespace

