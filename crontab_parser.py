import re
import logging

logger = logging.getLogger()


def parse(crontab, valid_range):
    for n, field in enumerate(crontab[:5]):
        if '/' in field:
            field_values = [int(x) for x in re.split('\W', field)]
            crontab[n] = list(range(field_values[0], field_values[1], field_values[2]))
        elif '-' in field:
            field_values = [int(x) for x in field.split('-')]
            crontab[n] = list(range(field_values[0], field_values[1] + 1))
        elif '*' in field:
            crontab[n] = list(range(*valid_range[n]))
        elif ',' in field:
            crontab[n] = [int(x) for x in field.split(',')]
    crontab[5] = ' '.join(crontab[5:])

    # checking for invalid values
    check_crontab(crontab[:6], valid_range)

    return crontab[:6]


def check_crontab(crontab, valid_range):
    err_field = ['min', 'hour', 'day_of_month', 'month', 'day_of_week']

    # Avoiding impossible dates as 31th June
    valid_range[2] = (1, 31) if crontab[3] in ['4', '6', '9', '11'] else (1, 29) if crontab[3] == '2' else (1, 32)

    current_field = 0
    for field, valid_values in zip(crontab, valid_range):
        if isinstance(field, list):
            for value in field:
                if int(value) not in range(*valid_values):
                    logger.error("Invalid input: {} in {} field"
                                 .format(value, err_field[current_field]))
                    exit()
        else:
            if int(field) not in range(*valid_values):
                logger.error("Invalid input: {} in {} field"
                             .format(field, err_field[current_field]))
                exit()
        current_field+=1


def stylize(parsed_crontab):
    parsed_crontab[:-1] = [' '.join(str(value) for value in field) if isinstance(field, list) else field for field in parsed_crontab[:-1]]
    output = "Minute: {}\n" \
             "Hour: {}\n" \
             "Day of the month: {}\n" \
             "Month: {}\n" \
             "Day of the week: {}\n" \
             "Command: {}".format(*parsed_crontab)
    return output
