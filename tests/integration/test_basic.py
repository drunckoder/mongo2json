import mongo2json


def test_type(basic_input, basic_big_input):
    assert isinstance(mongo2json.loads(basic_input), list)
    assert isinstance(mongo2json.loads(basic_big_input), list)
