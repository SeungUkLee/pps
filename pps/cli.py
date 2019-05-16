import argparse
import os

from .color import Color
from .helper import (
    exception,
    inquirer_prompt,
    read_file,
    run_script,
    toml_parsing,
)
from .message import Message


@exception
def run_pps_cmd(args, file_path, test=False):
    scripts = toml_parsing(read_file(file_path))['scripts']

    opt, res, err = None, None, None
    if args.show:
        opt = 'show'
        res = [
            '{0}: "{1}"'.format(script, cmd) for script, cmd in scripts.items()
        ]
    elif not test:
        ans = inquirer_prompt(scripts)
        if ans is None:
            raise KeyboardInterrupt
        cmd = ans['cmd']
        res = run_script(scripts[cmd])
        err = -1 if res != 0 else 1

    return opt, res, err


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--show', help="show pipfile scripts list", action='store_true'
    )

    return parser


def main(arg=None, file_path=None):
    parser = arg_parser()
    args = (
        parser.parse_args()
        if arg is None
        else parser.parse_args(arg.split(' '))
    )
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if file_path is None:
        file_path = '{0}/../Pipfile'.format(root_dir)

    opt, res, err = run_pps_cmd(args, file_path)
    if err == -1:
        print(Message.EXE_SCRIPT_ERR_MSG)
        return
    if opt == 'show':
        for cmd_and_script in res:
            cmd, script = cmd_and_script.split(':')
            print('{0}{1}{2}:{3}'.format(Color.CYAN, cmd, Color.ENDC, script))
