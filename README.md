# Crontab parser

Simple crontab parser written in Python.

## Usage:

```
python main.py <input>
```

#### Input:

``5 0 1 2 0 /usr/bin/sample.sh``, using:
 
 1. `-` for ranges
 2. `-/` for ranges with step values
 3. `,` for lists
 4. `*` for full valid ranges 

#### Output:
```Minute: 5
Hour: 0
Day of the month: 1
Month: 2
Day of the week: 0
Command: /usr/bin/sample.sh
```

## Tests
```
python test_parser.py
```