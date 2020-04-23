import re

from mongo2json import cleaner


def test_apply_rule():
    pattern = re.compile(pattern=r'ObjectId\((.*)\)')
    string = '"_id" : ObjectId("5e6a39ba48a2151ff724399e"),'
    expect = '"_id" : "5e6a39ba48a2151ff724399e",'
    assert cleaner.apply_rule(pattern=pattern, string=string) == expect
