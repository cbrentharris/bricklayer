import subprocess
import re
import os
import errno
import glob
from collections import OrderedDict
from os.path import expanduser
from bricklayer.doctor.metrics import Metrics

from jinja2 import Environment, PackageLoader


class TLSystem(object):
    HOME = expanduser("~")
    TL_HOME = os.environ.get("TL_HOME", os.path.join(HOME, "TL/TL_System"))
    TL_PROJECT_HOME = os.environ.get("TL_PROJECT_HOME", os.path.join(HOME, "TL_Project"))
    MLTON_BIN = "/usr/local/bin/mlton"
    MLLEX_BIN = "/usr/local/bin/mllex"
    SML_COMMENT_REGEX = "\(\*(.|\s)*?\*\)"

    TRANSPILE_ARGS = [
        os.path.join(TL_PROJECT_HOME, "Transformation", "bin", "transform"),
        "@MLton",
        "load-world",
        os.path.join(TL_PROJECT_HOME, "Transformation", "bin", "transform.mlton"),
        "--",
        "--dir={}".format(os.path.join(TL_PROJECT_HOME, "Transformation")),
        "--tlp=smlToPython",
        "--target-dir={}".format(os.path.join(TL_PROJECT_HOME, "Target")),
        "--target-index=0",
        "--target-type=single"
    ]

    @staticmethod
    def surround_with_quotes(string):
        return '"{}"'.format(string)

    @classmethod
    def compile_sml_file_args(cls, directory, filename):
        return map(cls.surround_with_quotes, [
            cls.MLTON_BIN,
            "-link-opt",
            "-fno-PIE",
            "-mlb-path-var",
            "TL {}".format(cls.TL_HOME),
            "-mlb-path-var",
            "DOMAIN {}".format(cls.TL_PROJECT_HOME),
            "-output",
            os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", filename),
            "-verbose",
            "1",
            "-const",
            "Exn.keepHistory false",
            "-profile",
            "no",
            "-profile-branch",
            "false",
            "-profile-val",
            "false",
            os.path.join(cls.TL_HOME, directory, "{}.mlb".format(filename)),
        ])

    @classmethod
    def build_tl_args(cls):

        build_tokens_args = [
            "cp",
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "Syntax", "bricklayer.spec")),
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "target_tokens.spec")),
            '&&',
            cls.surround_with_quotes(cls.MLLEX_BIN),
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "target_tokens.spec")),
        ]
        build_parser_args = cls.compile_sml_file_args("Parse", "parser") + [
            "&&",
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "parser")),
            cls.surround_with_quotes("-link-opt"),
            cls.surround_with_quotes("-fno-PIE"),
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation")),
            cls.surround_with_quotes("bricklayer.bnf"),
            cls.surround_with_quotes("sml_prog")
        ]
        build_parser_table_args = [
            "cd",
            cls.surround_with_quotes(os.path.join(cls.TL_HOME, "Engine")),
            "&&",
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "parser")),
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation")),
            cls.surround_with_quotes("bricklayer.bnf"),
            cls.surround_with_quotes("sml_prog")
        ]

        build_transformer_args = cls.compile_sml_file_args("Transform", "transform") + [
            "&&",
            cls.surround_with_quotes(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "transform")),
            cls.surround_with_quotes("--dir={}".format(os.path.join(cls.TL_PROJECT_HOME, "Transformation"))),
            cls.surround_with_quotes("--grammar=bricklayer.bnf"),
            cls.surround_with_quotes("--start-symbol=sml_prog")
        ]
        build_pretty_printer_args = [
                                        "cp",
                                        cls.surround_with_quotes(
                                            os.path.join(cls.TL_PROJECT_HOME, "Transformation", "Syntax",
                                                         "format.sty")),
                                        cls.surround_with_quotes(
                                            os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin",
                                                         "format.sty.sml")),
                                        "&&",
                                    ] + cls.compile_sml_file_args("PrettyPrint", "prettyprint")

        args = reduce(lambda command1, command2: command1 + [';'] + command2,
                      [build_tokens_args, build_parser_args, build_parser_table_args, build_transformer_args,
                       build_pretty_printer_args])
        return args

    @classmethod
    def build_parse_tlp_file_args(cls, tlp_file):
        return map(cls.surround_with_quotes, [
            os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "parser"),
            "@MLton",
            "load-world",
            os.path.join(cls.TL_PROJECT_HOME, "Transformation", "bin", "parser.mlton"),
            "--",
            "TLP",
            os.path.join(cls.TL_PROJECT_HOME, "Transformation"),
            tlp_file
        ])

    @classmethod
    def initialize_system(cls):
        cls.create_transpile_directory()
        args = cls.build_tl_args()
        print(' '.join(args))
        subprocess.call(' '.join(args), shell=True)

    @classmethod
    def create_transpile_directory(cls):
        for target_dir in ["SML_Modules", "TL_Modules", "Syntax", "bin"]:
            try:
                os.makedirs(os.path.join(cls.TL_PROJECT_HOME, "Transformation", target_dir))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        for filename in ['format.sty', 'bricklayer.spec', 'bricklayer.bnf']:
            # make the files under syntax
            with open(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "Syntax", filename), 'w') as outfile:
                env = Environment(loader=PackageLoader('bricklayer', 'templates'))
                template = env.get_template(filename)
                outfile.write(template.render())
        with open(os.path.join(cls.TL_PROJECT_HOME, "Transformation", "TL_Modules", "smlToPython.tlp"), 'w') as outfile:
            env = Environment(loader=PackageLoader('bricklayer', 'templates'))
            template = env.get_template('smlToPython.tlp')
            outfile.write(template.render())

    @classmethod
    def transpile_all_files(cls):
        directory_map = OrderedDict([
            ('Level_1', ['Assignment_1', 'Assignment_2', 'Assignment_3']),
            ('Level_2', ['Assignment_4', 'Assignment_5', 'Assignment_6', 'Assignment_7'])
        ])
        for parent_dir, children_dirs in directory_map.items():
            for child_dir in children_dirs:
                full_dir = os.path.join(cls.TL_PROJECT_HOME, "Target", "0", parent_dir, child_dir)
                os.chdir(full_dir)
                filelist = glob.glob("*no_comments.bl")
                for f in filelist:
                    os.remove(f)
                for filename in os.listdir(full_dir):
                    TLSystem.transpile(os.path.join(parent_dir, child_dir, filename))


    @classmethod
    def transpile(cls, filename):
        new_file = cls.replace_newlines_with_spaces_in_file(filename)
        subprocess.call(' '.join(cls.build_parse_tlp_file_args("smlToPython")), shell=True)
        subprocess.call(' '.join(map(cls.surround_with_quotes, cls.TRANSPILE_ARGS + [new_file])), shell=True)
        metrics = Metrics()
        try:
            metrics.collect_metrics(os.path.join(cls.TL_PROJECT_HOME, "Target", "1", "transpiled.py"))
            cls.append_metrics_to_log_file(metrics, filename)
        except SyntaxError:
            print "Error collecting metrics of filename " + filename

    @classmethod
    def remove_comments(cls, string):
        return re.sub(cls.SML_COMMENT_REGEX, "", string)

    @classmethod
    def replace_newlines_with_spaces(cls, string):
        return string.replace("\r", "\n")

    @classmethod
    def replace_newlines_with_spaces_in_file(cls, filename):
        name, ext = os.path.splitext(filename)
        new_filename = os.path.join(cls.TL_PROJECT_HOME, "Target", "0", name + "_no_comments" + ext)
        with open(os.path.join(cls.TL_PROJECT_HOME, "Target", "0", filename), 'rb') as input_file:
            output = cls.replace_newlines_with_spaces(input_file.read())
            with open(new_filename, 'wb') as output_file:
                output_file.write(output)
        return name + "_no_comments" + ext

    @classmethod
    def append_metrics_to_log_file(cls, metrics, filename):
        with open(os.path.join(cls.TL_PROJECT_HOME, "Target", "2", "stats.csv"), "a+") as output_file:
            output_file.write("\n" + ",".join(map(str, [metrics.cyclomatic_complexity, metrics.source_lines_of_code,
                                                 metrics.comments, metrics.user_defined_functions, metrics.level,
                                                 filename])))
