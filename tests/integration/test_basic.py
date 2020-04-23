import mongo2json


def test_type(basic_input):
    assert type(mongo2json.loads(basic_input)) == list
