import unittest
from io import StringIO
from unittest.mock import patch


class Test(unittest.TestCase):

    @patch('builtins.input', return_value="joonas")
    @patch('sys.stdout', new_callable=StringIO)
    def test_case1(self, mock_stdout, mock_input):
        import solution_10926
        self.assertEqual(mock_stdout.getvalue(), "joonas??!\n")

    @patch('builtins.input', return_value="baekjoon")
    @patch('sys.stdout', new_callable=StringIO)
    def test_case1(self, mock_stdout, mock_input):
        import solution_10926
        self.assertEqual(mock_stdout.getvalue(), "baekjoon??!\n")
