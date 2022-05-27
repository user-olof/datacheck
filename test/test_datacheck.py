import pytest

from datacheck import XXX


@pytest.fixture
def control_data_list():
    return [["-47333", "SKATTEVERKET"],
            ["-7962", "SKATTEVERKET"],
            ["-246263", "GARANTITAK I KUMLA AB"],
            ["-4.2", "PRIS ENL SPEC"],
            ["250000", "FÄNSBODA AB"],
            ["50000", "FÄNSBODA AB"],
            ["-7962", "SKATTEVERKET"],
            ["-11.9", "PRIS ENL SPEC"],
            ["-15188", "JA:S BILSERVICE"]]

@pytest.fixture
def control_data_tuple():
    return (("-47333", "SKATTEVERKET"),
            ("-7962", "SKATTEVERKET"),
            ("-246263", "GARANTITAK I KUMLA AB"),
            ("-4.2", "PRIS ENL SPEC"),
            ("250000", "FÄNSBODA AB"),
            ("50000", "FÄNSBODA AB"),
            ("-7962", "SKATTEVERKET"),
            ("-11.9", "PRIS ENL SPEC"),
            ("-15188", "JA:S BILSERVICE"))



def test_int_int():
    arg = 4
    control_data = 5
    # datacheck = _DataCheck.setup(obj=arg, control_data=control_data)
    # res = datacheck.check_instances()
    types, values = XXX.compare(arg, control_data)
    assert types[0] is int and "Arg: 4 || Control data: 5" in str(values[0])


# this test is supposed to raise an exception
@pytest.mark.skip
def test_list_int():
    arg = ['a', 'b', 1234]
    control_data = 1234
    # datacheck = _DataCheck.setup(obj=arg, control_data=control_data)
    # res = datacheck.check_instances()
    res = XXX.compare(arg, control_data)
    assert len(res) > 0

def test_list_list(control_data_list):
    arg = [["-47333", "SKATTEVERKET"],
                ["-7962", "SKATTEVERKET"],
                ["-246263", "GARANTITAK I KUMLA AB"],
                ["-4.2", "PRIS ENL SPEC"],
                ["250000", "FÄNSBODA AB"],
                ["50000", "FÄNSBODA AB"],
                ["-7962", "SKATTEVERKET"],
                ["-11.9", "PRIS ENL SPEC"],
                ["-15188", "JA:S BILSERVICE"]]
    # control_data = 1234
    # datacheck = _DataCheck.setup(obj=arg, control_data=control_data_list)
    # res = datacheck.check_instances()
    res = XXX.compare(arg, control_data_list)
    assert len(res) > 0

def test_tuple_tuple(control_data_tuple):
    arg = (("-47333", "SKATTEVERKET"),
     ("-7962", "SKATTEVERKET"),
     ("-246263", "GARANTITAK I KUMLA AB"),
     ("-4.2", "PRIS ENL SPEC"),
     ("250000", "FÄNSBODA AB"),
     ("50000", "FÄNSBODA AB"),
     ("-7962", "SKATTEVERKET"),
     ("XXX", "PRIS ENL SPEC"),
     ("-15188", "JA:S BILSERVICE"))
    # datacheck = _DataCheck.setup(obj=arg, control_data=control_data_list)
    # res = datacheck.check_instances()
    res = XXX.compare(arg, control_data_tuple)
    assert len(res) > 0