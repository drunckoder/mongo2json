import re
from functools import reduce
from typing import Pattern, List, Iterable

patterns: List[Pattern[str]] = [
    re.compile(pattern=r'ObjectId\((.*)\)'),
    re.compile(pattern=r'ISODate\((.*)\)'),
    re.compile(pattern=r'NumberLong\((.*)\)'),
    re.compile(pattern=r'NumberInt\((.*)\)'),
    re.compile(pattern=r'NumberDecimal\("(.*)"\)'),
]


def apply_pattern(pattern: Pattern[str], string: str) -> str:
    return pattern.sub(repl=r'\1', string=string)


def clean_line(line: str) -> str:
    return reduce(
        lambda string, pattern: apply_pattern(pattern=pattern, string=string),
        patterns,
        line
    )


def clean_string(string: str) -> Iterable[str]:
    return map(clean_line, string.splitlines())


def clean(string: str) -> str:
    return ''.join(clean_string(string=string))
