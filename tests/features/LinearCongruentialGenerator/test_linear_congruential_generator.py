import unittest
from unittest.mock import patch, mock_open, call
from features.LinearCongruentialGenerator.linear_congruential_generator import LinearCongruentialGenerator  # use actual module name

class TestLCG(unittest.TestCase):
    def setUp(self):
        self.lcg = LinearCongruentialGenerator()

    def test_generate_value(self):
        self.assertEqual(self.lcg.generate_value(2), 64)

    @patch('builtins.input', side_effect=['5', '6', '7', '8'])
    def test_update_params_from_terminal(self, mock_input):
        self.lcg.update_params_from_terminal()
        self.assertEqual(self.lcg.a, 5)
        self.assertEqual(self.lcg.c, 6)
        self.assertEqual(self.lcg.m, 7)
        self.assertEqual(self.lcg.x0, 8)

    @patch('builtins.open', new_callable=mock_open,
            read_data='a,c,m,x0\n5,6,7,8\n')
    def test_update_params_from_csv_file(self, mock_file):
        with patch('builtins.input', return_value=''):
            self.lcg.update_params_from_csv_file()
        self.assertEqual(self.lcg.a, 5)
        self.assertEqual(self.lcg.c, 6)
        self.assertEqual(self.lcg.m, 7)
        self.assertEqual(self.lcg.x0, 8)

    def test_get_period(self):
        self.lcg.last_sequence = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        self.assertEqual(self.lcg.get_period(), 5)


class MockLCG(LinearCongruentialGenerator):
    def __init__(self):
        super().__init__()
        self.a = 1
        self.c = 1
        self.m = 5
        self.x0 = 1
        self.last_sequence = []
        self.last_period = 0

class TestLCG2(unittest.TestCase):
    def setUp(self):
        self.lcg = MockLCG()

    def test_generate_value(self):
        self.assertEqual(self.lcg.generate_value(1), 2)

    @patch('builtins.input', return_value='1')   # we return '1' whenever input() is called
    def test_generate_sequence(self, mock_input):
        self.lcg.generate_sequence()
        self.assertEqual(self.lcg.last_sequence, [1])


    @patch('builtins.print')
    def test_print_results(self, mock_print):
        self.lcg.last_sequence = [1, 2, 3, 4, 0]
        self.lcg.last_period = 5
        self.lcg.print_results()
        calls = [call('Results:'),
                 call('Sequence: ', [1, 2, 3, 4, 0]),
                 call('Period: ', 5)]
        mock_print.assert_has_calls(calls, any_order=False)    # check that print() was called with expected arguments


    def test_get_period(self):
        self.lcg.last_sequence = [1, 2, 3, 4, 0, 1, 2, 3, 4, 0]
        self.assertEqual(self.lcg.get_period(), 5)

if __name__ == '__main__':
    unittest.main()