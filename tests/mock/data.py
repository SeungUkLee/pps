from pps.color import CYAN, ENDC

INPUT_TOML_DATA = """[[source]]
    name = "test_file"
    url = "https://test_file.test"
    verify_ssl = true
    
    [scripts]
    echo = "Echo Hello World!!"
    version = "python --version"
    
    [dev-packages]
    test-dev-packages = "*"
    
    [packages]
    test-package = "*"
    
    [requires]
    python_version = "3.7"
    """

OUTPUT_TOML_DATA = {
    'source': [
        {
            'name': 'test_file',
            'url': 'https://test_file.test',
            'verify_ssl': True,
        }
    ],
    'scripts': {'echo': 'Echo Hello World!!', 'version': 'python --version'},
    'dev-packages': {'test-dev-packages': '*'},
    'packages': {'test-package': '*'},
    'requires': {'python_version': '3.7'},
}


OPT_SHOW_DATA = """{0}echo{1}: "Echo Hello World!!"
{0}version{1}: "python --version"
{0}error{1}: "error"
""".format(
    CYAN, ENDC
)
