from .color import Color


class Message:
    EXE_SCRIPT_ERR_MSG = '{0}[!]{1} An error occurred while executing script in Pipfile'.format(
        Color.FAIL, Color.ENDC
    )
    KEYWORD_NOT_FOUND_MSG = "{0}[!]{1} {2}Pipfile{3} in {4}[scripts]{5} keyword not found!".format(
        Color.FAIL,
        Color.ENDC,
        Color.OKBLUE,
        Color.ENDC,
        Color.YELLOW,
        Color.ENDC,
    )
    FILE_NOT_FOUND_MSG = "{0}[!]{1} {2}Pipfile{3} not found!".format(
        Color.FAIL, Color.ENDC, Color.OKBLUE, Color.ENDC
    )
    KEYBOARD_INTERRUPT_MSG = "{0}[!]{1} KeyboardInterrupt".format(
        Color.FAIL, Color.ENDC
    )
    INQUIRER_MESSAGE = "{0}Select Pipfile script to run{1}".format(
        Color.YELLOW, Color.ENDC
    )
