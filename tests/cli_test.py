import argparse
import pytest
import os

from pps.cli import run_pps_cmd, arg_parser, main


@pytest.mark.parametrize('arg, namespace', [
    ('--show', argparse.Namespace(show=True)),
])
def test_arg_parser(arg, namespace):
    parser = arg_parser()
    actual = parser.parse_args(arg.split(' '))

    assert actual == namespace


@pytest.mark.parametrize('namespace', [
    argparse.Namespace(show=True),
    argparse.Namespace(show=False)
])
def test_run_cmd_pps(namespace):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_name = 'test.toml'
    file_path = '{0}/mock/{1}'.format(root_dir, test_file_name)

    opt, res, err = run_pps_cmd(
        args=namespace,
        file_path=file_path,
        test=True
    )

    if err == -1:
        pytest.fail("An error occurred while executing script in Pipfile")

    if opt == 'show':
        assert res == ['echo: "Echo Hello World!!"', 'version: "python --version"', 'error: "error"']


@pytest.mark.parametrize('namespace', [
    argparse.Namespace(show=True),
    argparse.Namespace(show=False)
])
def test_run_cmd_pps_error(namespace):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_name = 'no_script_test.toml'
    invalid_file_path = '{0}/mock/{1}'.format(root_dir, test_file_name)

    with pytest.raises(SystemExit):
        run_pps_cmd(
            args=namespace,
            file_path='',
            test=True
        )

        run_pps_cmd(
            args=namespace,
            file_path=invalid_file_path,
            test=True
        )
