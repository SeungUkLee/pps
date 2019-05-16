import functools
import subprocess

import inquirer
import toml

from .message import Message


def exception(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            print(Message.KEYWORD_NOT_FOUND_MSG)
            exit()
        except FileNotFoundError:
            print(Message.FILE_NOT_FOUND_MSG)
            exit()
        except KeyboardInterrupt:
            print(Message.KEYBOARD_INTERRUPT_MSG)
            exit()

    return wrapper


def read_file(file_path):
    reader = open(file_path, 'r', encoding="utf8")
    file_content = reader.read()
    reader.close()

    return file_content


def toml_parsing(toml_string):
    parsed_toml = toml.loads(toml_string)

    return parsed_toml


def inquirer_prompt(choice):
    questions = [
        inquirer.List('cmd', message=Message.INQUIRER_MESSAGE, choices=choice)
    ]
    answer = inquirer.prompt(questions)
    return answer


def run_script(script):
    p = subprocess.call(script, shell=True)

    return p
