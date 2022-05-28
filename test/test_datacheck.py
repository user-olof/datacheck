import pytest

from datacheck import XXX


@pytest.fixture
def control_data_list():
    return [["-47333", "aaa"],
            ["-7962", "bbb"],
            ["-246263", "ccc"],
            ["-4.2", "ddd"],
            ["250000", "eee"],
            ["50000", "fff"],
            ["-7962", "ggg"],
            ["-11.9", "hhh"],
            ["-15188", "iii"]]


@pytest.fixture
def control_data_tuple():
    return (("-47333", "aaa"),
            ("-7962", "bbb"),
            ("-246263", "ccc"),
            ("-4.2", "ddd"),
            ("250000", "eee"),
            ("50000", "fff"),
            ("-7962", "ggg"),
            ("-11.9", "hhh"),
            ("-15188", "iii"))


@pytest.fixture
def control_data_complicated():
    return ([["-47333", "aaa"],
             ("-7962", "bbb")],
            (),
            "-4.2",
            (((250000, "eee"),
              ("50000", "fff")),
             (-7962, "ggg")),
            ("-11.9", "hhh"),
            ("-15188", "iii"))


def test_int_int():
    arg = 4
    control_data = 5
    types, values = XXX.compare(arg, control_data)
    assert types[0] is int and "Arg: 4 || Control data: 5" in str(values[0])


# this test is supposed to raise an exception
@pytest.mark.skip
def test_list_int():
    arg = ['a', 'b', 1234]
    control_data = 1234
    res = XXX.compare(arg, control_data)
    assert len(res) > 0


def test_list_list(control_data_list):
    arg = [["-47333", "aaa"],
           ["-7962", "bbb"],
           ["-246263", "ccc"],
           ["-4.2", "ddd"],
           ["250000", "eee"],
           ["50000", "fff"],
           ["-7962", "ggg"],
           ["-11.9", "hhh"],
           ["-15188", "iii"]]
    res = XXX.compare(arg, control_data_list)
    assert len(res) > 0


def test_tuple_tuple(control_data_tuple):
    arg = (("-47333", "aaa"),
           ("-7962", "bbb"),
           ("-246263", "ccc"),
           ("-4.2", "ddd"),
           ("250000", "eee"),
           ("50000", "fff"),
           ("-7962", "ggg"),
           ("-11.9", "hhh"),
           ("-15188", "iii"))
    res = XXX.compare(arg, control_data_tuple)
    assert len(res) > 0


def test_complicated(control_data_complicated):
    arg = ([["-47333", "aaa"],
            ("-7962", "bbb")],
           (),
           "-4.2",
           (((250000, "eee"),
             ("50000", "fff")),
            (-7962, "ggg")),
           ("-11.9", "hhh"),
           ("-15188", "iii"))
    res = XXX.compare(arg, control_data_complicated)
    assert len(res) > 0
