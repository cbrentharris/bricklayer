from bricklayer import create_parser, diagnose, cannot_be_compiled, collect, main
from unittest import TestCase
import mock
import os

class CommandLineTest(TestCase):

    def test_it_collects_via_the_command_line(self):
        args = ['bricklayer', '--collect', 'compileable.py']
        with mock.patch('sys.argv',args):
            with mock.patch('bricklayer.collect') as mock_collect:
                main()
                mock_collect.assert_called_with('compileable.py')

    def test_it_diagnoses_via_the_command_line(self):
        args = ['bricklayer', '--diagnose', 'compileable.py']
        with mock.patch('sys.argv',args):
            with mock.patch('bricklayer.diagnose') as mock_diagnose:
                main()
                mock_diagnose.assert_called_with('compileable.py')

    def test_it_downloads_ldd_via_the_command_line(self):
        args = ['bricklayer', '--download'] 
        with mock.patch('sys.argv', args):
            with mock.patch('bricklayer.utils.downloader.Downloader.download_ldd') as mock_download:
                main()
                mock_download.assert_called_with()

    @mock.patch('bricklayer.doctor.checks.Checker.check_program')
    def test_it_diagnoses_a_file(self, mock_check):
        compileable_full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'compileable.py')
        diagnose(compileable_full_path)
        mock_check.assert_called_with(compileable_full_path)

    def test_it_tries_to_compile_a_file(self):
        compileable_full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'compileable.py')
        uncompileable_full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uncompileable.py')
        self.assertTrue(cannot_be_compiled(uncompileable_full_path))
        self.assertFalse(cannot_be_compiled(compileable_full_path))

    @mock.patch('bricklayer.backend.api.BackendApi.post_metrics')
    def test_it_collects_data(self,  mock_post):
        fake_metrics = mock.Mock(source_lines_of_code=1, comments=1, cyclomatic_complexity=1, user_defined_functions=1,level=1)
        compileable_full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'compileable.py')
        with mock.patch('bricklayer.doctor.metrics.Metrics.__new__', return_value=fake_metrics):
            collect(compileable_full_path)
            mock_post.assert_called_with(
                    source_lines_of_code=fake_metrics.source_lines_of_code,
                    comments=fake_metrics.comments,
                    cyclomatic_complexity=fake_metrics.cyclomatic_complexity,
                    filename=compileable_full_path,
                    user_defined_functions=fake_metrics.user_defined_functions,
                    level=fake_metrics.level
                    )
