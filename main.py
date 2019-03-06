import sys
import crontab_parser as parser

crontab_entry = sys.argv[1:]
valid_range = [(0, 60), (0, 24), (1, 32), (1, 13), (0, 7)]

parsed_crontab = parser.parse(crontab_entry, valid_range)
result = parser.stylize(parsed_crontab)

print(result)