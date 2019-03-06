import unittest
import crontab_parser as parser

class TestParserMethods(unittest.TestCase):

    valid_range = [(0, 60), (0, 24), (1, 32), (1, 13), (0, 7)]

    def test_parse_crontab(self):
        # Lists
        self.assertEqual(parser.parse(['1', '1', '1', '1', '0,1', '/usr/bin/sample.sh'], self.valid_range),
                         ['1', '1', '1', '1', [0, 1], '/usr/bin/sample.sh'])
        # Asterisks
        self.assertEqual(parser.parse(['1', '1', '1', '1', '*', '/usr/bin/sample.sh'], self.valid_range),
                         ['1', '1', '1', '1', [0, 1, 2, 3, 4, 5, 6], '/usr/bin/sample.sh'])
        # Range
        self.assertEqual(parser.parse(['1', '1', '1', '1', '1-3', '/usr/bin/sample.sh'], self.valid_range),
                         ['1', '1', '1', '1', [1, 2, 3], '/usr/bin/sample.sh'])
        # Range with steps
        self.assertEqual(parser.parse(['1', '1', '1', '1', '0-5/2', '/usr/bin/sample.sh'], self.valid_range),
                         ['1', '1', '1', '1', [0, 2, 4], '/usr/bin/sample.sh'])


    def test_check_crontab(self):
        self.assertRaises(SystemExit, parser.check_crontab,
                          ['0', '0', '0', '0', '0', '/usr/bin/sample.sh'], self.valid_range)


    def test_output_style(self):
        self.assertEqual(parser.stylize(['1', [1, 2], '10', '1', '1', '/usr/bin/sample.sh foo bar']),
                         "Minute: 1\n" \
                         "Hour: 1 2\n" \
                         "Day of the month: 10\n" \
                         "Month: 1\n" \
                         "Day of the week: 1\n" \
                         "Command: /usr/bin/sample.sh foo bar")

if __name__ == '__main__':
    unittest.main()