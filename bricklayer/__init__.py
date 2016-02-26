import argparse
import py_compile
from bricklayer.doctor.config import Configurator
from bricklayer.doctor.metrics import Metrics
from bricklayer.doctor.checks import Checker
from bricklayer.backend.api import BackendApi
from bricklayer.utils.downloader import Downloader

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--diagnose', help='Use diagnose if you are having issues with your program and would like to see some help about what is wrong')
    parser.add_argument('-c', '--collect', help='Submit data to bricklayer')
    parser.add_argument('-k', '--key', help='Set an API key to use to post to the bricklayer backend')
    parser.add_argument('-hn', '--hostname', help='The hostname of your bricklayer backend')
    parser.add_argument('-dl', '--download', help='Downlaod lego digital designer.', action='store_true')
    return parser

def diagnose(filename):
    checker = Checker()
    checker.check_program(filename)

def cannot_be_compiled(filename):
    try:
        py_compile.compile(filename, doraise=True)
        return False
    except py_compile.PyCompileError as e:
        return True

def collect(filename):
    if not filename.endswith('.py'):
        raise ValueError("You must specify a python file to collect data about. Caanot collect data about {}".format(filename))
    if cannot_be_compiled(filename):
        raise ValueError("There is an issue with your python program. Try running the --diagnose method of bricklayer to see what is wrong.")
    m = Metrics()
    m.collect_metrics(filename)
    BackendApi.post_metrics(
        source_lines_of_code=m.source_lines_of_code,
        comments=m.comments,
        cyclomatic_complexity=m.cyclomatic_complexity,
        filename=filename,
        user_defined_functions=m.user_defined_functions,
        level=m.level
    )

def main():
    parser = create_parser()
    args = parser.parse_args()
    Configurator.create_config_if_doesnt_exist()
    if args.key:
        Configurator.add_to_config('key', args.key)
    if args.hostname:
        configuration.add_to_config('hostname', args.hostname)
    if args.diagnose:
        diagnose(args.diagnose)
    if args.collect:
        collect(args.collect)
    if args.download:
        Downloader.download_ldd()


if __name__ == '__main__': 
    main()
